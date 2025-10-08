# Sprint Meeting Notes

*note: replace anything surrounded by << >> and **remove** the << >>*

**Attended**: Alex Eskenazi, Vaughn Stout, Vishil Patel

**DATE**: 10/6/2025

***

## Sprint Review

### SRS Sections Updated

Introduction, Functional Requirements, Non-Functional Requirements

### User Story

N/A

### Sprint Requirements Attempted

Database setup and schema creation
Basic data storage and retrieval

### Completed Requirements

Set up a working database with sample internship data and a schema for storing posts and user accounts. Verified that the database can handle adding and reading test data.

### Incomplete Requirements

N/A

### The summary of the entire project

We are creating a web app where students can share and find internship opportunities. Users can post internships with details like the company, description, and tags, and others can comment or upvote them.

The goal is to make it easier for students to discover real, useful internships all in one place. We’re starting with basic features like login, posting, commenting, and voting, and will keep improving it as we go.

***

## Sprint Planning

## Requirements Flex

<< # >>/3 requirement flexes remaining

## Technical Debt

User authentication system including signup, login, and session management

### Requirement Target

User authentication with signup login and logout
Password hashing and email uniqueness checks
Session management and auth guard for protected pages

### User Stories

## Epic: User Accounts
What we want to do: Let people make accounts and log in, different types of users

User Stories:

•⁠  ⁠Making an Account 
  - As a student looking for internships, I want to sign up with my email and password so that I can save internships I like and post my own
•⁠  ⁠Logging In  
  - As a student who already has an account, I want to log back into my account so that I can see my saved stuff and post internships
•⁠  ⁠Different User Types
  - As an admin person, I want to give users different permissions so that we can have moderators and stuff


### Planning

Create backend routes for signup login and logout
Validate input and return clear errors
Hash passwords and enforce unique email

### Action Items

Build signup and login routes with validation and hashing
Add session handling and a protected test route

### Issues and Risks

Password security and session bugs may appear

### Team Work Assignments


Alex frontend pages for signup login and posting plus documentation\
Vaughn backend auth routes hashing and session logic\
Vishil database integration query checks and testing
