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
                <button
                  onClick={handleDeletePost}
                  className="text-red-600 hover:text-red-700 text-sm"
                >
                  Delete
                </button>
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
                </div>
                <p className="text-gray-700 whitespace-pre-wrap">{comment.content}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default PostDetail;