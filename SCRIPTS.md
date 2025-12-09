# Available Scripts

This document provides a quick reference for all helper scripts in the project.

## Running the Application

### `./run-backend.sh`

Starts the Flask backend server.

**What it does:**

* Creates/activates Python virtual environment
* Installs backend dependencies from `backend/requirements.txt`
* Checks MySQL database connection
* Starts Flask server on port 5001

**Usage:**

```bash
./run-backend.sh
```

### `./run-frontend.sh`

Starts the React frontend development server.

**What it does:**

* Checks for and installs Node.js dependencies if needed
* Starts React development server on port 3000
* Opens browser automatically

**Usage:**

```bash
./run-frontend.sh
```

## Database Population Scripts

### `python3 add_sample_data.py` ⭐ Recommended

Adds comprehensive sample data for testing and demonstration.

**What it adds:**

* **9 test user accounts:**
  * 8 regular users: alice_smith, bob_jones, carol_wilson, david_lee, emma_chen, frank_garcia, grace_kim, henry_patel
  * 1 moderator: moderator_jane
  * All using @binghamton.edu email addresses
* **12 sample internship posts** from companies like Google, Microsoft, Meta, Netflix, Apple, OpenAI, etc.
* **20-40 realistic comments** spread across the posts
* **Voting activity** to create realistic vote scores and rankings

**Default passwords:**

* Regular users: `password123`
* Moderator: `mod123`

**Usage:**

```bash
python3 add_sample_data.py
```

**When to use:**

* When you want a fully populated database for testing
* For demos and presentations
* To test features like comments, voting, user interactions

### `python3 add_sample_internships.py`

Adds only internship posts without test users.

**What it adds:**

* **10 sample internship posts** from major tech companies
* All posts created by the admin user
* No additional users, comments, or votes

**Usage:**

```bash
python3 add_sample_internships.py
```

**When to use:**

* When you already have users and just need posts
* When you want to manually test posting/commenting
* For minimal sample data

## Database Initialization Scripts

### `python3 backend/init_db.py`

Full database reset and initialization (use with caution).

**What it does:**

* **Drops all existing tables** (deletes all data!)
* Creates fresh database schema
* Adds sample users and posts
* Creates admin, moderator, and basic users

**Usage:**

```bash
python3 backend/init_db.py
```

**⚠️ Warning:** This will delete all existing data in the database!

**When to use:**

* When you need to completely reset the database
* During initial development setup
* When the database schema changes

### `python3 backend/add_indexes.py`

Optimizes database performance by adding indexes.

**What it does:**

* Adds database indexes on frequently queried columns
* Improves query performance for posts, votes, and users
* Safe to run multiple times (uses `IF NOT EXISTS`)

**Usage:**

```bash
python3 backend/add_indexes.py
```

**When to use:**

* After initial database setup
* When app performance is slow
* When working with large amounts of data

## Quick Start Workflow

For a fresh setup with sample data:

```bash
# 1. Start the backend (creates admin user)
./run-backend.sh

# 2. In a new terminal, add comprehensive sample data
python3 add_sample_data.py

# 3. In another terminal, start the frontend
./run-frontend.sh
```

Now you have:

* ✅ Backend running on <http://localhost:5001>
* ✅ Frontend running on <http://localhost:3000>
* ✅ Database populated with users, posts, comments, and votes
* ✅ Ready to test all features!

## Test Accounts

After running `add_sample_data.py`, you can log in with:

| Username | Email | Password | Role |
|----|----|----|----|
| admin | admin@internshiphub.com | admin123 | admin |
| moderator_jane | jane.moderator@binghamton.edu | mod123 | moderator |
| alice_smith | alice.smith@binghamton.edu | password123 | user |
| bob_jones | bob.jones@binghamton.edu | password123 | user |
| carol_wilson | carol.wilson@binghamton.edu | password123 | user |
| david_lee | david.lee@binghamton.edu | password123 | user |
| emma_chen | emma.chen@binghamton.edu | password123 | user |
| frank_garcia | frank.garcia@binghamton.edu | password123 | user |
| grace_kim | grace.kim@binghamton.edu | password123 | user |
| henry_patel | henry.patel@binghamton.edu | password123 | user |

## Troubleshooting

**Script won't run:**

```bash
chmod +x run-backend.sh run-frontend.sh add_sample_data.py add_sample_internships.py
```

**Database connection errors:**

* Make sure MySQL Docker container is running: `docker ps | grep mysql`
* Restart container if needed: `docker start ihub-mysql-1`

**"Admin user not found" error:**

* Run the backend first: `./run-backend.sh`
* This creates the admin user automatically
* Then run the sample data scripts


