#!/usr/bin/env python3
"""
Script to add comprehensive sample data to the database.
This includes users, posts, comments, and votes for testing.
"""

from app import app
from backend.models import db, User, Post, Vote, Comment
from backend.auth import bcrypt
from datetime import datetime, timedelta
import random

def add_sample_users():
    """Create sample user accounts with different roles"""
    print("Creating sample users...")

    users_data = [
        {
            'username': 'alice_smith',
            'email': 'alice.smith@binghamton.edu',
            'password': 'password123',
            'role': 'user'
        },
        {
            'username': 'bob_jones',
            'email': 'bob.jones@binghamton.edu',
            'password': 'password123',
            'role': 'user'
        },
        {
            'username': 'carol_wilson',
            'email': 'carol.wilson@binghamton.edu',
            'password': 'password123',
            'role': 'user'
        },
        {
            'username': 'david_lee',
            'email': 'david.lee@binghamton.edu',
            'password': 'password123',
            'role': 'user'
        },
        {
            'username': 'emma_chen',
            'email': 'emma.chen@binghamton.edu',
            'password': 'password123',
            'role': 'user'
        },
        {
            'username': 'frank_garcia',
            'email': 'frank.garcia@binghamton.edu',
            'password': 'password123',
            'role': 'user'
        },
        {
            'username': 'grace_kim',
            'email': 'grace.kim@binghamton.edu',
            'password': 'password123',
            'role': 'user'
        },
        {
            'username': 'henry_patel',
            'email': 'henry.patel@binghamton.edu',
            'password': 'password123',
            'role': 'user'
        },
        {
            'username': 'moderator_jane',
            'email': 'jane.moderator@binghamton.edu',
            'password': 'mod123',
            'role': 'moderator'
        }
    ]

    created_users = []
    for user_data in users_data:
        # Check if user already exists
        existing = User.query.filter_by(username=user_data['username']).first()
        if existing:
            print(f"  Skipping '{user_data['username']}' - already exists")
            created_users.append(existing)
            continue

        # Create new user
        password_hash = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
        user = User(
            username=user_data['username'],
            email=user_data['email'],
            password_hash=password_hash,
            role=user_data['role']
        )
        db.session.add(user)
        created_users.append(user)
        print(f"  Created user: {user_data['username']}")

    db.session.commit()
    return created_users


