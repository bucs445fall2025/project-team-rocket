# Internship Hub
## CS 445 Final Project
### Fall 2024

### Team: Team Rocket

- Alex Eskenazi - Frontend Dev, UI Design
- Vaughn Stout - Backend Dev, Documentation, Team Lead  
- Vishil Patel - Backend Dev, Auth, QA Tester

## Getting Started
Internship Hub is a web platform where students can share and discover internship opportunities. The platform features role-based access control, content moderation, voting system, and comprehensive search functionality. Built with Flask backend and responsive HTML/CSS/JavaScript frontend.

### Quick Start

1. Install Python dependencies: `cd backend && pip install -r requirements.txt`
2. Initialize database: `python init_db.py`
3. Run application: `python app.py`
4. Open browser to: http://localhost:5000

### Features Implemented

- [x] User authentication with 4 role levels (Guest, Basic, Moderator, Admin)
- [x] Post creation and management with moderation workflow
- [x] Commenting system
- [x] Voting and ranking system
- [x] Search and filtering by keywords and tags
- [x] Content reporting system
- [x] Responsive Bootstrap UI
- [x] Unit tests for backend API

### Future Roadmap

- [ ] Email notifications for post approvals
- [ ] Advanced search filters (location, company size)
- [ ] User profiles and saved posts
- [ ] API rate limiting and security enhancements
- [ ] Mobile app companion
  
## SRS
See `etc/specifications.md` for detailed requirements and user stories.
  
### Prerequisites

* Python 3.7+
* pip (Python package manager)
* Modern web browser

### Installing
```bash
# Clone the repository
git clone <repository-url>
cd project-team-rocket

# Install backend dependencies
cd backend
pip install -r requirements.txt

# Initialize database with test data
python init_db.py

# Start the application
python app.py
```

Access the application at http://localhost:5000 with test accounts:

- Admin: admin@example.com / admin123
- Moderator: mod@example.com / mod123  
- Student: student@example.com / student123

## Built With

* [Flask](https://flask.palletsprojects.com/) - Python web framework
* [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM
* [Flask-Login](https://flask-login.readthedocs.io/) - User session management
* [Bootstrap](https://getbootstrap.com/) - Frontend CSS framework
* [SQLite](https://www.sqlite.org/) - Database engine
* [pytest](https://docs.pytest.org/) - Testing framework

## License
<< Add a [license](https://choosealicense.com/) >>

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
