// Simple validation functions for forms

export function validateEmail(email: string): string | null {
  if (!email) return 'Email is required';
  if (!email.includes('@') || !email.includes('.')) {
    return 'Please enter a valid email';
  }
  return null;
}

export function validatePassword(password: string): string | null {
  if (!password) return 'Password is required';
  if (password.length < 6) {
    return 'Password must be at least 6 characters';
  }
  return null;
}

export function validateUsername(username: string): string | null {
  if (!username) return 'Username is required';
  if (username.length < 3) {
    return 'Username must be at least 3 characters';
  }
  return null;
}

export function validateRequired(value: string, fieldName: string): string | null {
  if (!value || !value.trim()) {
    return `${fieldName} is required`;
  }
  return null;
}

export function validatePostTitle(title: string): string | null {
  if (!title || !title.trim()) return 'Title is required';
  if (title.trim().length < 5) {
    return 'Title must be at least 5 characters';
  }
  return null;
}

export function validatePostDescription(description: string): string | null {
  if (!description || !description.trim()) return 'Description is required';
  if (description.trim().length < 20) {
    return 'Description must be at least 20 characters';
  }
  return null;
}

export function validateURL(url: string): string | null {
  if (!url || !url.trim()) return 'Link is required';
  if (!url.startsWith('http://') && !url.startsWith('https://')) {
    return 'Please enter a valid URL (starting with http:// or https://)';
  }
  return null;
}
