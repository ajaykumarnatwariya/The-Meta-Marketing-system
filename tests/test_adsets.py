from fastapi.testclient import TestClient
from main import app
from database.database import SessionLocal, engine
from database.models import Base, Campaign, Adset, Group
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

def test_create_adset(test_db):
    campaign = Campaign()
    group1 = Group()
    group2 = Group()
    test_db.add(campaign)
    test_db.add(group1)
    test_db.add(group2)
    test_db.commit()

    response = client.post("/adsets",
        params={"name": "Test Adset", "optimization_goal": "Reach", "campaign_id": campaign.id},
        json=[group1.id, group2.id]).json()
    assert response["status_code"] == 201
    assert response["message"] == "Adset created successfully"
    assert response["data"]["name"] == "Test Adset"
    assert response["data"]["optimization_goal"] == "Reach"
    assert response["data"]["campaign"] == campaign.id
    assert response["data"]["groups"] == [group1.id, group2.id]

def test_get_all_adsets(test_db):
    adset1 = Adset(name="Adset 1", optimization_goal="Reach")
    adset2 = Adset(name="Adset 2", optimization_goal="Link Clicks")
    test_db.add(adset1)
    test_db.add(adset2)
    test_db.commit()

    response = client.get("/adsets").json()
    assert response["status_code"] == 200

def test_get_adset_by_id(test_db):
    adset = Adset(name="Adset 1", optimization_goal="Reach")
    test_db.add(adset)
    test_db.commit()

    response = client.get(f"/adsets/{adset.id}").json()
    assert response["status_code"] == 200
    assert response["data"]["name"] == "Adset 1"

def test_partial_update_adset(test_db):
    adset = Adset(name="Adset 1", optimization_goal="Reach")
    test_db.add(adset)
    test_db.commit()

    response = client.patch(f"/adsets/{adset.id}", params={"name": "Updated Adset"}).json()
    assert response["status_code"] == 200
    assert response["data"]["name"] == "Updated Adset"

def test_update_adset(test_db):
    adset = Adset(name="Adset 1", optimization_goal="Reach")
    test_db.add(adset)
    test_db.commit()

    response = client.put(f"/adsets/{adset.id}", params={"name": "New Name", "optimization_goal": "New Goal", "campaign_id": 1},
        json=[1,2]).json()
    assert response["status_code"] == 200
    assert response["data"]["name"] == "New Name"
    assert response["data"]["optimization_goal"] == "New Goal"

def test_delete_adset(test_db):
    adset = Adset(name="Adset 1", optimization_goal="Reach")
    test_db.add(adset)
    test_db.commit()

    response = client.delete(f"/adsets/{adset.id}").json()
    assert response["status_code"] == 200
    assert response["message"] == "Adset deleted successfully"
