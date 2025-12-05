# Internship Hub - Project Structure

## Directory Layout

Current project structure:

```
project-team-rocket/
├── app.py                      # Flask application entry point (runs on port 5001)
├── backend/                    # All backend Python code
│   ├── __init__.py
│   ├── models.py              # Database models (User, Post, Comment, Vote, Report)
│   ├── auth.py                # Authentication routes (/api/auth/*)
│   ├── posts.py               # Posts API (/api/posts/*)
│   ├── votes.py               # Voting system (/api/votes/*)
│   ├── comments.py            # Comments API (/api/comments/*)
│   ├── reports.py             # Reporting system (/api/reports/*)
│   ├── admin.py               # Admin panel routes (/api/admin/*)
│   ├── init_db.py             # Database initialization script
│   ├── add_indexes.py         # Database index optimization
│   └── requirements.txt       # Python dependencies
├── frontend/                   # React frontend application
│   ├── src/
│   │   ├── index.tsx          # Entry point
│   │   ├── App.tsx            # Main app component
│   │   ├── components/        # Reusable components
│   │   ├── pages/             # Page components
│   │   ├── contexts/          # React contexts (auth)
│   │   ├── services/          # API service
│   │   └── lib/               # Utilities and validations
│   ├── public/
│   │   └── index.html         # HTML template
│   ├── package.json           # Node dependencies
│   ├── tsconfig.json          # TypeScript config
│   ├── tailwind.config.js     # Tailwind CSS config
│   └── postcss.config.js      # PostCSS config
├── run-backend.sh             # Convenience script to start backend
├── run-frontend.sh            # Convenience script to start frontend
├── add_sample_internships.py  # Script to populate sample data
├── SETUP.md                   # Detailed setup instructions
├── README.md                  # Project overview
├── LICENSE                    # Project license
├── SCRIPTS.md                 # Helper scripts
└── venv/                      # Python virtual environment (gitignored)
```

## Key Points

### Backend
- **Location**: `/backend/` directory
- **Entry point**: `app.py` in the root directory
- **Database**: MySQL (running in Docker)
- **Port**: 5001 (configured in app.py)
- **Framework**: Flask with SQLAlchemy ORM

### Frontend
- **Location**: `/frontend/` directory
- **Entry point**: `src/index.tsx`
- **Port**: 3000
- **Framework**: React with TypeScript
- **Styling**: Tailwind CSS
- **API Proxy**: Configured to proxy to localhost:5001

### Scripts
- **run-backend.sh**: Starts Flask backend (auto-installs dependencies)
- **run-frontend.sh**: Starts React frontend (auto-installs dependencies)
- **add_sample_internships.py**: Adds 10 sample internship posts to database
