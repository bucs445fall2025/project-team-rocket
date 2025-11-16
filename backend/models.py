from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

# database setup
db = SQLAlchemy()

# user model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')  # user, admin, moderator
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships - this stuff is confusing but it works
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    votes = db.relationship('Vote', backref='user', lazy=True)
    # TODO: figure out the report relationships later
    reports_made = db.relationship('Report', foreign_keys='Report.reporter_id', backref='reporter', lazy=True)
    reports_reviewed = db.relationship('Report', foreign_keys='Report.reviewed_by', backref='reviewer', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def is_admin(self):
        return self.role == 'admin'

    def is_moderator(self):
        return self.role in ['moderator', 'admin']
    
    def check_password(self, password):
        # check if password matches
        from flask_bcrypt import Bcrypt
        bcrypt = Bcrypt()
        return bcrypt.check_password_hash(self.password_hash, password)


# posts model - for internship posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=False)
    tags = db.Column(db.String(500))  # store as comma separated string
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='active')  # active, deleted, expired
    approved = db.Column(db.Boolean, nullable=False, default=True)  
    company = db.Column(db.String(200))
    vote_score = db.Column(db.Integer, default=0)  # calculated from votes
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationships
    comments = db.relationship('Comment', backref='post', lazy=True)
    votes = db.relationship('Vote', backref='post', lazy=True)
    reports = db.relationship('Report', backref='post', lazy=True)

    def __repr__(self):
        return f'<Post {self.title}>'
        
    def update_vote_score(self):
        # count up votes minus down votes
        upvotes = Vote.query.filter_by(post_id=self.id, vote_type='up').count()
        downvotes = Vote.query.filter_by(post_id=self.id, vote_type='down').count()
        self.vote_score = upvotes - downvotes
        db.session.commit()
        print(f"Updated vote score for post {self.id}: {self.vote_score}")  # debug


# comments on posts
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Comment {self.id} on Post {self.post_id}>'
    
    def can_edit(self, user):
        # users can edit their own comments, admins can edit any
        if user.is_admin():
            return True
        return self.author_id == user.id


# upvotes and downvotes
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    vote_type = db.Column(db.String(10), nullable=False)  # 'up' or 'down'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # make sure users can only vote once per post
    __table_args__ = (
        db.UniqueConstraint('user_id', 'post_id', name='unique_user_post_vote'),
    )

    def __repr__(self):
        return f'<Vote {self.vote_type} by User {self.user_id} on Post {self.post_id}>'


# reports for bad posts
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    reason = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')  # pending, resolved
    reviewed_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    reviewed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # users can only report each post once
    __table_args__ = (
        db.UniqueConstraint('reporter_id', 'post_id', name='unique_user_post_report'),
    )

    def __repr__(self):
        return f'<Report {self.id} on Post {self.post_id}>'

