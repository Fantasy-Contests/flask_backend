import pytest
from fantasy_app_project.app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app.test_client()