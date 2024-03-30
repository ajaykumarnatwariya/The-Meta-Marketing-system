from fastapi import APIRouter
from database.database import SessionLocal
from database.models import Campaign
from utils.custom_response import CustomResponse

router = APIRouter()

@router.post("/campaigns", response_model=CustomResponse, tags=["campaigns"])
def create_campaign(name: str, objective: str):
    """Create a new campaign.

    Args:
        name (str): The name of the campaign.
        objective (str): The objective of the campaign.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        new_campaign = Campaign(name=name, objective=objective)
        db.add(new_campaign)
        db.commit()
        db.refresh(new_campaign)
        return CustomResponse(status_code=201, message="Campaign created successfully", data=new_campaign.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to create campaign", error=str(e))

@router.get("/campaigns", response_model=CustomResponse, tags=["campaigns"])
def get_all_campaigns():
    """Get all campaigns.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        campaigns = db.query(Campaign).all()
        campaigns_json = [campaign.to_json() for campaign in campaigns]
        return CustomResponse(status_code=200, message="Success", data=campaigns_json)
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to retrieve campaigns", error=str(e))

@router.get("/campaigns/{campaign_id}", response_model=CustomResponse, tags=["campaigns"])
def get_campaign_by_id(campaign_id: int):
    """Get a campaign by ID.

    Args:
        campaign_id (int): The ID of the campaign to retrieve.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
        if not campaign:
            return CustomResponse(status_code=404, message="Campaign not found", data=None)
        return CustomResponse(status_code=200, message="Success", data=campaign.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to retrieve campaign", error=str(e))

@router.patch("/campaigns/{campaign_id}", response_model=CustomResponse, tags=["campaigns"])
def update_campaign(campaign_id: int, name: str = None, objective: str = None):
    """Update a campaign.

    Args:
        campaign_id (int): The ID of the campaign to update.
        name (str, optional): The new name of the campaign. Defaults to None.
        objective (str, optional): The new objective of the campaign. Defaults to None.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
        if not campaign:
            return CustomResponse(status_code=404, message="Campaign not found", data=None)
        if name:
            campaign.name = name
        if objective:
            campaign.objective = objective
        db.commit()
        db.refresh(campaign)
        return CustomResponse(status_code=200, message="Campaign updated successfully", data=campaign.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to update campaign", error=str(e))

@router.put("/campaigns/{campaign_id}", response_model=CustomResponse, tags=["campaigns"])
def update_campaign(campaign_id: int, name: str, objective: str):
    """Update a campaign using PUT method.

    Args:
        campaign_id (int): The ID of the campaign to update.
        name (str): The new name of the campaign.
        objective (str): The new objective of the campaign.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
        if not campaign:
            return CustomResponse(status_code=404, message="Campaign not found", data=None)
        campaign.name = name
        campaign.objective = objective
        db.commit()
        db.refresh(campaign)
        return CustomResponse(status_code=200, message="Campaign updated successfully", data=campaign.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to update campaign", error=str(e))

@router.delete("/campaigns/{campaign_id}", response_model=CustomResponse, tags=["campaigns"])
def delete_campaign(campaign_id: int):
    """Delete a campaign.

    Args:
        campaign_id (int): The ID of the campaign to delete.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
        if not campaign:
            return CustomResponse(status_code=404, message="Campaign not found", data=None)
        db.delete(campaign)
        db.commit()
        return CustomResponse(status_code=200, message="Campaign deleted successfully", data=None)
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to delete campaign", error=str(e))
