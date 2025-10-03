# Database Schema Overview

This document describes the main tables and relationships in the current database schema for the project.

## Users
- **id** (Primary Key)
- **username** (Unique)
- **email** (Unique)
- **password_hash** so we do not need to store the actual passwords

## Posts
- **id** (Primary Key)
- **user_id** (Foreign Key -> Users.id)
- **title**
- **content**
- **timestamp**

## Comments
- **id** (Primary Key)
- **post_id** (Foreign Key -> Posts.id)
- **user_id** (Foreign Key -> Users.id)
- **content**
- **timestamp**

## Votes
- **id** (Primary Key)
- **user_id** (Foreign Key -> Users.id)
- **post_id** (Foreign Key -> Posts.id)
- **value** (int, e.g. 1 for upvote, -1 for downvote)

## Reports
- **id** (Primary Key)
- **user_id** (Foreign Key -> Users.id)
- **post_id** (Foreign Key -> Posts.id, nullable)
- **comment_id** (Foreign Key -> Comments.id, nullable)
- **reason**
- **timestamp**

### Notes
- Each user can create posts, comments, votes, and reports.
- Posts and comments are linked to users.
- Votes are used for upvoting/downvoting posts.
- Reports can be for either a post or a comment.
