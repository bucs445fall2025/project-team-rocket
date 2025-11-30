#!/usr/bin/env python3
"""
Script to add sample internship posts to the database.
Run this after the database is set up and you have at least one user.
"""

from app import app
from backend.models import db, User, Post, Vote, Comment
from datetime import datetime

def add_sample_internships():
    with app.app_context():
        # Get the admin user to be the author
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print("Error: Admin user not found. Please run the app first to create the admin user.")
            return

        print("Adding sample internship posts...")

        sample_posts = [
            {
                'title': 'Software Engineering Intern - Google',
                'company': 'Google',
                'description': 'Join the Chrome team to work on cutting-edge web technologies. We\'re looking for students with strong programming skills in Python, JavaScript, or C++. This is a paid summer internship with potential for return offers. You\'ll work alongside experienced engineers on real projects that impact millions of users.',
                'link': 'https://careers.google.com/jobs/results/',
                'tags': 'Software Engineering, Google, Python, JavaScript, C++, Web Development'
            },
            {
                'title': 'Data Science Intern - Microsoft',
                'company': 'Microsoft',
                'description': 'Work with big data and machine learning algorithms at Microsoft Azure. Great opportunity for students interested in AI, data analysis, and statistical modeling. You\'ll collaborate with data scientists and engineers to build predictive models and data pipelines. Previous experience with Python, R, and SQL preferred.',
                'link': 'https://careers.microsoft.com/us/en',
                'tags': 'Data Science, Machine Learning, Python, AI, Microsoft, Azure, R, SQL'
            },
            {
                'title': 'Frontend Developer Intern - Shopify',
                'company': 'Shopify',
                'description': 'Build beautiful, responsive user interfaces using React and TypeScript. Remote-friendly position with flexible hours. Perfect for students passionate about user experience and interface design. You\'ll work on Shopify\'s merchant admin dashboard and help improve the experience for millions of entrepreneurs.',
                'link': 'https://www.shopify.com/careers',
                'tags': 'Frontend, React, TypeScript, Remote, Web Development, UI/UX, Shopify'
            },
            {
                'title': 'Mobile Development Intern - Meta (Facebook)',
                'company': 'Meta',
                'description': 'Develop mobile applications for iOS and Android using React Native. Work on features used by billions of people worldwide. This role offers mentorship from senior engineers and the opportunity to ship code to production. Experience with Swift, Kotlin, or React Native is a plus.',
                'link': 'https://www.metacareers.com/',
                'tags': 'Mobile Development, iOS, Android, React Native, Meta, Facebook, Swift, Kotlin'
            },
            {
                'title': 'Backend Engineering Intern - Netflix',
                'company': 'Netflix',
                'description': 'Help build and scale backend services that power Netflix streaming for 200M+ subscribers. Work with distributed systems, microservices, and cloud infrastructure. We\'re looking for students with experience in Java, Python, or Go, and an interest in scalable systems.',
                'link': 'https://jobs.netflix.com/',
                'tags': 'Backend Engineering, Netflix, Java, Python, Go, Distributed Systems, Cloud'
            },
            {
                'title': 'Cybersecurity Intern - Amazon Web Services',
                'company': 'Amazon',
                'description': 'Join AWS Security team to help protect cloud infrastructure and customer data. Work on security automation, threat detection, and incident response. Great for students interested in information security, cryptography, and secure systems. Knowledge of networking and Linux is helpful.',
                'link': 'https://www.amazon.jobs/',
                'tags': 'Cybersecurity, AWS, Amazon, Cloud Security, Information Security, Linux'
            },
            {
                'title': 'Product Management Intern - Stripe',
                'company': 'Stripe',
                'description': 'Work cross-functionally to define and ship new product features for Stripe\'s payment platform. Collaborate with engineering, design, and business teams. Ideal for students with technical background who want to learn product management. Strong analytical and communication skills required.',
                'link': 'https://stripe.com/jobs',
                'tags': 'Product Management, Stripe, Payments, Product, Cross-functional, Analytics'
            },
            {
                'title': 'DevOps/SRE Intern - LinkedIn',
                'company': 'LinkedIn',
                'description': 'Help maintain and improve LinkedIn\'s infrastructure and deployment pipelines. Learn about CI/CD, containerization, and site reliability engineering. Work with Kubernetes, Docker, and monitoring tools. Great opportunity to learn production engineering at scale.',
                'link': 'https://www.linkedin.com/jobs/',
                'tags': 'DevOps, SRE, LinkedIn, Kubernetes, Docker, CI/CD, Infrastructure'
            },
            {
                'title': 'Machine Learning Intern - OpenAI',
                'company': 'OpenAI',
                'description': 'Contribute to cutting-edge AI research and development. Work on large language models, reinforcement learning, or computer vision projects. We\'re looking for students with strong math/CS background and experience with deep learning frameworks like PyTorch or TensorFlow.',
                'link': 'https://openai.com/careers/',
                'tags': 'Machine Learning, AI, OpenAI, Deep Learning, PyTorch, TensorFlow, Research'
            },
            {
                'title': 'Full Stack Intern - Airbnb',
                'company': 'Airbnb',
                'description': 'Build features across the entire stack - from React frontend to Ruby/Java backend. Work on projects that help millions of people find and book unique travel experiences. Collaborative environment with strong mentorship. Experience with modern web technologies preferred.',
                'link': 'https://careers.airbnb.com/',
                'tags': 'Full Stack, Airbnb, React, Ruby, Java, Web Development, Travel Tech'
            }
        ]

        # Add each post to the database
        added_count = 0
        for post_data in sample_posts:
            # Check if post already exists (by title)
            existing = Post.query.filter_by(title=post_data['title']).first()
            if existing:
                print(f"  Skipping '{post_data['title']}' - already exists")
                continue

            post = Post(
                title=post_data['title'],
                company=post_data['company'],
                description=post_data['description'],
                link=post_data['link'],
                tags=post_data['tags'],
                author_id=admin.id,
                status='active',
                approved=True,
                vote_score=0
            )
            db.session.add(post)
            added_count += 1
            print(f"  Added: {post_data['title']}")

        db.session.commit()

        print(f"\n✓ Successfully added {added_count} sample internship posts!")
        print(f"Total posts in database: {Post.query.count()}")

if __name__ == '__main__':
    print("=" * 60)
    print("Adding Sample Internship Posts")
    print("=" * 60)
    add_sample_internships()
    print("=" * 60)
    print("Done! You can now view these posts in the app.")
    print("=" * 60)
