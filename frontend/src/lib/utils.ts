// utility functions

// combine css classes - found this online
export function cn(...classes: any[]): string {
  return classes.filter(Boolean).join(' ');
}

// format dates
export function formatDate(date: any): string {
  const d = new Date(date);
  return d.toLocaleDateString();
}

// check if email is valid
export function isValidEmail(email: string): boolean {
  return email.includes('@') && email.includes('.');
}

// make text shorter if too long
export function truncateText(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength) + '...';
}

// debug helper
export function debug(msg: string, data?: any) {
  console.log(`[DEBUG] ${msg}`, data);
}
