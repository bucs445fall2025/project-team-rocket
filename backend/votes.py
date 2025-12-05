from flask import Blueprint, request, jsonify, session
from backend.models import db, Post, Vote
from backend.auth import login_required

votes_bp = Blueprint('votes', __name__, url_prefix='/api/votes')

@votes_bp.route('', methods=['POST'])
@login_required
def vote_post():
    try:
        data = request.get_json()
        
        if not data or 'post_id' not in data or 'vote_type' not in data:
            return jsonify({'error': 'Missing post_id or vote_type'}), 400
        
        post_id = data['post_id']
        vote_type = data['vote_type']
        
        if vote_type not in ['up', 'down']:
            return jsonify({'error': 'Invalid vote type. Must be "up" or "down"'}), 400
        
        # Check if post exists and is active
        post = Post.query.filter_by(id=post_id, status='active', approved=True).first()
        if not post:
            return jsonify({'error': 'Post not found'}), 404
        
        user_id = session['user_id']
        
        # Check if user already voted on this post
        existing_vote = Vote.query.filter_by(user_id=user_id, post_id=post_id).first()
        
        if existing_vote:
            if existing_vote.vote_type == vote_type:
                # Same vote type - remove the vote (toggle off)
                db.session.delete(existing_vote)
                message = f'{vote_type.capitalize()}vote removed'
            else:
                # Different vote type - update the vote
                existing_vote.vote_type = vote_type
                message = f'Vote changed to {vote_type}vote'
        else:
            # No existing vote - create new vote
            new_vote = Vote(
                user_id=user_id,
                post_id=post_id,
                vote_type=vote_type
            )
            db.session.add(new_vote)
            message = f'{vote_type.capitalize()}voted successfully'
        
        # Update post vote score
        post.update_vote_score()
        
        # Get updated vote info
        user_vote = None
        updated_vote = Vote.query.filter_by(user_id=user_id, post_id=post_id).first()
        if updated_vote:
            user_vote = updated_vote.vote_type
        
        return jsonify({
            'message': message,
            'post': {
                'id': post.id,
                'vote_score': post.vote_score,
                'user_vote': user_vote
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to process vote'}), 500

@votes_bp.route('/post/<int:post_id>', methods=['GET'])
def get_post_votes(post_id):
    try:
        # Check if post exists
        post = Post.query.filter_by(id=post_id, status='active', approved=True).first()
        if not post:
            return jsonify({'error': 'Post not found'}), 404
        
        # Get vote counts
        upvotes = Vote.query.filter_by(post_id=post_id, vote_type='up').count()
        downvotes = Vote.query.filter_by(post_id=post_id, vote_type='down').count()
        
        # Get user's vote if logged in
        user_vote = None
        if 'user_id' in session:
            vote = Vote.query.filter_by(
                user_id=session['user_id'], 
                post_id=post_id
            ).first()
            user_vote = vote.vote_type if vote else None
        
        return jsonify({
            'post_id': post_id,
            'vote_score': post.vote_score,
            'upvotes': upvotes,
            'downvotes': downvotes,
            'user_vote': user_vote
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch vote information'}), 500