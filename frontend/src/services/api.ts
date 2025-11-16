import axios from 'axios';

// api setup
const api = axios.create({
  baseURL: 'http://localhost:5001/api',
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
  },
});

// debug api calls
api.interceptors.request.use(request => {
  console.log('API Request:', request.method, request.url);
  return request;
});

// basic types - probably should organize these better
export interface User {
  id: number;
  username: string;
  email: string;
  role: string;
  created_at: string;
}

export interface Post {
  id: number;
  title: string;
  description: string;
  company?: string;
  link: string;
  tags: any;  // sometimes string, sometimes array - need to fix this
  author: {
    id: number;
    username: string;
  };
  vote_score: number;
  user_vote?: any;  // 'up' | 'down' | null but whatever
  comment_count: number;
  created_at: string;
  updated_at: string;
  can_edit?: boolean;
  // admin stuff
  status?: string;
  approved?: boolean;
  report_count?: number;
}

export interface Comment {
  id: number;
  content: string;
  author: any;  // has id and username but whatever
  created_at: string;
  can_edit: boolean;
}

export interface Report {
  id: number;
  post: any;  // post object with nested author
  reporter: any;  // user object
  reason: string;
  status: string;
  reviewed_by?: any;  // user object or null
  created_at: string;
  reviewed_at?: string;
}

// pagination stuff - copied from somewhere
export interface PaginationResponse<T> {
  items: T;
  pagination: {
    page: number;
    pages: number;
    per_page: number;
    total: number;
    has_next: boolean;
    has_prev: boolean;
  };
}

// auth stuff
export const authAPI = {
  signup: (userData: any) => api.post('/auth/signup', userData),
  login: (credentials: any) => api.post('/auth/login', credentials),
  logout: () => api.post('/auth/logout'),
  getCurrentUser: () => api.get('/auth/me'),
};

// posts api
export const postsAPI = {
  getPosts: (params?: any) => api.get('/posts', { params }),
  getPost: (id: number) => api.get(`/posts/${id}`),
  createPost: (postData: any) => api.post('/posts', postData),
  updatePost: (id: number, postData: any) => api.put(`/posts/${id}`, postData),
  deletePost: (id: number) => api.delete(`/posts/${id}`),
};

// voting
export const votesAPI = {
  vote: (postId: number, voteType: string) => 
    api.post('/votes', { post_id: postId, vote_type: voteType }),
  getPostVotes: (postId: number) => api.get(`/votes/post/${postId}`),
};

// comments 
export const commentsAPI = {
  getPostComments: (postId: number) => api.get(`/comments/post/${postId}`),
  createComment: (postId: number, content: string) => 
    api.post('/comments', { post_id: postId, content }),
  updateComment: (id: number, content: string) => 
    api.put(`/comments/${id}`, { content }),
  deleteComment: (id: number) => api.delete(`/comments/${id}`),
};

// reports
export const reportsAPI = {
  createReport: (postId: number, reason: string) =>
    api.post('/reports', { post_id: postId, reason }),
  getReports: (params?: any) => api.get('/reports', { params }),
  resolveReport: (id: number, action: string) =>
    api.post(`/reports/${id}/resolve`, { action }),
  markPostDeleted: (postId: number) =>
    api.post(`/reports/post/${postId}/mark-deleted`),
};

// admin functions
export const adminAPI = {
  getAllPosts: (params?: any) => api.get('/admin/posts', { params }),
  deletePost: (postId: number) => api.post(`/admin/posts/${postId}/delete`),
  restorePost: (postId: number) => api.post(`/admin/posts/${postId}/restore`),
  getAllUsers: (params?: any) => api.get('/admin/users', { params }),
};

// TODO: add error handling for failed api calls
// TODO: maybe add some loading indicators?
// FIXME: the error messages could be better

// helper function we never use
export function formatApiError(error: any) {
  // started writing this but never finished it
  return error.message || 'Something went wrong';
}

export default api;