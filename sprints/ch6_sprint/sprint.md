# Sprint Meeting Notes

**Attended**: Alex Eskenazi, Vaughn Stout, Vishil Patel

**DATE**: October 18, 2025

***

## Sprint 5 Review

### SRS Sections Updated

Team Roles, Requirements Section, Testing Section

### User Story

As a development team, we want clearly defined roles and responsibilities so that we can work efficiently and ensure all aspects of the project are properly covered.

As a software engineer, I want comprehensive test coverage so that we can catch bugs early and maintain code quality throughout development.

### Sprint Requirements Attempted

Team role assignment, requirements expansion, and testing framework design

### Completed Requirements

We assigned team roles with Alex as Front-End Lead, Vaughn as Software Lead, and Vishil as Back-End Lead. Each person has clear responsibilities for their area. We expanded our requirements section to have 16 functional requirements (FR1-FR16) and 4 non-functional requirements (NFR1-NFR4) covering all the features we want to build. We also created a comprehensive testing plan that covers all our backend models (User, Post, Comment, Vote, Report) and API endpoints with specific test descriptions following the required format.

### Incomplete Requirements

We haven't started implementing the actual frontend UI components yet - still in the planning and design phase. The backend API endpoints for frontend integration also need to be built.

### The summary of the entire project

We're building an Internship Hub web application where students can share and discover internship opportunities. Users can post internships they find, comment on posts, and upvote helpful opportunities. Our goal is to centralize internship sharing instead of having information scattered across Discord, emails, and group chats. We have a solid Flask backend with SQLAlchemy models and now we're focusing on creating a user-friendly frontend interface.

***

## Sprint 6 Planning

## Requirements Flex

3/5 requirement flexes remaining

## Technical Debt

Frontend development - we need to start building the actual React components and connect them to our existing Flask backend

### Requirement Target

Begin frontend implementation with focus on usability principles identified in our analysis. Create the basic React application structure and implement core UI components.

### User Stories

As a student visitor, I want to see a clean, intuitive homepage so that I understand what the platform is for and how to get started.

As a new user, I want the registration and login process to be straightforward so that I can quickly create an account and start using the platform.

As a student posting internships, I want the posting form to be easy to fill out with helpful guidance so that I can share opportunities without frustration.

### Planning

Start building the React frontend application using the usability principles we identified. Focus on the three main areas: learnability (clear navigation and familiar patterns), efficiency (quick actions and smart defaults), and memorability (consistent design and helpful icons). We'll implement the basic pages first: homepage, login/registration, dashboard, and posting form.

### Action Items

Set up React development environment with proper project structure
Create basic component library with consistent styling
Implement authentication pages (login/registration) with good form validation
Build main dashboard layout with navigation
Start internship posting form with step-by-step guidance
Connect frontend to existing Flask backend API

### Issues and Risks

We're still pretty new to React so we'll probably have to figure out a lot of stuff as we go. Getting the React frontend to talk to our Flask backend might be tricky - we'll have to deal with CORS and making sure the API calls work right. Also we need to actually test our usability ideas to make sure they're not just good on paper.

### Team Work Assignments

Alex: React app setup, component design system, and main dashboard layout
Vaughn: Backend API endpoints for frontend integration, authentication flow
Vishil: Form components, validation logic, and testing the user experience flows
