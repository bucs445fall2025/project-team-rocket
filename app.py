from flask import Flask, jsonify
from flask_cors import CORS
from backend.models import db
from backend.auth import auth_bp, init_bcrypt
from backend.posts import posts_bp
from backend.votes import votes_bp
from backend.comments import comments_bp
from backend.reports import reports_bp
from backend.admin import admin_bp
import os

# just creating the app here - simpler than factory pattern
app = Flask(__name__)

# basic config stuff
app.config['SECRET_KEY'] = "6fba8277f0c64d0193ad35e4e2cf6b5ddde1a9a7f5a07bda5a6a8cbdde3e7129"
# MySQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ihub_user:ihub_password@localhost:3306/internship_hub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# need CORS for react frontend
CORS(app, supports_credentials=True, origins=['http://localhost:3000', 'http://127.0.0.1:3000'])

# setup database and bcrypt
db.init_app(app)
init_bcrypt(app)

# register all the routes
app.register_blueprint(auth_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(votes_bp) 
app.register_blueprint(comments_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def index():
    return jsonify({'message': 'Internship Hub API is running!'})

# basic error handling - probably should add more
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # make admin user if not exists
        from backend.models import User
        from backend.auth import bcrypt
        
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            # just hardcode the password for now
            password_hash = bcrypt.generate_password_hash('admin123').decode('utf-8')
            admin = User(
                username='admin',
                email='admin@internshiphub.com', 
                password_hash=password_hash,
                role='admin'
            )
            db.session.add(admin)
            db.session.commit()
            print("Admin user created - username: admin, password: admin123")
        
    # run on port 5001 because 5000 conflicts with airplay
    app.run(debug=True, port=5001)