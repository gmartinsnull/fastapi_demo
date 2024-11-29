import pytest
from fastapi.testclient import TestClient
from app.main import app  # Adjust this import based on your file structure


client = TestClient(app)


def test_root_endpoint():
    """
    Test the root endpoint '/'
    """
    print("Testing root endpoint")
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to fastapi demo API!" in response.json()[
        "message"]


# def test_mock_endpoint():
#     """
#     Test the "test" endpoint '/test/'
#     """
#     print("Testing \"test\" endpoint")
#     response = client.get("/test")
#     assert response.status_code == 200
#     assert response.json() == {"success": "public api test"}
