import React, { useState, useEffect } from 'react';
import { reportsAPI, adminAPI } from '../services/api';

// admin page - only admins can see this
const AdminPanel = () => {
  const [activeTab, setActiveTab] = useState('reports');
  const [reports, setReports] = useState([]);
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [statusFilter, setStatusFilter] = useState('pending');
  const [postStatusFilter, setPostStatusFilter] = useState('all');
  
  console.log('AdminPanel rendered, activeTab:', activeTab); // debug

  useEffect(() => {
    if (activeTab === 'reports') {
      fetchReports();
    } else {
      fetchPosts();
    }
  }, [activeTab, statusFilter, postStatusFilter]);

  const fetchReports = async () => {
    console.log('Fetching reports...'); // debug
    setLoading(true);
    try {
      const response = await reportsAPI.getReports({
        status: statusFilter === 'all' ? undefined : statusFilter,
        per_page: 50
      });
      setReports(response.data.reports);
      console.log('Got reports:', response.data.reports.length);
    } catch (error) {
      console.error('Error fetching reports:', error);
      setError('Failed to load reports');
    }
    setLoading(false);
  };

  const handleResolveReport = async (reportId: any, action: any) => {
    console.log('Resolving report:', reportId, action); // debug
    try {
      await reportsAPI.resolveReport(reportId, action);
      fetchReports(); // reload the reports
    } catch (error: any) {
      console.error('Error resolving report:', error);
      alert('Failed to resolve report: ' + (error.response?.data?.error || error.message));
    }
  };

  const fetchPosts = async () => {
    console.log('Fetching posts for admin...'); // debug
    setLoading(true);
    try {
      const response = await adminAPI.getAllPosts({
        status: postStatusFilter === 'all' ? undefined : postStatusFilter,
        per_page: 50
      });
      setPosts(response.data.posts);
      console.log('Got posts:', response.data.posts.length);
    } catch (error) {
      console.error('Error fetching posts:', error);
      setError('Failed to load posts');
    }
    setLoading(false);
  };

  const handleDeletePost = async (postId: any) => {
    // confirm before deleting
    if (!window.confirm('Are you sure you want to delete this post?')) {
      return;
    }
    
    console.log('Deleting post:', postId); // debug
    try {
      await adminAPI.deletePost(postId);
      fetchPosts(); // reload posts
    } catch (error: any) {
      console.error('Delete failed:', error);
      alert('Failed to delete post');
    }
  };

  const handleRestorePost = async (postId: any) => {
    console.log('Restoring post:', postId); // debug
    try {
      await adminAPI.restorePost(postId);
      fetchPosts(); // reload posts
    } catch (error: any) {
      console.error('Restore failed:', error);
      alert('Failed to restore post');
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="max-w-6xl mx-auto">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-2xl font-bold text-gray-900">Admin Panel</h1>
      </div>

      {/* Tabs */}
      <div className="border-b border-gray-200 mb-6">
        <nav className="-mb-px flex space-x-8">
          <button
            onClick={() => setActiveTab('reports')}
            className={`py-2 px-1 border-b-2 font-medium text-sm ${
              activeTab === 'reports'
                ? 'border-primary-500 text-primary-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            }`}
          >
            Reports
          </button>
          <button
            onClick={() => setActiveTab('posts')}
            className={`py-2 px-1 border-b-2 font-medium text-sm ${
              activeTab === 'posts'
                ? 'border-primary-500 text-primary-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            }`}
          >
            Posts Management
          </button>
        </nav>
      </div>

      {/* Filters */}
      <div className="mb-6">
        {activeTab === 'reports' ? (
          <select
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value)}
            className="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="pending">Pending Reports</option>
            <option value="resolved">Resolved Reports</option>
            <option value="all">All Reports</option>
          </select>
        ) : (
          <select
            value={postStatusFilter}
            onChange={(e) => setPostStatusFilter(e.target.value)}
            className="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="all">All Posts</option>
            <option value="active">Active Posts</option>
            <option value="deleted">Deleted Posts</option>
            <option value="expired">Expired Posts</option>
          </select>
        )}
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-md mb-6">
          {error}
        </div>
      )}

      {loading ? (
        <div className="text-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
          <p className="mt-2 text-gray-500">Loading {activeTab}...</p>
        </div>
      ) : activeTab === 'reports' ? (
        reports.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-500 text-lg">No reports found</p>
          </div>
        ) : (
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Post
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Reporter
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Reason
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Status
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Date
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Actions
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {reports.map((report: any) => (
                  <tr key={report.id}>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div>
                        <div className="text-sm font-medium text-gray-900">
                          {report.post.title}
                        </div>
                        <div className="text-sm text-gray-500">
                          by {report.post.author.username}
                        </div>
                        <div className="text-xs text-gray-400">
                          Status: {report.post.status}
                        </div>
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="text-sm text-gray-900">{report.reporter.username}</div>
                    </td>
                    <td className="px-6 py-4">
                      <div className="text-sm text-gray-900 max-w-xs truncate">
                        {report.reason}
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${
                        report.status === 'pending' 
                          ? 'bg-yellow-100 text-yellow-800'
                          : 'bg-green-100 text-green-800'
                      }`}>
                        {report.status}
                      </span>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {formatDate(report.created_at)}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                      {report.status === 'pending' && (
                        <div className="space-x-2">
                          <button
                            onClick={() => handleResolveReport(report.id, 'dismiss')}
                            className="text-gray-600 hover:text-gray-900"
                          >
                            Dismiss
                          </button>
                          <button
                            onClick={() => handleResolveReport(report.id, 'delete_post')}
                            className="text-red-600 hover:text-red-900"
                          >
                            Delete Post
                          </button>
                          <button
                            onClick={() => handleResolveReport(report.id, 'expire_post')}
                            className="text-orange-600 hover:text-orange-900"
                          >
                            Mark Expired
                          </button>
                        </div>
                      )}
                      {report.status === 'resolved' && report.reviewed_by && (
                        <div className="text-xs text-gray-500">
                          Resolved by {report.reviewed_by.username}
                          <br />
                          {report.reviewed_at && formatDate(report.reviewed_at)}
                        </div>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
        )
      ) : (
        // Posts Management Tab
        posts.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-500 text-lg">No posts found</p>
          </div>
        ) : (
          <div className="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
            <div className="overflow-x-auto">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Post Details
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Author
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Status
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Stats
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Date
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Actions
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {posts.map((post: any) => (
                    <tr key={post.id}>
                      <td className="px-6 py-4">
                        <div>
                          <div className="text-sm font-medium text-gray-900 max-w-xs truncate">
                            {post.title}
                          </div>
                          {post.company && (
                            <div className="text-sm text-gray-500">
                              {post.company}
                            </div>
                          )}
                          <div className="text-xs text-gray-400">
                            ID: {post.id}
                          </div>
                        </div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <div className="text-sm text-gray-900">{post.author.username}</div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${
                          post.status === 'active' 
                            ? 'bg-green-100 text-green-800'
                            : post.status === 'deleted'
                            ? 'bg-red-100 text-red-800'
                            : 'bg-yellow-100 text-yellow-800'
                        }`}>
                          {post.status || 'active'}
                        </span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        <div>Score: {post.vote_score}</div>
                        <div>Reports: {post.report_count || 0}</div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {formatDate(post.created_at)}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                        {(post.status || 'active') === 'active' ? (
                          <button
                            onClick={() => handleDeletePost(post.id)}
                            className="text-red-600 hover:text-red-900 mr-3"
                          >
                            Delete
                          </button>
                        ) : (
                          <button
                            onClick={() => handleRestorePost(post.id)}
                            className="text-green-600 hover:text-green-900 mr-3"
                          >
                            Restore
                          </button>
                        )}
                        <a
                          href={post.link}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-primary-600 hover:text-primary-900"
                        >
                          View
                        </a>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )
      )}
    </div>
  );
};

export default AdminPanel;