from flask import Blueprint, request, jsonify, session
from sqlalchemy import or_, desc
from backend.models import db, Post, User, Vote, Comment
from backend.auth import login_required, admin_required
from datetime import datetime

posts_bp = Blueprint('posts', __name__, url_prefix='/api/posts')

@posts_bp.route('', methods=['GET'])
def get_posts():
    # get all the query stuff
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    search = request.args.get('search', '').strip()
    tags = request.args.get('tags', '').strip()
    sort_by = request.args.get('sort', 'recent')
    print(f"Getting posts - page: {page}, search: {search}")  # debug
    
    # only get active posts 
    query = Post.query.filter_by(status='active', approved=True)
        
    # search stuff
    if search:
        query = query.filter(
            or_(
                Post.title.contains(search),
                Post.description.contains(search),
                Post.company.contains(search) if Post.company else False
            )
        )
        print(f"Applied search filter: {search}")  # debug
    
    # filter by tags
    if tags:
        # split tags by comma
        tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
        for tag in tag_list:
            query = query.filter(Post.tags.contains(tag))
        print(f"Applied tag filters: {tag_list}")  # debug
        
    # sorting
    if sort_by == 'popular':
        query = query.order_by(desc(Post.vote_score), desc(Post.created_at))
        print("Sorting by popular")
    else:  # recent is default
        query = query.order_by(desc(Post.created_at))
        print("Sorting by recent")
    
    # paginate results
    posts_paginated = query.paginate(
        page=page, 
        per_page=per_page, 
        error_out=False
    )
    print(f"Found {posts_paginated.total} posts total")  # debug
    
    # format response
    posts_data = []
    for post in posts_paginated.items:
        # get user's vote if logged in
        user_vote = None
        if 'user_id' in session:
            vote = Vote.query.filter_by(
                user_id=session['user_id'], 
                post_id=post.id
            ).first()
            user_vote = vote.vote_type if vote else None
        
        # get comment count
        comment_count = Comment.query.filter_by(post_id=post.id).count()
        
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
            'vote_score': post.vote_score,
            'user_vote': user_vote,
            'comment_count': comment_count,
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

@posts_bp.route('', methods=['POST'])
@login_required
def create_post():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['title', 'description', 'link']
        if not data or not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        title = data['title'].strip()
        description = data['description'].strip()
        link = data['link'].strip()
        company = data.get('company', '').strip()
        tags = data.get('tags', '').strip()
        
        # Validate input
        if len(title) < 5:
            return jsonify({'error': 'Title must be at least 5 characters'}), 400
        
        if len(description) < 20:
            return jsonify({'error': 'Description must be at least 20 characters'}), 400
        
        if not link.startswith(('http://', 'https://')):
            return jsonify({'error': 'Link must be a valid URL'}), 400
        
        # Create new post
        new_post = Post(
            title=title,
            description=description,
            link=link,
            company=company if company else None,
            tags=tags if tags else None,
            author_id=session['user_id'],
            status='active',
            approved=True
        )
        
        db.session.add(new_post)
        db.session.commit()
        
        return jsonify({
            'message': 'Post created successfully',
            'post': {
                'id': new_post.id,
                'title': new_post.title,
                'description': new_post.description,
                'company': new_post.company,
                'link': new_post.link,
                'tags': new_post.tags.split(',') if new_post.tags else [],
                'created_at': new_post.created_at.isoformat()
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create post'}), 500

@posts_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    try:
        post = Post.query.filter_by(id=post_id, status='active', approved=True).first()
        
        if not post:
            return jsonify({'error': 'Post not found'}), 404
        
        # Get user's vote if logged in
        user_vote = None
        if 'user_id' in session:
            vote = Vote.query.filter_by(
                user_id=session['user_id'], 
                post_id=post.id
            ).first()
            user_vote = vote.vote_type if vote else None
        
        # Get comments
        comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.created_at.asc()).all()
        comments_data = []
        for comment in comments:
            comments_data.append({
                'id': comment.id,
                'content': comment.content,
                'author': {
                    'id': comment.author.id,
                    'username': comment.author.username
                },
                'created_at': comment.created_at.isoformat(),
                'can_edit': 'user_id' in session and (
                    session['user_id'] == comment.author_id or 
                    User.query.get(session['user_id']).is_admin()
                )
            })
        
        return jsonify({
            'post': {
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
                'vote_score': post.vote_score,
                'user_vote': user_vote,
                'created_at': post.created_at.isoformat(),
                'updated_at': post.updated_at.isoformat(),
                'can_edit': 'user_id' in session and (
                    session['user_id'] == post.author_id or 
                    User.query.get(session['user_id']).is_admin()
                )
            },
            'comments': comments_data
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch post'}), 500

@posts_bp.route('/<int:post_id>', methods=['PUT'])
@login_required
def update_post(post_id):
    try:
        post = Post.query.get(post_id)
        
        if not post:
            return jsonify({'error': 'Post not found'}), 404
        
        # Check permission
        user = User.query.get(session['user_id'])
        if post.author_id != session['user_id'] and not user.is_admin():
            return jsonify({'error': 'Permission denied'}), 403
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Update fields
        if 'title' in data:
            title = data['title'].strip()
            if len(title) < 5:
                return jsonify({'error': 'Title must be at least 5 characters'}), 400
            post.title = title
        
        if 'description' in data:
            description = data['description'].strip()
            if len(description) < 20:
                return jsonify({'error': 'Description must be at least 20 characters'}), 400
            post.description = description
        
        if 'link' in data:
            link = data['link'].strip()
            if not link.startswith(('http://', 'https://')):
                return jsonify({'error': 'Link must be a valid URL'}), 400
            post.link = link
        
        if 'company' in data:
            post.company = data['company'].strip() if data['company'] else None
        
        if 'tags' in data:
            post.tags = data['tags'].strip() if data['tags'] else None
        
        post.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'message': 'Post updated successfully',
            'post': {
                'id': post.id,
                'title': post.title,
                'description': post.description,
                'company': post.company,
                'link': post.link,
                'tags': post.tags.split(',') if post.tags else [],
                'updated_at': post.updated_at.isoformat()
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update post'}), 500

@posts_bp.route('/<int:post_id>', methods=['DELETE'])
@login_required
def delete_post(post_id):
    try:
        post = Post.query.get(post_id)
        
        if not post:
            return jsonify({'error': 'Post not found'}), 404
        
        # Check permission
        user = User.query.get(session['user_id'])
        if post.author_id != session['user_id'] and not user.is_admin():
            return jsonify({'error': 'Permission denied'}), 403
        
        # Mark as deleted instead of actually deleting
        post.status = 'deleted'
        post.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({'message': 'Post deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete post'}), 500