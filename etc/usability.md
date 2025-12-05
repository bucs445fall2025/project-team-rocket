# Usability Review - Internship Hub

**Team Members:** Alex Eskenazi, Vaughn Stout, Vishil Patel  
**Date:** October 20, 2025

## Overview

We read the "Usability 101" article like the assignment asked, and then looked at our planned GUI for the Internship Hub to see how well it follows the usability stuff. Here's what we found and some ideas for making it better.

## Current Planned GUI Design

Our Internship Hub application will feature:

- **Login/Registration Page** - Simple forms for user authentication
- **Main Dashboard** - Central hub showing recent internship posts with search functionality
- **Internship Posting Form** - Multi-step form for students to share opportunities
- **Internship Details Page** - Detailed view of each internship with comments and voting
- **User Profile Page** - Personal dashboard showing saved posts and user activity
- **Search/Filter Interface** - Advanced filtering by company, location, tags, and dates

## Usability Quality Attributes Analysis

### 1. Learnability
*How easy is it for users to accomplish basic tasks the first time they encounter the design?*

**Current UI Elements Supporting Learnability:**
- **Clear Navigation Menu** - Simple top navigation with obvious labels like "Dashboard", "Post Internship", "My Profile"
- **Familiar Posting Interface** - Similar to social media posting, which students already know
- **Standard Form Layouts** - Login and registration forms follow conventional patterns
- **Visual Hierarchy** - Important actions (like "Post Internship") will be prominently displayed with contrasting colors
- **Search Bar Placement** - Positioned at the top of the dashboard where users expect it

**What Works Well:**
Students should be able to figure out how to search and post pretty easily since it's like other websites they already use (Instagram, LinkedIn, etc.).

### 2. Efficiency
*Once users have learned the design, how quickly can they perform tasks?*

**Current UI Elements Supporting Efficiency:**
- **Quick Actions Dashboard** - One-click access to "Post New Internship" from the main page
- **Save/Bookmark Feature** - Users can quickly save interesting internships for later
- **Tag-Based Filtering** - Click on tags to instantly filter similar internships
- **Recent Activity Section** - Shows users their recent posts and saved items
- **Auto-Complete Search** - Search suggestions appear as users type

**What Works Well:**
Once people know how to use it, they can browse through new posts and find what they want really fast without clicking around a bunch.

### 3. Memorability
*When users return to the design after a period of not using it, how easily can they reestablish proficiency?*

**Current UI Elements Supporting Memorability:**
- **Consistent Color Scheme** - Same colors for actions throughout the app (e.g., blue for "save", green for "post")
- **Persistent Navigation** - Navigation menu stays in the same location on every page
- **Icon Usage** - Standard icons for common actions (heart for save, comment bubble for discussions)
- **Breadcrumb Navigation** - Users can see where they are in the app and easily go back
- **Status Indicators** - Clear visual feedback when posts are saved or actions are completed

**What Works Well:**
When students come back after winter break or whatever, they should remember how to use it because everything looks the same and works like other websites.

## Proposed UI Improvements for Better Usability

Based on our analysis, we identified several areas where we can improve usability:

### 1. Enhanced Learnability Improvements

**Problem:** New users might not understand the difference between "posting an internship" vs "applying to internships"

**Solution:** 
- Add a brief explanation on the dashboard: "Share internships you find with other students" 
- Include tooltip help text on the posting form
- Create a simple onboarding tour for first-time users

**Why this helps:** The article said new users need to be able to do stuff right away. If we explain things better, people won't get confused about what the site is for.

### 2. Enhanced Efficiency Improvements  

**Problem:** Users have to scroll through many posts to find relevant internships

**Solution:**
- Implement "Smart Filters" that remember user preferences (preferred locations, companies, roles)
- Add a "Recently Viewed" section so users can quickly return to internships they looked at before
- Include bulk actions like "Save All" for multiple internships at once

**Reasoning:** The article mentioned that efficiency improves when the interface adapts to user behavior. Remembering preferences reduces repetitive filtering tasks.

### 3. Enhanced Memorability Improvements

**Problem:** Users might forget how to access advanced features after time away

**Solution:**
- Add contextual help icons (?) next to complex features
- Use consistent button placement across all pages
- Implement a "Quick Start" guide accessible from the user profile
- Ensure all important actions have both text labels AND recognizable icons

**Reasoning:** Nielsen's article stressed that good usability means users don't have to relearn the interface. Visual consistency and accessible help will support returning users.

## Additional Usability Considerations

### Error Prevention
- Add confirmation dialogs before deleting posts
- Validate form data in real-time with helpful error messages
- Provide clear feedback when actions succeed or fail

### User Control
- Allow users to edit their posts after publishing
- Provide an "undo" option for recently deleted items  
- Let users customize their dashboard layout

### Mobile Responsiveness
- Ensure all functionality works well on phones since many students primarily use mobile devices
- Use touch-friendly button sizes
- Optimize text size for mobile reading

## Conclusion

By focusing on these three key usability attributes - learnability, efficiency, and memorability - we can create an Internship Hub that truly serves student needs. The planned improvements will make the platform more intuitive for new users while maintaining speed and convenience for regular users.

Our next steps are to implement these design decisions as we build the frontend interface, keeping usability testing in mind throughout the development process.