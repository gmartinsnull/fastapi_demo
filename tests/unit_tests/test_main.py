import pytest
from fastapi.testclient import TestClient
from app.main import app  # Adjust this import based on your file structure


client = TestClient(app)

def test_root_endpoint():
    """
    Test the root endpoint '/'
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the Iris Species Prediction API!" in response.json()["message"]

def test_predict_endpoint():
    """
    Test the predict endpoint '/predict/'
    """
    response = client.get("/predict/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is the predict endpoint."}
