# User Stories - Internship Hub

## Epic Overview

We're organizing our user stories into bigger chunks called "epics" to make it easier to plan what we're building. Here's what we came up with:

**Epic 1: Account Stuff** (US-001 to US-003)
- Basic login/signup functionality
- Different user types (student, mod, admin)

**Epic 2: Posting Internships** (US-004 to US-007)  
- Creating and managing internship posts
- Viewing all the posts

**Epic 3: Voting** (US-008 to US-009)
- Upvote/downvote system
- Sorting posts by votes

**Epic 4: Comments** (US-010 to US-013)
- Commenting on posts
- Managing your own comments

**Epic 5: Search** (US-014 to US-016)
- Finding specific internships
- Filtering by tags

**Epic 6: Moderation** (US-017 to US-020)
- Approving posts
- Handling reports and user management

**Epic 7: Technical Stuff** (US-021 to US-022)
- Mobile support and performance

---

## Epic 1: User Account Stuff

### US-001: Making an Account
**As a** student looking for internships  
**I want to** sign up with my email and password  
**So that** I can save internships I like and post my own

**Acceptance Criteria:**
- Students can make accounts with username, email, password
- Can't have duplicate emails (duh)
- Gets a confirmation when they sign up
- New accounts are just "basic" users

### US-002: Logging In
**As a** student who already has an account  
**I want to** log back into my account  
**So that** I can see my saved stuff and post internships

**Acceptance Criteria:**
- Login with email/username + password
- Shows error message if wrong password
- Takes you to the main page when you login successfully
- Need to validate the login info

### US-003: Different User Types
**As a** admin person  
**I want to** give users different permissions  
**So that** we can have moderators and stuff

**Acceptance Criteria:**
- Different roles: guest, regular, moderator, admin
- Moderators can approve posts
- Admins can do everything
- Regular users can just post and vote

## Epic 2: Posting Internships

### US-004: Create Internship Post
**As a** student with an internship to share  
**I want to** make a post about it  
**So that** other students can see it and apply

**Acceptance Criteria:**
- Can make posts with title, description, company link, tags
- Title, description, and link are required
- Tags are optional but helpful
- Posts need to be approved by mods first
- Shows who posted it

### US-005: Edit My Posts
**As a** student who posted something  
**I want to** be able to edit it later  
**So that** I can fix typos or update info

**Acceptance Criteria:**
- Only edit your own posts
- Can change title, description, link, tags
- Keeps track of when it was edited
- Still needs to stay approved after editing (maybe?)

### US-006: Delete My Posts
**As a** student who posted  
**I want to** delete my post  
**So that** I can remove it if the internship is filled or expired

**Acceptance Criteria:**
- Only delete your own posts
- Deletes everything (comments, votes, etc.)
- Ask "are you sure?" before deleting
- Can't get it back once deleted

### US-007: Browse All Posts
**As a** student looking for internships  
**I want to** see a list of all the internships  
**So that** I can find ones I want to apply to

**Acceptance Criteria:**
- Shows all approved posts in a list
- Can scroll through them
- Shows title, description, company, tags, votes
- Works on phone and computer

## Epic 3: Voting on Posts

### US-008: Upvote/Downvote Posts
**As a** student browsing internships  
**I want to** upvote good posts and downvote bad ones  
**So that** the best internships show up first

**Acceptance Criteria:**
- Logged in users can upvote or downvote posts
- Can only vote once per post
- Can change your vote (from up to down or whatever)
- Score = upvotes - downvotes

### US-009: Sort by Votes
**As a** student looking at posts  
**I want to** see the highest rated ones first  
**So that** I don't waste time on crappy internships

**Acceptance Criteria:**
- Posts sorted by vote score (highest first)
- Updates in real time when people vote
- If votes are tied, show newer posts first

## Epic 4: Comments

### US-010: Comment on Posts
**As a** student  
**I want to** comment on internship posts  
**So that** I can ask questions or share tips

**Acceptance Criteria:**
- Can comment on approved posts
- Comments show up right away
- Shows who commented and when
- Need to be logged in to comment

### US-011: Read Comments
**As a** student  
**I want to** read what other people said about internships  
**So that** I can get more info before applying

**Acceptance Criteria:**
- Comments show under each post
- Shows username and time posted
- Comments in order (oldest first)
- Easy to tell comments apart from the main post

### US-012: Edit My Comments
**As a** student who commented  
**I want to** edit my comment  
**So that** I can fix typos

**Acceptance Criteria:**
- Can only edit your own comments
- Shows that it was edited (maybe)
- Keeps the original timestamp

### US-013: Delete My Comments
**As a** student who commented  
**I want to** delete my comment  
**So that** I can remove it if I said something dumb

**Acceptance Criteria:**
- Can only delete your own comments
- Gone forever once deleted
- Maybe ask "are you sure?"

## Epic 5: Finding Stuff

### US-014: Search Posts
**As a** student  
**I want to** search for specific internships  
**So that** I can find ones at companies I like

**Acceptance Criteria:**
- Search box that looks through titles and descriptions
- Doesn't care about caps or lowercase
- Shows results fast
- If you don't type anything, shows everything

### US-015: Filter by Tags
**As a** student  
**I want to** filter by tags like "Remote" or "CS"  
**So that** I can find internships I actually want

**Acceptance Criteria:**
- Click on tags to filter
- Can pick multiple tags
- Can search + filter at same time
- Updates right away when you click

### US-016: Multiple Filters
**As a** student  
**I want to** use search + tags together  
**So that** I can be really specific about what I want

**Acceptance Criteria:**
- Search + tags work together
- Easy to use interface
- Still fast when using lots of filters

## Epic 6: Moderator Stuff

### US-017: Approve Posts
**As a** moderator  
**I want to** check posts before they go live  
**So that** we don't get spam or inappropriate content

**Acceptance Criteria:**
- Mods can see posts waiting for approval
- Can approve or reject with a reason
- Approved posts show up for everyone
- Keep track of who approved what

### US-018: Report Bad Posts
**As a** student  
**I want to** report posts that suck or are fake  
**So that** mods can remove them

**Acceptance Criteria:**
- "Report" button on posts
- Need to give a reason
- Can only report each post once
- Post stays visible until mods decide

### US-019: Handle Reports
**As a** moderator  
**I want to** see reported posts and deal with them  
**So that** the site stays clean

**Acceptance Criteria:**
- List of all reported posts
- Shows who reported and why
- Can mark as "resolved"
- Keep track of mod actions

### US-020: Manage Users (Admin)
**As an** admin  
**I want to** manage user accounts  
**So that** I can ban trolls and promote good users to mods

**Acceptance Criteria:**
- See all user accounts
- Change user roles (make someone a mod, etc.)
- Ban/suspend users
- Log what admins do

## Epic 7: Other Important Stuff

### US-021: Works on Phone
**As a** student using my phone  
**I want to** use the site on mobile  
**So that** I can check internships when I'm not at my computer

**Acceptance Criteria:**
- Everything works on phone
- Buttons aren't too small to tap
- Text is readable
- Voting and commenting work with touch

### US-022: Fast Site
**As a** student  
**I want to** have the site load quickly  
**So that** I don't get frustrated and leave

**Acceptance Criteria:**
- Pages load fast
- Search results show up quickly
- Voting/commenting happens right away
- Works even with lots of posts

