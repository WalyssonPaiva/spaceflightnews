from lib.app import app
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)


def test_create_article(monkeypatch):
    monkeypatch.setenv('COLLECTION', 'test_collection', prepend=False)
    clear_db()
    response = client.post("/articles/", json=article_factory())
    expected_response = article_factory()
    expected_response["id"] = 0
    assert response.status_code == 200
    assert response.json() == expected_response

def test_get_articles(monkeypatch):
    monkeypatch.setenv('COLLECTION', 'test_collection', prepend=False)
    create_article_db()
    response = client.get("/articles/")
    assert len(response.json()) >= 1

def test_get_article(monkeypatch):
    monkeypatch.setenv('COLLECTION', 'test_collection', prepend=False)
    article = create_article_db()
    response = client.get(f"/articles/{article['id']}")
    assert response.status_code == 200
    assert response.json() == article

def test_update_article(monkeypatch):
    monkeypatch.setenv('COLLECTION', 'test_collection', prepend=False)
    article = create_article_db()
    article["title"] = "Updated Title"
    response = client.put(f"/articles/{article['id']}", json=article)
    assert response.status_code == 200
    assert response.json() == article

@pytest.fixture(scope='session', autouse=True)
def clear_after_all_tests():
    from _pytest.monkeypatch import MonkeyPatch
    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.setenv('COLLECTION', 'test_collection', prepend=False)
    clear_db()
    mpatch.undo()

def article_factory():
    return {
    "title": "Phase Four and Orbit Fab to work on Maxwell engine refueling",
    "url": "https://spacenews.com/phase-four-and-orbit-fab-maxwell-mou/",
    "imageUrl": "https://spacenews.com/wp-content/uploads/2022/01/rsz_2ndgenrftfiring.jpg",
    "newsSite": "SpaceNews",
    "summary": "Propulsion startup Phase Four has signed a memorandum of understanding with satellite refueling startup Orbit Fab aimed at preparing future Phase Four Maxwell engines for on-orbit refueling.",
    "publishedAt": "2022-01-24T16:02:46.000Z",
    "updatedAt": "2022-01-24T16:02:46.945Z",
    "featured": False,
    "launches": [],
    "events": []
  }

def create_article_db():
    from lib.database import article as article_db
    article = article_factory()
    article['id'] = article_db.get_next_id()
    return article_db.create_article(article)

def clear_db():
    from lib.database import article as article_db
    article_db.delete_collection()