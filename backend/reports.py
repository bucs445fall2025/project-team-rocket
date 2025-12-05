from flask import Blueprint, request, jsonify, session
from backend.models import db, Post, Report, User
from backend.auth import login_required, admin_required
from datetime import datetime

reports_bp = Blueprint('reports', __name__, url_prefix='/api/reports')

@reports_bp.route('', methods=['POST'])
@login_required
def create_report():
    try:
        data = request.get_json()
        
        if not data or 'post_id' not in data or 'reason' not in data:
            return jsonify({'error': 'Missing post_id or reason'}), 400
        
        post_id = data['post_id']
        reason = data['reason'].strip()
        
        if len(reason) < 5:
            return jsonify({'error': 'Reason must be at least 5 characters'}), 400
        
        if len(reason) > 500:
            return jsonify({'error': 'Reason cannot exceed 500 characters'}), 400
        
        # Check if post exists and is active
        post = Post.query.filter_by(id=post_id, status='active').first()
        if not post:
            return jsonify({'error': 'Post not found'}), 404
        
        user_id = session['user_id']
        
        # Check if user already reported this post
        existing_report = Report.query.filter_by(reporter_id=user_id, post_id=post_id).first()
        if existing_report:
            return jsonify({'error': 'You have already reported this post'}), 400
        
        # Create new report
        new_report = Report(
            reporter_id=user_id,
            post_id=post_id,
            reason=reason,
            status='pending'
        )
        
        db.session.add(new_report)
        db.session.commit()
        
        return jsonify({
            'message': 'Post reported successfully. Thank you for helping keep the community clean.',
            'report': {
                'id': new_report.id,
                'reason': new_report.reason,
                'created_at': new_report.created_at.isoformat()
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create report'}), 500

@reports_bp.route('', methods=['GET'])
@admin_required
def get_reports():
    try:
        # Get query parameters
        page = request.args.get('page', 1, type=int)
        per_page = min(request.args.get('per_page', 20, type=int), 100)
        status = request.args.get('status', 'pending')  # pending, resolved, dismissed
        
        # Build query
        query = Report.query
        if status and status != 'all':
            query = query.filter_by(status=status)
        
        # Order by creation date (newest first)
        query = query.order_by(Report.created_at.desc())
        
        # Paginate
        reports_paginated = query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        # Format response
        reports_data = []
        for report in reports_paginated.items:
            reports_data.append({
                'id': report.id,
                'post': {
                    'id': report.post.id,
                    'title': report.post.title,
                    'author': {
                        'id': report.post.author.id,
                        'username': report.post.author.username
                    },
                    'status': report.post.status
                },
                'reporter': {
                    'id': report.reporter.id,
                    'username': report.reporter.username
                },
                'reason': report.reason,
                'status': report.status,
                'reviewed_by': {
                    'id': report.reviewer.id,
                    'username': report.reviewer.username
                } if report.reviewer else None,
                'created_at': report.created_at.isoformat(),
                'reviewed_at': report.reviewed_at.isoformat() if report.reviewed_at else None
            })
        
        return jsonify({
            'reports': reports_data,
            'pagination': {
                'page': reports_paginated.page,
                'pages': reports_paginated.pages,
                'per_page': reports_paginated.per_page,
                'total': reports_paginated.total,
                'has_next': reports_paginated.has_next,
                'has_prev': reports_paginated.has_prev
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to fetch reports'}), 500

@reports_bp.route('/<int:report_id>/resolve', methods=['POST'])
@admin_required
def resolve_report(report_id):
    try:
        report = Report.query.get(report_id)
        
        if not report:
            return jsonify({'error': 'Report not found'}), 404
        
        data = request.get_json()
        action = data.get('action') if data else 'dismiss'  # dismiss, delete_post, expire_post
        
        if action not in ['dismiss', 'delete_post', 'expire_post']:
            return jsonify({'error': 'Invalid action'}), 400
        
        # Update report status
        report.status = 'resolved'
        report.reviewed_by = session['user_id']
        report.reviewed_at = datetime.utcnow()
        
        # Take action on the post if needed
        post = report.post
        if action == 'delete_post':
            post.status = 'deleted'
            post.updated_at = datetime.utcnow()
        elif action == 'expire_post':
            post.status = 'expired'
            post.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'message': f'Report resolved. Action taken: {action.replace("_", " ")}',
            'report': {
                'id': report.id,
                'status': report.status,
                'action_taken': action
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to resolve report'}), 500

@reports_bp.route('/post/<int:post_id>/mark-deleted', methods=['POST'])
@login_required
def mark_post_deleted(post_id):
    try:
        post = Post.query.get(post_id)
        
        if not post:
            return jsonify({'error': 'Post not found'}), 404
        
        user = User.query.get(session['user_id'])
        
        # Only post author or admin can mark as deleted
        if post.author_id != session['user_id'] and not user.is_admin():
            return jsonify({'error': 'Permission denied'}), 403
        
        post.status = 'deleted'
        post.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'message': 'Post marked as deleted',
            'post': {
                'id': post.id,
                'status': post.status
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to mark post as deleted'}), 500