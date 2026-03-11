"""Tests for the Flask app."""
import pytest

from app import app


@pytest.fixture
def client():
    """Create test client."""
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_index_returns_200(client):
    """GET / returns 200 and JSON with message and status."""
    r = client.get("/")
    assert r.status_code == 200
    data = r.get_json()
    assert data["status"] == "ok"
    assert "message" in data


def test_health_returns_200(client):
    """GET /health returns 200 and healthy status."""
    r = client.get("/health")
    assert r.status_code == 200
    data = r.get_json()
    assert data["status"] == "healthy"


def test_health_content_type_json(client):
    """GET /health returns application/json."""
    r = client.get("/health")
    assert r.content_type == "application/json"
