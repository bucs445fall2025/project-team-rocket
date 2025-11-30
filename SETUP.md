# Internship Hub - Setup Guide

This guide will help you get the app running on your local machine.

## Prerequisites

You need to have these installed first:

* Python 3.10+
* Node.js 16+ and npm
* Docker Desktop

## Step 1: Clone the Repository

```bash
git clone <repository-url>
cd project-team-rocket
```

## Step 2: Set Up the Database

We're using MySQL in a Docker container because it's easier than installing MySQL directly.

```bash
# Start the MySQL container
docker run -d \
  --name ihub-mysql-1 \
  -e MYSQL_ROOT_PASSWORD=rootpassword \
  -e MYSQL_DATABASE=internship_hub \
  -e MYSQL_USER=ihub_user \
  -e MYSQL_PASSWORD=ihub_password \
  -p 3306:3306 \
  mysql:8.0
```

Wait like 30 seconds for MySQL to fully start up. You can check if it's ready:

```bash
docker ps
```

Look for the container named `ihub-mysql-1` - it should say "healthy" or "Up".

## Step 3: Set Up the Backend

```bash
# Create a Python virtual environment
python3 -m venv venv

# Activate it (you'll need to do this every time you open a new terminal)
source venv/bin/activate

# Install Python dependencies
pip install -r backend/requirements.txt

# Run the Flask app
python app.py
```

The backend should start on http://localhost:5001

When it starts for the first time, it will automatically:

* Create all the database tables
* Create an admin account (username: `admin`, password: `admin123`)

Keep this terminal window open!

## Step 4: Set Up the Frontend

Open a **new terminal window** and run:

```bash
cd project-team-rocket/frontend

# Install npm packages (this takes a few minutes)
npm install

# Start the React development server
npm start
```

The frontend should open automatically in your browser at http://localhost:3000

If it doesn't open automatically, just go to http://localhost:3000 in your browser.

## Quick Summary

Once everything is set up, here's how to start the app:

**Terminal 1 (Backend):**

```bash
source venv/bin/activate
python app.py
```

**Terminal 2 (Frontend):**

```bash
cd frontend
npm start
```

## Common Issues

### Port 5001 already in use

If you're on a Mac, AirPlay uses port 5000/5001. Either:

* Turn off AirPlay Receiver in System Preferences
* Or change the port in `app.py` (last line)

### Port 3000 already in use

Something else is using port 3000. Kill it:

```bash
lsof -ti:3000 | xargs kill -9
```

### MySQL container won't start

Maybe you already have MySQL running locally. Check:

```bash
docker ps -a
```

If you see `ihub-mysql-1` but it's stopped, just start it:

```bash
docker start ihub-mysql-1
```

### Can't connect to database

Make sure the MySQL container is actually running:

```bash
docker ps | grep mysql
```

If it's not there, go back to Step 2.

### Frontend can't reach backend

Make sure both servers are running. The frontend expects the backend at http://localhost:5001

## Stopping Everything

**Stop the servers:**

* Press `Ctrl+C` in both terminal windows

**Stop the MySQL container:**

```bash
docker stop ihub-mysql-1
```

**Start it again later:**

```bash
docker start ihub-mysql-1
```

## Default Admin Account

Username: `admin`
Password: `admin123`

You can use this to access the admin panel at http://localhost:3000/admin

## Database Management

**Reset the database:**

```bash
docker stop ihub-mysql-1
docker rm ihub-mysql-1
# Then run the docker run command from Step 2 again
```

**View database contents:**

```bash
docker exec -it ihub-mysql-1 mysql -uihub_user -pihub_password internship_hub
```

Then you can run SQL queries like:

```sql
SHOW TABLES;
SELECT * FROM user;
```

Type `exit` to quit the MySQL shell.

## Notes

* The virtual environment (`venv/`) should NOT be committed to git - it's already in .gitignore
* Same with `node_modules/` in the frontend
* If you pull new changes from git, you might need to:
  * `pip install -r backend/requirements.txt` (if backend dependencies changed)
  * `cd frontend && npm install` (if frontend dependencies changed)


