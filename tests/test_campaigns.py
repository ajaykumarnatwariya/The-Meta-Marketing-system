from fastapi.testclient import TestClient
from main import app
from database.database import SessionLocal, engine
from database.models import Base, Campaign

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

def test_create_campaign(test_db):
    response = client.post("/campaigns", params={"name": "Test Campaign"}).json()
    assert response["status_code"] == 201
    assert response["message"] == "Campaign created successfully"
    assert response["data"]["name"] == "Test Campaign"

def test_get_all_campaigns(test_db):
    campaign1 = Campaign(name="Campaign 1")
    campaign2 = Campaign(name="Campaign 2")
    test_db.add(campaign1)
    test_db.add(campaign2)
    test_db.commit()

    response = client.get("/campaigns").json()
    assert response["status_code"] == 200
    assert len(response["data"][-2:]) == 2

def test_get_campaign_by_id(test_db):
    campaign = Campaign(name="Test Campaign")
    test_db.add(campaign)
    test_db.commit()

    response = client.get(f"/campaigns/{campaign.id}").json()
    assert response["status_code"] == 200
    assert response["data"]["name"] == "Test Campaign"

def test_partial_update_campaign(test_db):
    campaign = Campaign(name="Test Campaign")
    test_db.add(campaign)
    test_db.commit()

    response = client.patch(f"/campaigns/{campaign.id}", params={"name": "Updated Campaign"}).json()
    assert response["status_code"] == 200
    assert response["data"]["name"] == "Updated Campaign"

def test_update_campaign(test_db):
    campaign = Campaign(name="Test Campaign")
    test_db.add(campaign)
    test_db.commit()

    response = client.put(f"/campaigns/{campaign.id}", params={"name": "New Name"}).json()
    assert response["status_code"] == 200
    assert response["data"]["name"] == "New Name"

def test_delete_campaign(test_db):
    campaign = Campaign(name="Test Campaign")
    test_db.add(campaign)
    test_db.commit()

    response = client.delete(f"/campaigns/{campaign.id}").json()
    assert response["status_code"] == 200
    assert response["message"] == "Campaign deleted successfully"
