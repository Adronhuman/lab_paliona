import pytest,requests

def test_app():
    BASE = f"http://localhost:5000/api/v1/hello-world-19"
    response = requests.get(BASE)
    assert response.status_code == 200
test_app()
