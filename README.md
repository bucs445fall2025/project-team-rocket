# Binghamton Student Internship Hub
## CS 445 Final Project
### Fall 2025

### Team: Rocket
Alex Eskenazi, Vaughn Stout, Vishil Patel

## Getting Started
Web app with internship hub functionality, such as an account login system with admin/moderator/user roles, ability to view/vote/comment on posts, as well as upload your own. You can also filter specific posts you want through name or tags.

### Roadmap
- [X] Login/signup system
- [X] Post creation/deletion
- [X] Post voting/commenting
- [X] Filters
- [X] Post tags
- [ ] Time of upload (currently in UTC)
  
## Documentation
* [Software Requirements Specification (SRS)](etc/SRS.md) - Detailed requirements and specifications
* [Setup Guide](SETUP.md) - Comprehensive setup instructions with troubleshooting

## Prerequisites
* [Docker](https://www.docker.com/)
* Python 3.10+
* Node.js 16+ and npm

## Installation & Setup

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/project-team-rocket.git
cd project-team-rocket
```

2. **Start the backend server**
```bash
./run-backend.sh
```
This script will:
- Create and activate a Python virtual environment
- Install backend dependencies from `backend/requirements.txt`
- Check MySQL database connection
- Start Flask server on port 5001

3. **Add sample data (optional but recommended)**
In a new terminal:
```bash
python3 add_sample_data.py
```
This adds test users, internship posts, comments, and votes for testing and demonstration.

4. **Start the frontend server**
In another terminal:
```bash
./run-frontend.sh
```
This script will:
- Install Node.js dependencies if needed
- Start React development server on port 3000
- Open browser automatically

### Test Accounts

After running `add_sample_data.py`, you can log in with:

| Username | Email | Password | Role |
|----------|-------|----------|------|
| admin | admin@internshiphub.com | admin123 | admin |
| moderator_jane | jane.moderator@binghamton.edu | mod123 | moderator |
| alice_smith | alice.smith@binghamton.edu | password123 | user |

See [SCRIPTS.md](SCRIPTS.md) for more test accounts and additional setup options.

### Troubleshooting

**Database connection errors:**
```bash
# Check if MySQL container is running
docker ps | grep mysql

# Start container if needed
docker start ihub-mysql-1
```

**Script permissions:**
```bash
chmod +x run-backend.sh run-frontend.sh
```

For more information:
* [SETUP.md](SETUP.md) - Detailed setup guide with Docker configuration and troubleshooting
* [SCRIPTS.md](SCRIPTS.md) - Available scripts and database setup options

## Built With

### Backend
* [Flask](https://flask.palletsprojects.com/) - Python web framework
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - ORM for database interactions
* [Flask-Login](https://flask-login.readthedocs.io/) - User session management
* [Flask-CORS](https://flask-cors.readthedocs.io/) - Cross-Origin Resource Sharing
* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/) - Password hashing
* [PyMySQL](https://pymysql.readthedocs.io/) - MySQL database connector

### Frontend
* [React](https://reactjs.org/) - JavaScript UI library
* [TypeScript](https://www.typescriptlang.org/) - Typed JavaScript
* [React Router](https://reactrouter.com/) - Client-side routing
* [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
* [Axios](https://axios-http.com/) - HTTP client for API requests

### Database
* [MySQL](https://www.mysql.com/) - Relational database (via Docker)

## License
GNU General Public License v3.0

## Acknowledgments
Steven Moore, Abror Mamataliev - Project guidance/check-ins
