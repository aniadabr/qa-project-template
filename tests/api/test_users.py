import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_get_posts_returns_200_and_list():
    req = requests.get(f"{BASE_URL}/posts", timeout=10)
    assert req.status_code == 200

    body = req.json()
    assert isinstance(body, list)
    assert len(body) > 0
    assert "userId" in body[0]

@pytest.mark.api
def test_create_post_returns_201():
    payload = {
        "title": "qa test",
        "body": "test body",
        "userId": 1
    }

    req= requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)
    assert req.status_code == 201

    body = req.json()
    assert body["title"] == payload["title"]