def add_sample_posts(users):
    """Create sample internship posts from various users"""
    print("\nAdding sample internship posts...")

    posts_data = [
        {
            'title': 'Software Engineering Intern - Google',
            'company': 'Google',
            'description': 'Join the Chrome team to work on cutting-edge web technologies. We\'re looking for students with strong programming skills in Python, JavaScript, or C++. This is a paid summer internship with potential for return offers.',
            'link': 'https://careers.google.com/jobs/results/',
            'tags': 'Software Engineering, Google, Python, JavaScript, C++, Web Development'
        },
        {
            'title': 'Data Science Intern - Microsoft',
            'company': 'Microsoft',
            'description': 'Work with big data and machine learning algorithms at Microsoft Azure. Great opportunity for students interested in AI, data analysis, and statistical modeling. Previous experience with Python, R, and SQL preferred.',
            'link': 'https://careers.microsoft.com/us/en',
            'tags': 'Data Science, Machine Learning, Python, AI, Microsoft, Azure, R, SQL'
        },
        {
            'title': 'Frontend Developer Intern - Shopify',
            'company': 'Shopify',
            'description': 'Build beautiful, responsive user interfaces using React and TypeScript. Remote-friendly position with flexible hours. Perfect for students passionate about user experience.',
            'link': 'https://www.shopify.com/careers',
            'tags': 'Frontend, React, TypeScript, Remote, Web Development, UI/UX, Shopify'
        },
        {
            'title': 'Mobile Development Intern - Meta',
            'company': 'Meta',
            'description': 'Develop mobile applications for iOS and Android using React Native. Work on features used by billions of people worldwide. Experience with Swift, Kotlin, or React Native is a plus.',
            'link': 'https://www.metacareers.com/',
            'tags': 'Mobile Development, iOS, Android, React Native, Meta, Facebook'
        },
        {
            'title': 'Backend Engineering Intern - Netflix',
            'company': 'Netflix',
            'description': 'Help build and scale backend services that power Netflix streaming for 200M+ subscribers. Work with distributed systems, microservices, and cloud infrastructure.',
            'link': 'https://jobs.netflix.com/',
            'tags': 'Backend Engineering, Netflix, Java, Python, Distributed Systems, Cloud'
        },
        {
            'title': 'UX Design Intern - Adobe',
            'company': 'Adobe',
            'description': 'Design intuitive user experiences for Creative Cloud applications. Work with design systems, prototyping, and user research. Portfolio required for application.',
            'link': 'https://www.adobe.com/careers.html',
            'tags': 'UX Design, UI/UX, Adobe, Design, Creative Cloud, Figma'
        },
        {
            'title': 'Cybersecurity Intern - Amazon AWS',
            'company': 'Amazon',
            'description': 'Join AWS Security team to help protect cloud infrastructure and customer data. Work on security automation, threat detection, and incident response.',
            'link': 'https://www.amazon.jobs/',
            'tags': 'Cybersecurity, AWS, Amazon, Cloud Security, Information Security'
        },
        {
            'title': 'Product Management Intern - Stripe',
            'company': 'Stripe',
            'description': 'Work cross-functionally to define and ship new product features for Stripe\'s payment platform. Ideal for students with technical background who want to learn product management.',
            'link': 'https://stripe.com/jobs',
            'tags': 'Product Management, Stripe, Payments, Product, Analytics'
        },
        {
            'title': 'Game Development Intern - Unity',
            'company': 'Unity',
            'description': 'Work on Unity game engine features and tools. Perfect for students passionate about game development, computer graphics, and real-time rendering.',
            'link': 'https://unity.com/careers',
            'tags': 'Game Development, Unity, C#, Graphics, Gaming, Real-time'
        },
        {
            'title': 'iOS Engineer Intern - Apple',
            'company': 'Apple',
            'description': 'Develop features for iOS applications using Swift and SwiftUI. Work with the latest Apple technologies and contribute to apps used by millions daily.',
            'link': 'https://www.apple.com/careers/',
            'tags': 'iOS, Apple, Swift, SwiftUI, Mobile Development'
        },
        {
            'title': 'AI Research Intern - OpenAI',
            'company': 'OpenAI',
            'description': 'Contribute to cutting-edge AI research and development. Work on large language models, reinforcement learning, or computer vision projects.',
            'link': 'https://openai.com/careers/',
            'tags': 'AI, Machine Learning, Research, OpenAI, Deep Learning, PyTorch'
        },
        {
            'title': 'Full Stack Intern - Airbnb',
            'company': 'Airbnb',
            'description': 'Build features across the entire stack - from React frontend to Ruby/Java backend. Work on projects that help millions of people find unique travel experiences.',
            'link': 'https://careers.airbnb.com/',
            'tags': 'Full Stack, Airbnb, React, Ruby, Java, Web Development'
        }
    ]

    created_posts = []
    for i, post_data in enumerate(posts_data):
        # Check if post already exists
        existing = Post.query.filter_by(title=post_data['title']).first()
        if existing:
            print(f"  Skipping '{post_data['title']}' - already exists")
            created_posts.append(existing)
            continue

        # Assign to different users (cycling through available users)
        author = users[i % len(users)]

        post = Post(
            title=post_data['title'],
            company=post_data['company'],
            description=post_data['description'],
            link=post_data['link'],
            tags=post_data['tags'],
            author_id=author.id,
            status='active',
            approved=True,
            vote_score=0,
            created_at=datetime.utcnow() - timedelta(days=random.randint(1, 30))
        )
        db.session.add(post)
        created_posts.append(post)
        print(f"  Added post: {post_data['title']} (by {author.username})")

    db.session.commit()
    return created_posts


