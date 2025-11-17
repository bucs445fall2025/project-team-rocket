# Sprint Meeting Notes

**Attended**: Alex Eskenazi, Vaughn Stout, Vishil Patel

**DATE**: November 17, 2025

***

## Sprint 10 Review

### SRS Sections Updated

- Updated security requirements section with password validation improvements
- Added edit functionality documentation for posts and comments
- Database optimization notes added to performance section

### User Story

**User Story 2.2: Edit Own Posts**
- As a user, I want to edit my own posts so that I can fix typos or update information that changed

**User Story 3.3: Edit/Delete Own Comments**
- As a commenter, I want to edit or delete my comments so that I can correct mistakes or remove comments I no longer want visible

### Sprint Requirements Attempted

• Users can edit or delete their own posts anytime

• Users can see who commented and when, with ability to edit/delete their own comments

• Focused on security and reliability with proper data validation

### Completed Requirements

• Strengthened password requirements from 6 to 8 characters minimum with complexity rules (uppercase, lowercase, number, special character)

• Added edit functionality for posts on the frontend with modal form similar to create post

• Added edit functionality for comments with inline editing UI

• Database performance improvements with indexes on frequently queried columns (Post.status, Post.vote_score, Post.author_id)

• All edit operations properly check permissions (users can only edit their own content, admins can edit anything)

### Incomplete Requirements

• SECRET_KEY is still hardcoded in app.py - needs to be moved to environment variable but we ran out of time. The fix is planned but requires everyone on the team to update their local setup which is a coordination issue.

• Rate limiting is not implemented - wanted to add this to prevent brute force login attacks but didn't get to it this sprint

• Post approval/moderation system still not implemented - posts go live immediately without admin review

### The summary of the entire project

Internship Hub is a web application where college students can share and discover internship opportunities. Users can post internships with company details, descriptions, and application links. Other students can vote on posts to surface the best opportunities, leave comments with questions or experiences, and search/filter to find relevant internships. The platform includes user authentication, a voting system similar to Reddit, commenting functionality, and an admin panel for content moderation. Built with Flask/SQLAlchemy backend and React/TypeScript frontend with a SQLite database. The app now supports full CRUD operations on posts and comments with proper permission checking.

***

## Sprint 11 Planning

## Requirements Flex

3/5 requirement flexes remaining

## Technical Debt

• SECRET_KEY environment variable migration - needs coordination across team
• Rate limiting implementation for API endpoints
• Post moderation/approval workflow

### Requirement Target

• Moderators can approve posts before they go public

• Advanced search with filters (location, pay range, post date, etc.)

• User profile pages showing their posts and comment history

### User Stories

**User Story 5.1: Post Moderation**
- As a moderator, I want to review and approve posts before they appear publicly so that we can maintain quality content

**User Story 4.1: Advanced Search**
- As a student, I want to filter internships by location, salary, and date posted so that I can find opportunities that match my specific criteria

**User Story 6.1: User Profiles**
- As a user, I want to view my profile and see all my posts and comments in one place so that I can track my activity

### Planning

1. Implement SECRET_KEY environment variable - create .env file, update app.py to use python-dotenv, document setup process for team

2. Add rate limiting to login and signup endpoints using Flask-Limiter to prevent brute force attacks

3. Build post moderation system - add approval workflow, moderator dashboard, notification system for pending posts

4. Create user profile pages with activity history

### Action Items

- Vaughn: Finish SECRET_KEY migration, add rate limiting, write documentation
- Alex: Build moderator dashboard UI, create user profile pages
- Vishil: Implement approval workflow in backend, optimize queries for new features

### Issues and Risks

• Environment variable setup requires all team members to create local .env files which could cause confusion

• Final exams coming up in a few weeks so time is limited

• Rate limiting might be tricky to test properly without automated tests

• Moderation system is complex and might take longer than one sprint

### Team Work Assignments

**Alex Eskenazi:**
- Create moderator dashboard component for reviewing pending posts
- Build user profile page showing post and comment history
- Add approval/reject buttons to admin interface
- Test all new UI features

**Vaughn Stout:**
- Complete SECRET_KEY environment variable migration
- Implement Flask-Limiter for rate limiting on auth endpoints
- Write detailed setup documentation for .env configuration
- Document rate limiting behavior

**Vishil Patel:**
- Add approved flag logic to posts API
- Create moderation endpoints for approve/reject actions
- Optimize database queries for profile page
- Add indexes for new query patterns
