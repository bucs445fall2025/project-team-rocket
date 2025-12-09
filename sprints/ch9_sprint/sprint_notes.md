# Sprint Meeting Notes

**Attended**: Alex Eskenazi, Vaughn Stout, Vishil Patel

**DATE**: November 10, 2025

***

## Sprint 9 Review

### SRS Sections Updated

- Added Project Status section (v1.5)
- Documented known bugs with severity ratings
- Listed featues we have not yet implemented.

### User Story

**User Story 1.1: User Registration**
- As a student, I want to create an account with a username and password so that I can start posting and interacting with internship opportunities

**User Story 1.2: User Login**
- As a returning user, I want to log in with my credentials so that I can access my account and previous posts

**User Story 2.1: Create Internship Post**
- As a student, I want to post internship opportunities with all the details so that I can share valuable opportunities with other students

### Sprint Requirements Attempted

• Students can sign up and log in to their accounts

• Secure login system with password protection and session management

• Users can create posts with a title, description, company link, and tags

• All internships show up in a clean, scrollable list with sorting options

• Users can upvote or downvote internship posts (no double voting)

• Posts with higher ratings appear first in the feed

### Completed Requirements
• Implemented signup and login with secure password hashing and session management

• Finished post creation with required fields (title, description, company, link, tags)

• Built the home feed showing all posts in a scrollable list

• Implemented voting with double-vote prevention

• Feed sorted so higher-rated posts appear first

### Incomplete Requirements

• Users can edit or delete their own posts anytime - The delete works fine, but there's no edit button on the frontend yet. The backend code is ready but we never made the UI for it.

• Users can see who commented and when, with ability to edit/delete their own comments - Same issue - can delete comments but can't edit them from the website.

• Moderators can approve posts before they go public - This isn't implemented at all. Posts just go live immediately when you create them.

• Focused on security and reliability with proper data validation - Found some security issues that need fixing:
  - The secret key is hardcoded in the code which is bad
  - Password requirements are too weak (only 6 characters)

### The summary of the entire project

Internship Hub is a web app where college students can share and find internship opportunities. It's like Reddit but specifically for internships. Users can post opportunities with details like company name, description, and application link. Other students can upvote good posts, downvote bad ones, and leave comments asking questions or sharing their experiences. There's also an admin system for moderating content and handling reports. The backend is built with Flask and SQLAlchemy, and the frontend uses React with TypeScript. Right now the core features work but we have some bugs to fix and missing features to add.

***

## Sprint 10 Planning

## Requirements Flex

3/5 requirement flexes remaining

## Technical Debt

• Need to fix the hardcoded secret key security issue
• Need to add edit functionality for posts and comments on the frontend
• Should implement rate limiting to prevent brute force attacks

### Requirement Target

• Focused on security and reliability with proper data validation

• Users can edit or delete their own posts anytime

• Users can see who commented and when, with ability to edit/delete their own comments

### User Stories

**User Story 2.2: Edit Own Posts**
- As a user, I want to edit my own posts so that I can fix typos or update information that changed

**User Story 3.3: Edit/Delete Own Comments**
- As a commenter, I want to edit or delete my comments so that I can correct mistakes or remove comments I no longer want visible

### Planning

1. First priority is fixing the critical security bugs - move secret key to environment variable, strengthen password requirements, add rate limiting

2. Add edit functionality for posts - create an edit button on PostCard component, build an edit form similar to the create post form, wire it up to the existing backend API

3. Add edit functionality for comments - similar approach, add edit button next to delete button, create inline edit form

### Action Items

- Alex: Build the edit post and edit comment UI components
- Vaughn: Fix the security issues (secret key, password validation), write documentation for the fixes
- Vishil: Add database indexes, optimize the queries that are running multiple times

### Issues and Risks

• Moving the secret key to an environment variable means everyone on the team needs to update their local setup - need to document this clearly

• Only have about a week and a half until the next sprint meeting, and we all have other classes and assignments

### Team Work Assignments

**Alex Eskenazi:**
- Create edit post modal/form component
- Add edit button to PostCard component
- Create edit comment inline form
- Test all the new UI features

**Vaughn Stout:**
- Move SECRET_KEY to environment variable
- Update password validation to require 8+ chars with complexity rules
- Document environment variable setup for the team

**Vishil Patel:**
- Add database indexes on Post.status, Post.vote_score, Post.author_id
- Optimize post loading queries to prevent N+1 issues
- Test database performance improvements
