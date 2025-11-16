import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


try:
    from app import create_app
except Exception as exc:
    raise RuntimeError("Unable to import 'create_app' from app.py") from exc

app = create_app()

from backend.models import db, User, Post, Comment, Vote, Report
from werkzeug.security import generate_password_hash
from datetime import datetime

def create_sample_data():
    
    print("Creating sample users...")
    
    # Create users with different permission levels
    admin_user = User(
        username='admin',
        email='admin@example.com',
        password_hash=generate_password_hash('admin123'),
        role='admin'
    )
    
    moderator_user = User(
        username='moderator',
        email='moderator@example.com',
        password_hash=generate_password_hash('mod123'),
        role='moderator'
    )
    
    basic_user1 = User(
        username='student1',
        email='student1@example.com',
        password_hash=generate_password_hash('student123'),
        role='basic'
    )
    
    basic_user2 = User(
        username='student2',
        email='student2@example.com',
        password_hash=generate_password_hash('student123'),
        role='basic'
    )
    
    # Save users to database
    db.session.add(admin_user)
    db.session.add(moderator_user)
    db.session.add(basic_user1)
    db.session.add(basic_user2)
    db.session.commit()
    
    print("Creating sample posts...")
    
    # Create sample internship posts
    post1 = Post(
        title='Software Engineering Intern at Google',
        description='Amazing opportunity to work with the Chrome team on cutting-edge web technologies. Looking for students with strong programming skills in Python, JavaScript, or Java. This is a paid internship with potential for return offers.',
        link='https://careers.google.com/jobs/results/sample1',
        tags='Software Engineering, Google, Chrome, Web Development, Python, JavaScript',
        author_id=basic_user1.id,
        status='approved'  # Pre-approved for demonstration
    )
    
    post2 = Post(
        title='Data Science Intern - Machine Learning Focus',
        description='Work with big data and machine learning algorithms to solve real-world problems. Great opportunity for students interested in AI, data analysis, and statistical modeling. Previous experience with Python and R preferred.',
        link='https://careers.microsoft.com/jobs/sample2',
        tags='Data Science, Machine Learning, Python, AI, Analytics, Statistics',
        author_id=basic_user2.id,
        status='approved'
    )
    
    post3 = Post(
        title='Frontend Developer Intern - React Position',
        description='Build beautiful, responsive user interfaces using React and modern web technologies. Remote-friendly position with flexible hours. Perfect for students passionate about user experience and interface design.',
        link='https://startup.com/careers/frontend-intern',
        tags='Frontend, React, JavaScript, Remote, Web Development, UI/UX',
        author_id=basic_user1.id,
        status='pending'  # This post needs moderation approval
    )
    
    # Save posts to database
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.commit()
    
    print("Creating sample comments...")
    
    # Create sample comments on posts
    comment1 = Comment(
        content='I applied to this position last year! The interview process was really smooth and the team was very welcoming. Definitely recommend applying early.',
        post_id=post1.id,
        author_id=basic_user2.id
    )
    
    comment2 = Comment(
        content='Does anyone know the application deadline for this position? The link doesn\'t seem to show specific dates.',
        post_id=post1.id,
        author_id=moderator_user.id
    )
    
    comment3 = Comment(
        content='Great opportunity! I worked in data science last summer and the mentorship was excellent. Make sure to highlight any statistics coursework.',
        post_id=post2.id,
        author_id=admin_user.id
    )
    
    # Save comments to database
    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.commit()
    
    print("Creating sample votes...")
    
    # Create sample votes to demonstrate ranking
    vote1 = Vote(user_id=basic_user1.id, post_id=post1.id, vote_type='up')
    vote2 = Vote(user_id=basic_user2.id, post_id=post1.id, vote_type='up')
    vote3 = Vote(user_id=moderator_user.id, post_id=post1.id, vote_type='up')
    vote4 = Vote(user_id=admin_user.id, post_id=post2.id, vote_type='up')
    vote5 = Vote(user_id=basic_user1.id, post_id=post2.id, vote_type='down')
    
    # Save votes to database
    db.session.add(vote1)
    db.session.add(vote2)
    db.session.add(vote3)
    db.session.add(vote4)
    db.session.add(vote5)
    db.session.commit()
    
    print("Creating sample report...")
    
    # Create sample report for moderation demonstration
    report1 = Report(
        reporter_id=basic_user2.id,
        post_id=post3.id,
        reason='The application link appears to be broken or expired',
        status='pending'
    )
    
    db.session.add(report1)
    db.session.commit()
    
    # Calculate and update vote scores for all posts
    print("Calculating vote scores...")
    for post in Post.query.all():
        post.update_vote_score()
    
    print("\n" + "="*50)
    print("DATABASE SETUP COMPLETE!")
    print("="*50)
    print("\nSample data created:")
    print(f"Users: {User.query.count()}")
    print(f"Posts: {Post.query.count()}")
    print(f"Comments: {Comment.query.count()}")
    print(f"Votes: {Vote.query.count()}")
    print(f"Reports: {Report.query.count()}")
    
    print("\nTest user accounts:")
    print("  Admin: admin@example.com / admin123")
    print("  Moderator: moderator@example.com / mod123")
    print("  Student1: student1@example.com / student123")
    print("  Student2: student2@example.com / student123")

def init_database():
    with app.app_context():
        print("Dropping existing tables if they exist...")
        db.drop_all()
        
        print("Creating all database tables...")
        db.create_all()
        
        print("Adding sample data...")
        create_sample_data()

if __name__ == '__main__':
    init_database()