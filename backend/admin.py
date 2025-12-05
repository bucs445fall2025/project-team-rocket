from flask import Blueprint, request, jsonify, session
from sqlalchemy import desc
from backend.models import db, Post, User, Report
from backend.auth import admin_required
from datetime import datetime

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@admin_bp.route('/posts', methods=['GET'])
@admin_required
def get_all_posts():
    try:
        # Get query parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        status = request.args.get('status', 'all')  # all, active, deleted, expired
        
        # Build query
        query = Post.query
        if status != 'all':
            query = query.filter_by(status=status)
        
        # Order by creation date (newest first)
        query = query.order_by(desc(Post.created_at))
        
        # Paginate
        posts_paginated = query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        # Format response
        posts_data = []
        for post in posts_paginated.items:
            # Get report count for this post
            report_count = Report.query.filter_by(post_id=post.id, status='pending').count()
            
            posts_data.append({
                'id': post.id,
                'title': post.title,
                'description': post.description,
                'company': post.company,
                'link': post.link,
                'tags': post.tags.split(',') if post.tags else [],
                'author': {
                    'id': post.author.id,
                    'username': post.author.username
                },
                'status': post.status,
                'approved': post.approved,
                'vote_score': post.vote_score,
                'report_count': report_count,
                'created_at': post.created_at.isoformat(),
                'updated_at': post.updated_at.isoformat()
            })
        
        return jsonify({
            'posts': posts_data,
            'pagination': {
                'page': posts_paginated.page,
                'pages': posts_paginated.pages,
                'per_page': posts_paginated.per_page,
                'total': posts_paginated.total,
                'has_next': posts_paginated.has_next,
                'has_prev': posts_paginated.has_prev
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch posts'}), 500

@admin_bp.route('/posts/<int:post_id>/delete', methods=['POST'])
@admin_required
def delete_post_admin(post_id):
    try:
        post = Post.query.get(post_id)
        
        if not post:
            return jsonify({'error': 'Post not found'}), 404
        
        # Mark as deleted instead of actually deleting
        post.status = 'deleted'
        post.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'message': 'Post marked as deleted',
            'post': {
                'id': post.id,
                'title': post.title,
                'status': post.status
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete post'}), 500

@admin_bp.route('/posts/<int:post_id>/restore', methods=['POST'])
@admin_required
def restore_post_admin(post_id):
    try:
        post = Post.query.get(post_id)
        
        if not post:
            return jsonify({'error': 'Post not found'}), 404
        
        # Restore post to active status
        post.status = 'active'
        post.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'message': 'Post restored successfully',
            'post': {
                'id': post.id,
                'title': post.title,
                'status': post.status
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to restore post'}), 500

@admin_bp.route('/users', methods=['GET'])
@admin_required
def get_all_users():
    try:
        # Get query parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        # Get all users
        users_paginated = User.query.order_by(desc(User.created_at)).paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        # Format response
        users_data = []
        for user in users_paginated.items:
            post_count = Post.query.filter_by(author_id=user.id).count()
            
            users_data.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'post_count': post_count,
                'created_at': user.created_at.isoformat()
            })
        
        return jsonify({
            'users': users_data,
            'pagination': {
                'page': users_paginated.page,
                'pages': users_paginated.pages,
                'per_page': users_paginated.per_page,
                'total': users_paginated.total,
                'has_next': users_paginated.has_next,
                'has_prev': users_paginated.has_prev
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch users'}), 500