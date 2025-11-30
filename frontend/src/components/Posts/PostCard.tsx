import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Post } from '../../services/api';
import { useAuth } from '../../contexts/AuthContext';
import { votesAPI, reportsAPI } from '../../services/api';

interface PostCardProps {
  post: Post;
  onVoteUpdate?: (postId: number, newScore: number, userVote: 'up' | 'down' | null) => void;
}

const PostCard: React.FC<PostCardProps> = ({ post, onVoteUpdate }) => {
  const { user } = useAuth();
  const [voting, setVoting] = useState(false);
  const [reporting, setReporting] = useState(false);
  const [showReportForm, setShowReportForm] = useState(false);
  const [reportReason, setReportReason] = useState('');

  const handleVote = async (voteType: 'up' | 'down') => {
    if (!user || voting) return;

    setVoting(true);
    try {
      const response = await votesAPI.vote(post.id, voteType);
      if (onVoteUpdate) {
        onVoteUpdate(post.id, response.data.post.vote_score, response.data.post.user_vote);
      }
    } catch (error) {
      console.error('Vote failed:', error);
    } finally {
      setVoting(false);
    }
  };

  const handleReport = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!user || reporting || !reportReason.trim()) return;

    setReporting(true);
    try {
      await reportsAPI.createReport(post.id, reportReason.trim());
      setShowReportForm(false);
      setReportReason('');
      alert('Post reported successfully. Thank you for helping keep the community clean.');
    } catch (error: any) {
      alert(error.response?.data?.error || 'Failed to report post');
    } finally {
      setReporting(false);
    }
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString();
  };

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow">
      <div className="flex items-start space-x-4">
        {/* Vote buttons */}
        {user && (
          <div className="flex flex-col items-center space-y-1">
            <button
              onClick={() => handleVote('up')}
              disabled={voting}
              className={`p-2 rounded-full transition-colors ${
                post.user_vote === 'up'
                  ? 'bg-green-100 text-green-600'
                  : 'text-gray-400 hover:text-green-600 hover:bg-green-50'
              }`}
            >
              ▲
            </button>
            <span className={`text-sm font-medium ${
              post.vote_score > 0 ? 'text-green-600' : 
              post.vote_score < 0 ? 'text-red-600' : 'text-gray-500'
            }`}>
              {post.vote_score}
            </span>
            <button
              onClick={() => handleVote('down')}
              disabled={voting}
              className={`p-2 rounded-full transition-colors ${
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
          <div className="flex items-center justify-between mb-2">
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
            
            {user && (
              <div className="flex items-center space-x-2">
                <button
                  onClick={() => setShowReportForm(!showReportForm)}
                  className="text-gray-400 hover:text-red-500 text-sm"
                >
                  Report
                </button>
              </div>
            )}
          </div>

          <Link to={`/posts/${post.id}`} className="block group">
            <h3 className="text-lg font-semibold text-gray-900 group-hover:text-primary-600 mb-2">
              {post.title}
            </h3>
            <p className="text-gray-600 mb-3 line-clamp-3">
              {post.description}
            </p>
          </Link>

          {post.tags.length > 0 && (
            <div className="flex flex-wrap gap-2 mb-3">
              {post.tags.map((tag: any, index: any) => (
                <span
                  key={index}
                  className="px-2 py-1 bg-gray-100 text-gray-700 text-xs rounded-full"
                >
                  {tag}
                </span>
              ))}
            </div>
          )}

          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4 text-sm text-gray-500">
              <Link
                to={`/posts/${post.id}`}
                className="hover:text-primary-600"
              >
                {post.comment_count} comments
              </Link>
              <a
                href={post.link}
                target="_blank"
                rel="noopener noreferrer"
                className="text-primary-600 hover:text-primary-700 font-medium"
              >
                View Internship →
              </a>
            </div>
          </div>

          {/* Report form */}
          {showReportForm && (
            <form onSubmit={handleReport} className="mt-4 p-4 bg-gray-50 rounded-lg">
              <h4 className="font-medium text-gray-900 mb-2">Report this post</h4>
              <textarea
                value={reportReason}
                onChange={(e) => setReportReason(e.target.value)}
                placeholder="Why are you reporting this post? (e.g., job no longer available, spam, inappropriate content)"
                className="w-full p-2 border border-gray-300 rounded-md text-sm"
                rows={3}
                required
              />
              <div className="flex items-center justify-end space-x-2 mt-2">
                <button
                  type="button"
                  onClick={() => setShowReportForm(false)}
                  className="px-3 py-1 text-sm text-gray-600 hover:text-gray-800"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={reporting || !reportReason.trim()}
                  className="px-3 py-1 bg-red-600 text-white text-sm rounded-md hover:bg-red-700 disabled:opacity-50"
                >
                  {reporting ? 'Reporting...' : 'Report'}
                </button>
              </div>
            </form>
          )}
        </div>
      </div>
    </div>
  );
};

export default PostCard;