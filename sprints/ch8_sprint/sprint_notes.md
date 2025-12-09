# Sprint Meeting Notes

**Attended**: Alex Eskenazi, Vaughn Stout, Vishil Patel

**DATE**: November 3, 2025

***

## Sprint 7 Review

### SRS Sections Updated

User Interface section with all screen documentation and screenshots
User Stories section added with 6 epics covering all major features
Testing section verified and confirmed to be current

### User Stories

Epic 1: Account Management and Authentication
- As a student, I want to create an account with a username and password so that I can start posting and interacting with internship opportunities
- As a returning user, I want to log in with my credentials so that I can access my account and previous posts

Epic 2: Internship Posting and Management
- As a student, I want to post internship opportunities with all the details so that I can share valuable opportunities with other students
- As a user, I want to edit my own posts so that I can fix typos or update information that changed

Epic 6: User Experience and Accessibility
- As a student on my phone, I want the app to work well on mobile so that I can browse internships anywhere
- As a new user, I want the interface to be easy to understand so that I can start using the app without confusion

### Sprint Requirements Attempted

Complete user interface documentation with screenshots
Mobile responsiveness testing and fixes
Interface consistency review
User stories documentation in SRS
Requirements and user stories check to make sure they are aligned

### Completed Requirements

Finished documenting all seven main screens (Home, Sign Up, Login, Post Creation, Post Details, User Profile, Admin Panel) with screenshots and descriptions. Added User Stories section to SRS with 6 epics and 20+ stories that connect to our requirements. Tested on mobile and desktop - responsive design works pretty well. Fixed some UI stuff that didn't look right.

### Incomplete Requirements

Mobile UI could still use some polish in a few spots. The admin panel is a bit cramped on small screens. Search filters don't look great on phones under 375px width.

***

## Sprint 8 Planning - Application Reliability

## Requirements Flex

3/3 requirement flexes remaining

## Technical Debt

Some mobile UI issues on very small screens (under 375px)
Admin panel layout needs optimization for mobile
Error handling could be more specific in some API endpoints

### Requirement Target

Make the app more reliable and fix bugs
Better error handling
Review code for issues
Finalize testing docs

### User Stories

From Epic 6: User Experience and Accessibility
- As any user, I want pages to load quickly so that I don't waste time waiting
- As a new user, I want the interface to be easy to understand so that I can start using the app without confusion

From Epic 5: Content Moderation and Administration
- As an admin, I want to see all reported posts in one place so that I can efficiently moderate content

### Planning

Focus on making the app more reliable and fixing bugs. Review all the code for potential issues. Make sure error messages are helpful. Test edge cases like what happens if someone tries to post without logging in or votes on a deleted post. Document any bugs we find and prioritize fixes. Update testing section if needed.

### Action Items

- Review backend error handling and add better error messages
- Test edge cases and document bugs found
- Fix known mobile UI issues on small screens
- Review security - make sure users can't do stuff they shouldn't
- Make sure all user stories in SRS are actually implemented

### Issues and Risks

- Some edge cases might break the app
- Error messages might not be clear enough for users
- Mobile UI issues could affect user experience

### Team Work Assignments

Alex: Frontend error handling, mobile UI fixes, test user flows
Vaughn: Code review, documentation updates, requirements verification
Vishil: Backend error handling, database query optimization, security review
