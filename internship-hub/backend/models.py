from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='basic')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    posts = db.relationship(
        'Post',
        backref='author',
        lazy=True,
        cascade='all, delete-orphan',
        foreign_keys='Post.author_id'
    )
    comments = db.relationship('Comment', backref='author', lazy=True)
    votes = db.relationship('Vote', backref='user', lazy=True)
    reports_made = db.relationship('Report', foreign_keys='Report.reporter_id', backref='reporter', lazy=True)
    reports_reviewed = db.relationship('Report', foreign_keys='Report.reviewed_by', backref='reviewer', lazy=True)

    def __repr__(self) -> str:
        return f'<User {self.username}>'

    def is_admin(self) -> bool:
        return self.role == 'admin'

    def is_moderator(self) -> bool:
        return self.role in ['moderator', 'admin']


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=False)
    tags = db.Column(db.String(500))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
    vote_score = db.Column(db.Integer, default=0)
    moderated_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    moderated_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan')
    votes = db.relationship('Vote', backref='post', lazy=True, cascade='all, delete-orphan')
    reports = db.relationship('Report', backref='post', lazy=True, cascade='all, delete-orphan')
    moderator = db.relationship('User', foreign_keys=[moderated_by])

    __table_args__ = (
        db.Index('idx_post_title_search', 'title'),
        db.Index('idx_post_tags_search', 'tags'),
        db.Index('idx_post_author', 'author_id'),
        db.Index('idx_post_score_date', 'vote_score', 'created_at'),
    )

    def __repr__(self):
        return f'<Post {self.title}>'
    def update_vote_score(self) -> None:
        upvotes: int = Vote.query.filter_by(post_id=self.id, vote_type='up').count()
        downvotes: int = Vote.query.filter_by(post_id=self.id, vote_type='down').count()
        self.vote_score = upvotes - downvotes
        db.session.commit()


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Comment {self.id} on Post {self.post_id}>'


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    vote_type = db.Column(db.String(10), nullable=False)  # 'up' or 'down'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'post_id', name='unique_user_post_vote'),
        db.Index('idx_post_vote_type', 'post_id', 'vote_type'),
        db.Index('idx_user_votes', 'user_id'),
    )

    def __repr__(self):
        return f'<Vote {self.vote_type} by User {self.user_id} on Post {self.post_id}>'


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    reason = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
    reviewed_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    reviewed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('reporter_id', 'post_id', name='unique_user_post_report'),
    )

    def __repr__(self):
        return f'<Report {self.id} on Post {self.post_id}>'

