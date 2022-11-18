import pytest
from fantasy_app_project.app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app.test_client()

def test_main_route(app):
    response = app.get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, World!!!!'

def test_submodule_route(app):
    response = app.get('/test_submodule')

    assert response.status_code == 200