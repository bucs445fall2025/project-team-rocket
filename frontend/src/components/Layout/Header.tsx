import React from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';

const Header: React.FC = () => {
  const { user, logout, isAdmin } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = async () => {
    try {
      await logout();
      navigate('/');
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  const isActive = (path: string) => location.pathname === path;

  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center py-4">
          <div className="flex items-center space-x-8">
            <Link to="/" className="text-xl font-bold text-primary-600">
              Internship Hub
            </Link>
            
            <nav className="flex space-x-6">
              <Link
                to="/"
                className={`text-sm font-medium ${
                  isActive('/') 
                    ? 'text-primary-600' 
                    : 'text-gray-600 hover:text-primary-600'
                }`}
              >
                Home
              </Link>
              
              {user && (
                <>
                  <Link
                    to="/create"
                    className={`text-sm font-medium ${
                      isActive('/create') 
                        ? 'text-primary-600' 
                        : 'text-gray-600 hover:text-primary-600'
                    }`}
                  >
                    Post Internship
                  </Link>
                  
                  {isAdmin() && (
                    <Link
                      to="/admin"
                      className={`text-sm font-medium ${
                        isActive('/admin') 
                          ? 'text-primary-600' 
                          : 'text-gray-600 hover:text-primary-600'
                      }`}
                    >
                      Admin
                    </Link>
                  )}
                </>
              )}
            </nav>
          </div>

          <div className="flex items-center space-x-4">
            {user ? (
              <div className="flex items-center space-x-4">
                <span className="text-sm text-gray-700">
                  Welcome, <span className="font-medium">{user.username}</span>
                </span>
                <button
                  onClick={handleLogout}
                  className="text-sm font-medium text-gray-600 hover:text-primary-600"
                >
                  Logout
                </button>
              </div>
            ) : (
              <div className="flex items-center space-x-4">
                <Link
                  to="/login"
                  className="text-sm font-medium text-gray-600 hover:text-primary-600"
                >
                  Login
                </Link>
                <Link
                  to="/signup"
                  className="bg-primary-600 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-primary-700"
                >
                  Sign Up
                </Link>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;