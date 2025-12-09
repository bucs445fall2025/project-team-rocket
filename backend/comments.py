from flask import Blueprint, request, jsonify, session
from backend.models import db, Post, Comment, User
from backend.auth import login_required
from datetime import datetime

comments_bp = Blueprint('comments', __name__, url_prefix='/api/comments')

@comments_bp.route('', methods=['POST'])
@login_required
def create_comment():
    data = request.get_json()
    print(f"Creating comment: {data}")  # debug
    
    if not data or 'post_id' not in data or 'content' not in data:
        return jsonify({'error': 'Missing post_id or content'}), 400
    
    post_id = data['post_id']
    content = data['content'].strip()
    
    # basic validation
    if len(content) < 1:
        return jsonify({'error': 'Comment cannot be empty'}), 400
    
    if len(content) > 1000:  # probably should be configurable but whatever
        return jsonify({'error': 'Comment too long'}), 400
    
    # make sure post exists
    post = Post.query.filter_by(id=post_id, status='active', approved=True).first()
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    
    # create comment
    new_comment = Comment(
        content=content,
        post_id=post_id,
        author_id=session['user_id']
    )
    
    db.session.add(new_comment)
    db.session.commit()
    print(f"Comment created with id: {new_comment.id}")  # debug
        
    # get author info to return with comment
    author = User.query.get(session['user_id'])
    return jsonify({
        'message': 'Comment created successfully',
        'comment': {
            'id': new_comment.id,
            'content': new_comment.content,
            'post_id': new_comment.post_id,
            'author': {
                'id': author.id,
                    'username': author.username
                },
                'created_at': new_comment.created_at.isoformat(),
                'can_edit': True
            }
    }), 201

@comments_bp.route('/post/<int:post_id>', methods=['GET'])
def get_post_comments(post_id):
    try:
        # Check if post exists
        post = Post.query.filter_by(id=post_id, status='active', approved=True).first()
        if not post:
            return jsonify({'error': 'Post not found'}), 404
        
        # Get comments for this post
        comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.asc()).all()
        
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
            'post_id': post_id,
            'comments': comments_data,
            'comment_count': len(comments_data)
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch comments'}), 500

@comments_bp.route('/<int:comment_id>', methods=['PUT'])
@login_required
def update_comment(comment_id):
    try:
        comment = Comment.query.get(comment_id)
        
        if not comment:
            return jsonify({'error': 'Comment not found'}), 404
        
        # Check permission
        user = User.query.get(session['user_id'])
        if comment.author_id != session['user_id'] and not user.is_admin():
            return jsonify({'error': 'Permission denied'}), 403
        
        data = request.get_json()
        if not data or 'content' not in data:
            return jsonify({'error': 'Missing content'}), 400
        
        content = data['content'].strip()
        
        if len(content) < 1:
            return jsonify({'error': 'Comment cannot be empty'}), 400
        
        if len(content) > 1000:
            return jsonify({'error': 'Comment cannot exceed 1000 characters'}), 400
        
        comment.content = content
        db.session.commit()
        
        return jsonify({
            'message': 'Comment updated successfully',
            'comment': {
                'id': comment.id,
                'content': comment.content,
                'author': {
                    'id': comment.author.id,
                    'username': comment.author.username
                },
                'created_at': comment.created_at.isoformat()
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update comment'}), 500

@comments_bp.route('/<int:comment_id>', methods=['DELETE'])
@login_required
def delete_comment(comment_id):
    try:
        comment = Comment.query.get(comment_id)
        
        if not comment:
            return jsonify({'error': 'Comment not found'}), 404
        
        # Check permission
        user = User.query.get(session['user_id'])
        if comment.author_id != session['user_id'] and not user.is_admin():
            return jsonify({'error': 'Permission denied'}), 403
        
        db.session.delete(comment)
        db.session.commit()
        
        return jsonify({'message': 'Comment deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete comment'}), 500