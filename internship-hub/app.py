from backend.models import db



def create_app(database_uri: Optional[str] = None) -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "6fba8277f0c64d0193ad35e4e2cf6b5ddde1a9a7f5a07bda5a6a8cbdde3e7129"
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri or 'sqlite:///internship_hub.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    @app.route('/')
    def index() -> str:
        return 'Database setup successful! Internship Hub is ready.'
    return app


if __name__ == '__main__':
    _app = create_app()
    with _app.app_context():
        db.create_all()
    _app.run(debug=True)