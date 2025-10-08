import sys
from pathlib import Path
import pytest

repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root / 'internship-hub'))

from app import create_app
from backend.models import db


@pytest.fixture
def app():
    _app = create_app(database_uri='sqlite:///:memory:')
    return _app


def test_db_create_all(app):
    with app.app_context():
        db.create_all()
        metadata = db.metadata
        assert len(metadata.tables) > 0