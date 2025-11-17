import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { Post, Comment, postsAPI, commentsAPI, votesAPI, reportsAPI } from '../services/api';
import { useAuth } from '../contexts/AuthContext';

const PostDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const { user } = useAuth();
  const navigate = useNavigate();
  
  const [post, setPost] = useState<Post | null>(null);
  const [comments, setComments] = useState<Comment[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [newComment, setNewComment] = useState('');
  const [commentLoading, setCommentLoading] = useState(false);
  const [voting, setVoting] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [editForm, setEditForm] = useState({
    title: '',
    description: '',
    company: '',
    link: '',
    tags: ''
  });
  const [editingCommentId, setEditingCommentId] = useState<number | null>(null);
  const [editCommentContent, setEditCommentContent] = useState('');

  useEffect(() => {
    if (id) {
      fetchPostData();
    }
  }, [id]);

  const fetchPostData = async () => {
    try {
      setLoading(true);
      const postResponse = await postsAPI.getPost(Number(id));
      setPost(postResponse.data.post);
      setComments(postResponse.data.comments);
    } catch (error) {
      setError('Failed to load post');
      console.error('Error fetching post:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleVote = async (voteType: 'up' | 'down') => {
    if (!user || !post || voting) return;

    setVoting(true);
    try {
      const response = await votesAPI.vote(post.id, voteType);
      setPost({
        ...post,
        vote_score: response.data.post.vote_score,
        user_vote: response.data.post.user_vote
      });
    } catch (error) {
      console.error('Vote failed:', error);
    } finally {
      setVoting(false);
    }
  };

  const handleAddComment = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!user || !post || !newComment.trim() || commentLoading) return;

    setCommentLoading(true);
    try {
      const response = await commentsAPI.createComment(post.id, newComment.trim());
      setComments([...comments, response.data.comment]);
      setNewComment('');
      setPost({
        ...post,
        comment_count: post.comment_count + 1
      });
    } catch (error: any) {
      alert(error.response?.data?.error || 'Failed to add comment');
    } finally {
      setCommentLoading(false);
    }
  };

  const handleDeletePost = async () => {
    if (!post || !window.confirm('Are you sure you want to delete this post?')) return;

    try {
      await postsAPI.deletePost(post.id);
      navigate('/');
    } catch (error: any) {
      alert(error.response?.data?.error || 'Failed to delete post');
    }
  };

  const handleEditClick = () => {
    if (!post) return;
    setEditForm({
      title: post.title,
      description: post.description,
      company: post.company || '',
      link: post.link,
      tags: post.tags.join(', ')
    });
    setIsEditing(true);
  };

  const handleEditSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!post) return;

    try {
      const response = await postsAPI.updatePost(post.id, {
        title: editForm.title.trim(),
        description: editForm.description.trim(),
        company: editForm.company.trim() || undefined,
        link: editForm.link.trim(),
        tags: editForm.tags.trim() || undefined
      });

      // update the post with new data
      setPost({
        ...post,
        title: response.data.post.title,
        description: response.data.post.description,
        company: response.data.post.company,
        link: response.data.post.link,
        tags: response.data.post.tags,
        updated_at: response.data.post.updated_at
      });
      setIsEditing(false);
    } catch (error: any) {
      alert(error.response?.data?.error || 'Failed to update post');
    }
  };

  const handleEditComment = (comment: Comment) => {
    setEditingCommentId(comment.id);
    setEditCommentContent(comment.content);
  };

  const handleSaveComment = async (commentId: number) => {
    if (!editCommentContent.trim()) return;

    try {
      const response = await commentsAPI.updateComment(commentId, editCommentContent.trim());

      // update the comment in the list
      setComments(comments.map(c =>
        c.id === commentId
          ? { ...c, content: response.data.comment.content }
          : c
      ));
      setEditingCommentId(null);
      setEditCommentContent('');
    } catch (error: any) {
      alert(error.response?.data?.error || 'Failed to update comment');
    }
  };

  const handleDeleteComment = async (commentId: number) => {
    if (!window.confirm('Are you sure you want to delete this comment?')) return;

    try {
      await commentsAPI.deleteComment(commentId);
      setComments(comments.filter(c => c.id !== commentId));

      // update comment count
      if (post) {
        setPost({
          ...post,
          comment_count: post.comment_count - 1
        });
      }
    } catch (error: any) {
      alert(error.response?.data?.error || 'Failed to delete comment');
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (loading) {
    return (
      <div className="text-center py-8">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
        <p className="mt-2 text-gray-500">Loading post...</p>
      </div>
    );
  }

  if (error || !post) {
    return (
      <div className="text-center py-8">
        <p className="text-red-600">{error}</p>
        <Link to="/" className="mt-4 text-primary-600 hover:text-primary-700">
          ← Back to home
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto">
      {/* Back button */}
      <Link to="/" className="inline-flex items-center text-primary-600 hover:text-primary-700 mb-6">
        ← Back to all posts
      </Link>

      {/* Post */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-8">
        <div className="flex items-start space-x-6">
          {/* Vote buttons */}
          {user && (
            <div className="flex flex-col items-center space-y-2">
              <button
                onClick={() => handleVote('up')}
                disabled={voting}
                className={`p-3 rounded-full transition-colors ${
                  post.user_vote === 'up'
                    ? 'bg-green-100 text-green-600'
                    : 'text-gray-400 hover:text-green-600 hover:bg-green-50'
                }`}
              >
                ▲
              </button>
              <span className={`text-lg font-medium ${
                post.vote_score > 0 ? 'text-green-600' : 
                post.vote_score < 0 ? 'text-red-600' : 'text-gray-500'
              }`}>
                {post.vote_score}
              </span>
              <button
                onClick={() => handleVote('down')}
                disabled={voting}
                className={`p-3 rounded-full transition-colors ${
                  post.user_vote === 'down'
                    ? 'bg-red-100 text-red-600'
                    : 'text-gray-400 hover:text-red-600 hover:bg-red-50'
                }`}
              >
                ▼
              </button>
            </div>
          )}

          {/* Post content */}
          <div className="flex-1">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center space-x-2 text-sm text-gray-500">
                <span>Posted by <span className="font-medium">{post.author.username}</span></span>
                <span>•</span>
                <span>{formatDate(post.created_at)}</span>
                {post.company && (
                  <>
                    <span>•</span>
                    <span className="font-medium text-gray-700">{post.company}</span>
                  </>
                )}
              </div>

              {post.can_edit && (
                <div className="flex items-center space-x-3">
                  <button
                    onClick={handleEditClick}
                    className="text-blue-600 hover:text-blue-700 text-sm"
                  >
                    Edit
                  </button>
                  <button
                    onClick={handleDeletePost}
                    className="text-red-600 hover:text-red-700 text-sm"
                  >
                    Delete
                  </button>
                </div>
              )}
            </div>

            <h1 className="text-2xl font-bold text-gray-900 mb-4">{post.title}</h1>
            
            <div className="prose max-w-none mb-6">
              <p className="text-gray-700 whitespace-pre-wrap">{post.description}</p>
            </div>

            {post.tags.length > 0 && (
              <div className="flex flex-wrap gap-2 mb-6">
                {post.tags.map((tag: any, index: any) => (
                  <span
                    key={index}
                    className="px-3 py-1 bg-gray-100 text-gray-700 text-sm rounded-full"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            )}

            <div className="flex items-center justify-between">
              <span className="text-sm text-gray-500">
                {post.comment_count} comments
              </span>
              <a
                href={post.link}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center px-4 py-2 bg-primary-600 text-white font-medium rounded-md hover:bg-primary-700"
              >
                Apply Now →
              </a>
            </div>
          </div>
        </div>
      </div>

      {/* Comments section */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">
          Comments ({post.comment_count})
        </h2>

        {/* Add comment form */}
        {user ? (
          <form onSubmit={handleAddComment} className="mb-6">
            <textarea
              value={newComment}
              onChange={(e) => setNewComment(e.target.value)}
              placeholder="Add a comment..."
              className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
              rows={3}
            />
            <div className="flex justify-end mt-2">
              <button
                type="submit"
                disabled={commentLoading || !newComment.trim()}
                className="px-4 py-2 bg-primary-600 text-white font-medium rounded-md hover:bg-primary-700 disabled:opacity-50"
              >
                {commentLoading ? 'Adding...' : 'Add Comment'}
              </button>
            </div>
          </form>
        ) : (
          <div className="mb-6 p-4 bg-gray-50 rounded-md text-center">
            <Link to="/login" className="text-primary-600 hover:text-primary-700">
              Login
            </Link>{' '}
            to add a comment
          </div>
        )}

        {/* Comments list */}
        {comments.length === 0 ? (
          <p className="text-gray-500 text-center py-4">No comments yet</p>
        ) : (
          <div className="space-y-4">
            {comments.map((comment) => (
              <div key={comment.id} className="border-b border-gray-100 pb-4 last:border-b-0">
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center space-x-2 text-sm text-gray-500">
                    <span className="font-medium text-gray-900">{comment.author.username}</span>
                    <span>•</span>
                    <span>{formatDate(comment.created_at)}</span>
                  </div>

                  {comment.can_edit && (
                    <div className="flex items-center space-x-3 text-sm">
                      <button
                        onClick={() => handleEditComment(comment)}
                        className="text-blue-600 hover:text-blue-700"
                      >
                        Edit
                      </button>
                      <button
                        onClick={() => handleDeleteComment(comment.id)}
                        className="text-red-600 hover:text-red-700"
                      >
                        Delete
                      </button>
                    </div>
                  )}
                </div>

                {editingCommentId === comment.id ? (
                  <div className="mt-2">
                    <textarea
                      value={editCommentContent}
                      onChange={(e) => setEditCommentContent(e.target.value)}
                      className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                      rows={3}
                    />
                    <div className="flex items-center justify-end space-x-2 mt-2">
                      <button
                        onClick={() => {
                          setEditingCommentId(null);
                          setEditCommentContent('');
                        }}
                        className="px-3 py-1 text-sm text-gray-600 hover:text-gray-800"
                      >
                        Cancel
                      </button>
                      <button
                        onClick={() => handleSaveComment(comment.id)}
                        className="px-3 py-1 bg-primary-600 text-white text-sm rounded-md hover:bg-primary-700"
                      >
                        Save
                      </button>
                    </div>
                  </div>
                ) : (
                  <p className="text-gray-700 whitespace-pre-wrap">{comment.content}</p>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Edit modal */}
      {isEditing && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg shadow-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto p-6">
            <h2 className="text-2xl font-bold text-gray-900 mb-6">Edit Post</h2>

            <form onSubmit={handleEditSubmit} className="space-y-6">
              <div>
                <label htmlFor="edit-title" className="block text-sm font-medium text-gray-700 mb-1">
                  Title *
                </label>
                <input
                  id="edit-title"
                  type="text"
                  required
                  value={editForm.title}
                  onChange={(e) => setEditForm({...editForm, title: e.target.value})}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                />
              </div>

              <div>
                <label htmlFor="edit-company" className="block text-sm font-medium text-gray-700 mb-1">
                  Company
                </label>
                <input
                  id="edit-company"
                  type="text"
                  value={editForm.company}
                  onChange={(e) => setEditForm({...editForm, company: e.target.value})}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                />
              </div>

              <div>
                <label htmlFor="edit-link" className="block text-sm font-medium text-gray-700 mb-1">
                  Application Link *
                </label>
                <input
                  id="edit-link"
                  type="url"
                  required
                  value={editForm.link}
                  onChange={(e) => setEditForm({...editForm, link: e.target.value})}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                />
              </div>

              <div>
                <label htmlFor="edit-description" className="block text-sm font-medium text-gray-700 mb-1">
                  Description *
                </label>
                <textarea
                  id="edit-description"
                  required
                  rows={6}
                  value={editForm.description}
                  onChange={(e) => setEditForm({...editForm, description: e.target.value})}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                />
              </div>

              <div>
                <label htmlFor="edit-tags" className="block text-sm font-medium text-gray-700 mb-1">
                  Tags
                </label>
                <input
                  id="edit-tags"
                  type="text"
                  value={editForm.tags}
                  onChange={(e) => setEditForm({...editForm, tags: e.target.value})}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                  placeholder="Separate with commas"
                />
              </div>

              <div className="flex items-center justify-end space-x-3 pt-4 border-t border-gray-200">
                <button
                  type="button"
                  onClick={() => setIsEditing(false)}
                  className="px-4 py-2 border border-gray-300 text-gray-700 rounded-md hover:bg-gray-50"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 bg-primary-600 text-white font-medium rounded-md hover:bg-primary-700"
                >
                  Save Changes
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

export default PostDetail;