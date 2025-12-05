import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Post, postsAPI } from '../services/api';
import { useAuth } from '../contexts/AuthContext';
import PostCard from '../components/Posts/PostCard';
import { debug } from '../lib/utils';

const Home = () => {  // removed React.FC - not sure what that does anyway
  const { user } = useAuth();
  const [posts, setPosts] = useState<any[]>([]);  // any type cause typescript is confusing
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const [tags, setTags] = useState('');
  const [sortBy, setSortBy] = useState('recent');  // removed type
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  
  console.log('Home component rendered, user:', user);  // debug

  const fetchPosts = async (resetPage = false) => {
    debug('fetchPosts called', { resetPage, page, searchTerm });
    setLoading(true);
    const currentPage = resetPage ? 1 : page;
    
    try {
      const response = await postsAPI.getPosts({
        page: currentPage,
        per_page: 20,
        search: searchTerm.trim() || undefined,
        tags: tags.trim() || undefined,
        sort: sortBy,
      });
      
      console.log('API response:', response);  // debug
      setPosts(response.data.posts);
      setTotalPages(response.data.pagination.pages);
      
      if (resetPage) {
        setPage(1);
      }
    } catch (error) {
      console.error('Error fetching posts:', error);
      setError('Failed to load posts');
    }
    
    setLoading(false);
  };

  useEffect(() => {
    console.log('useEffect triggered - fetching posts');
    fetchPosts();
  }, [page, sortBy]);  // TODO: maybe add searchTerm here too?

  const handleSearch = (e: any) => {  // just use any for form events
    e.preventDefault();
    console.log('Search submitted:', searchTerm, tags);
    fetchPosts(true);
  };

  const handleVoteUpdate = (postId: number, newScore: number, userVote: any) => {
    setPosts((prevPosts: any) =>
      prevPosts.map((post: any) =>
        post.id === postId
          ? { ...post, vote_score: newScore, user_vote: userVote }
          : post
      )
    );
  };

  return (
    <div>
      {/* Hero section */}
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Discover Internship Opportunities
        </h1>
        <p className="text-lg text-gray-600 mb-6">
          Share and find internships with fellow students
        </p>
        
        {user && (
          <Link
            to="/create"
            className="inline-flex items-center px-4 py-2 bg-primary-600 text-white font-medium rounded-md hover:bg-primary-700"
          >
            Post an Internship
          </Link>
        )}
        
        {!user && (
          <div className="space-x-4">
            <Link
              to="/login"
              className="inline-flex items-center px-4 py-2 border border-primary-600 text-primary-600 font-medium rounded-md hover:bg-primary-50"
            >
              Login
            </Link>
            <Link
              to="/signup"
              className="inline-flex items-center px-4 py-2 bg-primary-600 text-white font-medium rounded-md hover:bg-primary-700"
            >
              Sign Up
            </Link>
          </div>
        )}
      </div>

      {/* Search and filters */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <form onSubmit={handleSearch} className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Search
              </label>
              <input
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="Search by title, description, or company..."
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Tags
              </label>
              <input
                type="text"
                value={tags}
                onChange={(e) => setTags(e.target.value)}
                placeholder="e.g. Software Engineering, Remote"
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Sort By
              </label>
              <select
                value={sortBy}
                onChange={(e) => setSortBy(e.target.value as 'recent' | 'popular')}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-primary-500 focus:border-primary-500"
              >
                <option value="recent">Most Recent</option>
                <option value="popular">Most Popular</option>
              </select>
            </div>
          </div>
          
          <div className="flex justify-end">
            <button
              type="submit"
              className="px-4 py-2 bg-primary-600 text-white font-medium rounded-md hover:bg-primary-700"
            >
              Search
            </button>
          </div>
        </form>
      </div>

      {/* Posts */}
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-md mb-6">
          {error}
        </div>
      )}

      {loading ? (
        <div className="text-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
          <p className="mt-2 text-gray-500">Loading posts...</p>
        </div>
      ) : posts.length === 0 ? (
        <div className="text-center py-12">
          <p className="text-gray-500 text-lg">No internships found</p>
          {user && (
            <Link
              to="/create"
              className="mt-4 inline-flex items-center px-4 py-2 bg-primary-600 text-white font-medium rounded-md hover:bg-primary-700"
            >
              Post the first internship
            </Link>
          )}
        </div>
      ) : (
        <>
          <div className="space-y-6">
            {posts.map((post: any) => (
              <PostCard
                key={post.id}
                post={post}
                onVoteUpdate={handleVoteUpdate}
              />
            ))}
          </div>

          {/* Simple pagination */}
          {totalPages > 1 && (
            <div className="flex justify-center mt-8 space-x-2">
              <button
                onClick={() => setPage(page - 1)}
                disabled={page === 1}
                className="px-4 py-2 border border-gray-300 text-gray-700 rounded-md hover:bg-gray-50 disabled:opacity-50"
              >
                Previous
              </button>
              
              <span className="px-4 py-2 text-gray-700">
                Page {page} of {totalPages}
              </span>
              
              <button
                onClick={() => setPage(page + 1)}
                disabled={page === totalPages}
                className="px-4 py-2 border border-gray-300 text-gray-700 rounded-md hover:bg-gray-50 disabled:opacity-50"
              >
                Next
              </button>
            </div>
          )}
        </>
      )}
    </div>
  );
};

export default Home;