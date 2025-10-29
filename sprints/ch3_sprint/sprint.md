# **Project Overview**

## **Application Vision/Goal:**

We want to build a website where students can share and find internships. Right now, a lot of info gets spread out across emails, Discord, LinkedIn, or random group chats, and its all over the place and hard to manage, but by creating a Internship Hub, everything’s in one place and easier to find allowing students to share opportunities and tips to help each other out.
## **Scope:**

Students can post internships with a link, title, description, and tags (like “Software Engineering,” “NYC,” or “Fall 2025”).

Users can comment under a post to add info like deadlines, interview tips, or personal experiences they may have.

A voting system lets people upvote the most helpful opportunities to spread important and trending opportunities or chats.

Search and filters help find posts by company, role, or tags.

Users can report broken links or expired posts so the board stays clean.
## **Deliverables:**

A working MVP web app.

Core features:

Posting internships with title, description, tags, and link.

Commenting on posts.

Voting system so the most useful internships rise to the top.

Search and filter functionality (by keyword, company, and tags).

Reporting feature for not working/expired opportunities.

A simple login/authentication system for posting and voting.

A SQLite database storing posts, comments, votes, and reports.

Documentation, including: How to run the app locally, Project design and architecture overview, & User guide for main features.

Testing:

Unit tests for backend routes (posts, votes, reports).

Manual testing of the UI.

## **Success Criteria:**

People can actually use it to post and browse internships.

Voting changes the order of posts (popular ones show up first).

Search and filters actually narrow things down.

Reported posts get flagged for review.

The app runs on both laptop and phone browsers without looking broken.

## **Assumptions:**
Everyone using the site is a student who just wants to share or find internships.

For MVP, we’ll keep authentication simple (school email or just a basic login).

SQLite is fine as a starter database, but we could switch to PostgreSQL if needed.

We’ll all stay on top of GitHub so our code doesn’t get messy.

## **Risks:**

Setting up login/auth might take longer than we expect.

People might try to add too many features and go off-scope.

If we don’t keep communication consistent, merge conflicts could waste time.

Testing might get rushed if we save it until the very e


## **Design / Architectural Review:**

Design / Architecture:

Frontend: React + TailwindCSS (clean, mobile-friendly).

Backend: Python Flask.

Database: SQLite (file-based, easy to set up).

Main Parts:

Post system (create, edit, delete internships).

Comments (linked to each post).

Votes (up/down, affects ranking).

Search + filter by tags.

Reporting feature.

Flow: Browser → API (Flask) → Database → API response → UI update.
## **Test Environment:**
Local testing on our laptops.

Unit tests (pytest) for backend endpoints.

Manual frontend testing for posting, voting, and search.

A set of fake posts in the database so we can test filters and rankings.

# **Team Setup**

## **Team Members:**
### Alex Eskenazi, Vaughn Stout, Vishil Patel

## **Team Roles:**
### Alex Eskenazi - Frontend Dev, UI Design
### Vaughn Stout - Backend Dev (DB + API), Documentation, Team Lead
### Vishil Patel - Backend Dev (API + Auth), QA Tester

## **Team Norms:**
Team will communicate through text, and will have weekly meetings on Fridays from 3:00PM-4:00PM. Will regularly check up with each other on sprint progress or after any commits are made.

## **Application Stack:**
Frontend will use React library, probably with CSS for UI.
Backend API will use Python with Flask framework.
Backend DB will use SQLite.


### **Libraries/Frameworks:**
React, Flask.
