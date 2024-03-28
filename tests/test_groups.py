from fastapi.testclient import TestClient
from main import app
from database.database import SessionLocal, engine
from database.models import Base, Group

import pytest

Base.metadata.create_all(bind=engine)

@pytest.fixture
def test_db():
    connection = engine.connect()
    transaction = connection.begin()
    try:
        yield SessionLocal()
    finally:
        transaction.rollback()
        connection.close()

client = TestClient(app)

def test_create_group(test_db):
    response = client.post("/groups", params={"name": "Test Group"}).json()
    assert response["status_code"] == 201
    assert response["message"] == "Group created successfully"
    assert response["data"]["name"] == "Test Group"

def test_get_all_groups(test_db):
    group1 = Group(name="Group 1")
    group2 = Group(name="Group 2")
    test_db.add(group1)
    test_db.add(group2)
    test_db.commit()

    response = client.get("/groups").json()
    assert response["status_code"] == 200
    assert len(response["data"][-2:]) == 2

def test_get_group_by_id(test_db):
    group = Group(name="Test Group")
    test_db.add(group)
    test_db.commit()

    response = client.get(f"/groups/{group.id}").json()
    assert response["status_code"] == 200
    assert response["data"]["name"] == "Test Group"

def test_partial_update_group(test_db):
    group = Group(name="Test Group")
    test_db.add(group)
    test_db.commit()

    response = client.patch(f"/groups/{group.id}", params={"name": "Updated Group"}).json()
    assert response["status_code"] == 200
    assert response["data"]["name"] == "Updated Group"

def test_update_group(test_db):
    group = Group(name="Test Group")
    test_db.add(group)
    test_db.commit()

    response = client.put(f"/groups/{group.id}", params={"name": "New Name"}).json()
    assert response["status_code"] == 200
    assert response["data"]["name"] == "New Name"

def test_delete_group(test_db):
    group = Group(name="Test Group")
    test_db.add(group)
    test_db.commit()

    response = client.delete(f"/groups/{group.id}").json()
    assert response["status_code"] == 200
    assert response["message"] == "Group deleted successfully"
