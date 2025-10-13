# Sprint Meeting Notes

**Attended**: Alex Eskenazi, Vaughn Stout, Vishil Patel

**DATE**: 10/13/2025

***

## Sprint 5 Review

### SRS Sections Updated

User Interface Requirements, Authentication Requirements, Security Requirements

### User Story

Epic: User Accounts - Making an Account, Logging In, Different User Types
Frontend pages for user registration and login interface

### Sprint Requirements Attempted

User authentication system including signup, login, and session management
Frontend development for authentication pages
Password hashing and email uniqueness validation

### Completed Requirements

Successfully implemented backend authentication routes with password hashing and session management. Created frontend signup and login pages with proper form validation. Integrated database with user account storage and authentication checks. Session handling and protected routes are working properly.

### Incomplete Requirements

None - all authentication requirements were completed successfully in this sprint.

### The summary of the entire project

We are creating a web app where students can share and find internship opportunities. Users can post internships with details like the company, description, and tags, and others can comment or upvote them. The goal is to make it easier for students to discover real, useful internships all in one place. We're building with React frontend, FastAPI backend, and SQLite database.

***

## Sprint 6 Planning

## Requirements Flex

3/5 requirement flexes remaining

## Technical Debt

None from previous sprint - authentication system was completed successfully.

### Requirement Target

Frontend internship posting functionality
Backend API endpoints for creating and managing internship posts
Integration of posting system with authentication

### User Stories

Epic: Internship Posting
- As a student, I want to post internship opportunities so that I can share valuable opportunities with other students
- As a student, I want to add details like company name, description, and tags to my internship posts so that others can easily understand the opportunity
- As a student, I want to edit or delete my own posts so that I can keep information accurate and up-to-date

### Planning

Create frontend forms for internship posting with fields for title, company, description, tags, and link. Build backend API routes for post creation, editing, and deletion. Implement proper validation and error handling. Connect posting system to authentication so only logged-in users can post.

### Action Items

- Build frontend posting form with validation
- Create backend API endpoints for post CRUD operations
- Implement proper authorization checks for post management
- Add database schema updates for post storage
- Test posting functionality end-to-end

### Issues and Risks

- Form validation complexity may cause delays
- Integration between frontend and backend posting may require debugging
- Database schema changes could affect existing authentication system

### Team Work Assignments

Alex: Frontend posting forms, UI design for post creation and editing pages
Vaughn: Backend API routes for posts, database schema updates, documentation
Vishil: Testing posting functionality, validation logic, integration testing