def add_sample_comments(users, posts):
    """Add realistic comments to posts"""
    print("\nAdding sample comments...")

    comments_templates = [
        "This looks like an amazing opportunity! Has anyone applied to this position before?",
        "I applied last year and got to the final round. The interview process was really thorough but fair.",
        "Does anyone know what the salary range is for this internship?",
        "The application deadline is coming up soon - make sure to apply early!",
        "I worked here last summer and it was an incredible experience. Highly recommend!",
        "What are the main qualifications they're looking for? I want to make sure I'm a good fit.",
        "Is this position remote-friendly or is it fully on-site?",
        "The company culture here is supposed to be really great. Excited to apply!",
        "I'm a sophomore - do you think I have a chance, or should I wait until junior year?",
        "Thanks for sharing! I've been looking for opportunities like this.",
        "The tech stack looks really interesting. Anyone have experience with these technologies?",
        "I heard they have a really good mentorship program for interns.",
        "Does this internship convert to full-time? Looking for return offer potential.",
        "Application submitted! Fingers crossed 🤞",
        "The project descriptions sound really impactful. Love that they give interns real work.",
        "Anyone else having trouble with the application portal?",
        "I got an interview! Any tips on what to prepare?",
        "This company has been on my dream list for a while. Hope I get a chance!",
        "The benefits package for interns is supposedly really competitive.",
        "How many hours per week do interns typically work here?"
    ]

    added_count = 0
    # Add 2-5 comments to each post
    for post in posts[:8]:  # Comment on first 8 posts
        num_comments = random.randint(2, 5)
        used_users = set()

        for _ in range(num_comments):
            # Pick a random user who hasn't commented on this post yet
            available_users = [u for u in users if u.id not in used_users and u.id != post.author_id]
            if not available_users:
                break

            commenter = random.choice(available_users)
            used_users.add(commenter.id)

            comment = Comment(
                content=random.choice(comments_templates),
                post_id=post.id,
                author_id=commenter.id,
                created_at=post.created_at + timedelta(hours=random.randint(1, 72))
            )
            db.session.add(comment)
            added_count += 1

    db.session.commit()
    print(f"  Added {added_count} comments across posts")


def add_sample_votes(users, posts):
    """Add votes to posts to create realistic vote scores"""
    print("\nAdding sample votes...")

    added_count = 0
    for post in posts:
        # Randomly select 40-80% of users to vote
        num_voters = random.randint(int(len(users) * 0.4), int(len(users) * 0.8))
        voters = random.sample(users, num_voters)

        for voter in voters:
            # Skip if user is the post author
            if voter.id == post.author_id:
                continue

            # Check if vote already exists
            existing_vote = Vote.query.filter_by(user_id=voter.id, post_id=post.id).first()
            if existing_vote:
                continue

            # 75% chance of upvote, 25% chance of downvote
            vote_type = 'up' if random.random() < 0.75 else 'down'

            vote = Vote(
                user_id=voter.id,
                post_id=post.id,
                vote_type=vote_type,
                created_at=post.created_at + timedelta(hours=random.randint(1, 168))
            )
            db.session.add(vote)
            added_count += 1

    db.session.commit()

    # Update vote scores for all posts
    print("  Calculating vote scores...")
    for post in posts:
        post.update_vote_score()

    print(f"  Added {added_count} votes")


def main():
    with app.app_context():
        print("=" * 70)
        print("Adding Comprehensive Sample Data to Database")
        print("=" * 70)

        # Add users first
        users = add_sample_users()

        # Add admin to users list if exists
        admin = User.query.filter_by(username='admin').first()
        if admin and admin not in users:
            users.append(admin)

        # Add posts
        posts = add_sample_posts(users)

        # Add comments
        add_sample_comments(users, posts)

        # Add votes
        add_sample_votes(users, posts)

        print("\n" + "=" * 70)
        print("Sample Data Summary")
        print("=" * 70)
        print(f"Total Users:    {User.query.count()}")
        print(f"Total Posts:    {Post.query.count()}")
        print(f"Total Comments: {Comment.query.count()}")
        print(f"Total Votes:    {Vote.query.count()}")
        print("\n" + "=" * 70)
        print("Test User Accounts")
        print("=" * 70)
        print("All users have password: 'password123' (except moderator)")
        print("Moderator has password: 'mod123'")
        print("\nSample users:")
        for user in User.query.filter(User.username != 'admin').limit(5).all():
            print(f"  - {user.username} ({user.email})")
        print("\n" + "=" * 70)
        print("Done! You can now view this data in the app.")
        print("=" * 70)


if __name__ == '__main__':
    main()
