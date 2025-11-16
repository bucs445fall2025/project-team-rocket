from flask import Blueprint, request, jsonify, session
from flask_bcrypt import Bcrypt
from backend.models import db, User

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
bcrypt = Bcrypt()

def init_bcrypt(app):
    bcrypt.init_app(app)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    # basic checks
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    username = data['username'].strip()
    email = data['email'].strip().lower()
    password = data['password']
    
    # some validation
    if len(username) < 3:
        return jsonify({'error': 'Username must be at least 3 characters'}), 400
    
    if len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters'}), 400
    
    # check email has @ and .
    if '@' not in email or '.' not in email:
        return jsonify({'error': 'Please enter a valid email'}), 400
    
    # see if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400
    
    # make new user
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        role='user'
    )
    
    db.session.add(new_user)
    db.session.commit()
    print(f"New user created: {username}")  # debug
    
    # log them in right away
    session['user_id'] = new_user.id
    session['username'] = new_user.username
    session['role'] = new_user.role
    
    return jsonify({
        'message': 'Account created successfully',
        'user': {
            'id': new_user.id,
            'username': new_user.username,
            'role': new_user.role
        }
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Missing username or password'}), 400
    
    username = data.get('username', '').strip()
    password = data.get('password', '')
    
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400
    
    # find user by username or email
    user = User.query.filter(
        (User.username == username) | (User.email == username.lower())
    ).first()
    
    # check if user exists and password is correct
    if not user or not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid username or password'}), 401
    
    # store user info in session
    session['user_id'] = user.id
    session['username'] = user.username
    session['role'] = user.role
    print(f"User {username} logged in")  # debug
    
    return jsonify({
        'message': 'Login successful',
        'user': {
            'id': user.id,
            'username': user.username,
            'role': user.role
        }
    }), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully'}), 200

@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    user = User.query.get(session['user_id'])
    if not user:
        session.clear()
        return jsonify({'error': 'User not found'}), 401
    
    return jsonify({
        'user': {
            'id': user.id,
            'username': user.username,
            'role': user.role,
            'email': user.email,
            'created_at': user.created_at.isoformat()
        }
    }), 200

# decorator to check if user is logged in
def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

# decorator to check if user is admin
def admin_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        
        user = User.query.get(session['user_id'])
        if not user or not user.is_admin():
            return jsonify({'error': 'Admin access required'}), 403
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function