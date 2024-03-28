from typing import List
from fastapi import APIRouter
from database.database import SessionLocal
from database.models import Adset, Group, Campaign
from models.custom_response import CustomResponse

router = APIRouter()

@router.post("/adsets", response_model=CustomResponse, tags=["adsets"])
def create_adset(name: str, optimization_goal: str, campaign_id: int, group_ids: List[int]):
    """Create a new adset.

    Args:
        name (str): The name of the adset.
        optimization_goal (str): The optimization goal of the adset.
        campaign_id (int): The ID of the campaign to which the adset belongs.
        group_ids (List[int]): The IDs of the groups to which the adset belongs.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
        if not campaign:
            return CustomResponse(status_code=404, message="Campaign not found", data=None)

        groups = db.query(Group).filter(Group.id.in_(group_ids)).all()
        if len(groups) != len(group_ids):
            return CustomResponse(status_code=404, message="One or more groups not found", data=None)

        new_adset = Adset(name=name, optimization_goal=optimization_goal, campaign=campaign, groups=groups)
        db.add(new_adset)
        db.commit()
        db.refresh(new_adset)
        return CustomResponse(status_code=201, message="Adset created successfully", data=new_adset.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to create adset", error=str(e))

@router.get("/adsets", response_model=CustomResponse, tags=["adsets"])
def get_all_adsets():
    """Get all adsets.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        adsets = db.query(Adset).all()
        adsets_json = [adset.to_json() for adset in adsets]
        return CustomResponse(status_code=200, message="Success", data=adsets_json)
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to retrieve adsets", error=str(e))

@router.get("/adsets/{adset_id}", response_model=CustomResponse, tags=["adsets"])
def get_adset_by_id(adset_id: int):
    """Get an adset by ID.

    Args:
        adset_id (int): The ID of the adset to retrieve.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        adset = db.query(Adset).filter(Adset.id == adset_id).first()
        if not adset:
            return CustomResponse(status_code=404, message="Adset not found", data=None)
        return CustomResponse(status_code=200, message="Success", data=adset.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to retrieve adset", error=str(e))

@router.patch("/adsets/{adset_id}", response_model=CustomResponse, tags=["adsets"])
def partial_update_adset(adset_id: int, name: str = None, optimization_goal: str = None, campaign_id: int = None, group_ids: List[int] = None):
    """Update an adset partially using PATCH method.

    Args:
        adset_id (int): The ID of the adset to update.
        name (str, optional): The new name of the adset. Defaults to None.
        optimization_goal (str, optional): The new optimization goal of the adset. Defaults to None.
        campaign_id (int, optional): The new ID of the campaign to which the adset belongs. Defaults to None.
        group_ids (List[int], optional): The new IDs of the groups to which the adset belongs. Defaults to None.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        adset = db.query(Adset).filter(Adset.id == adset_id).first()
        if not adset:
            return CustomResponse(status_code=404, message="Adset not found", data=None)

        if name:
            adset.name = name
        if optimization_goal:
            adset.optimization_goal = optimization_goal
        if campaign_id:
            campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
            if not campaign:
                return CustomResponse(status_code=404, message="Campaign not found", data=None)
            adset.campaign = campaign
        if group_ids:
            groups = db.query(Group).filter(Group.id.in_(group_ids)).all()
            if len(groups) != len(group_ids):
                return CustomResponse(status_code=404, message="One or more groups not found", data=None)
            adset.groups = groups

        db.commit()
        db.refresh(adset)
        return CustomResponse(status_code=200, message="Adset updated successfully", data=adset.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to update adset", error=str(e))

@router.put("/adsets/{adset_id}", response_model=CustomResponse, tags=["adsets"])
def update_adset(adset_id: int, name: str, optimization_goal: str, campaign_id: int, group_ids: List[int]):
    """Update an adset using PUT method.

    Args:
        adset_id (int): The ID of the adset to update.
        name (str): The new name of the adset.
        optimization_goal (str): The new optimization goal of the adset.
        campaign_id (int): The new ID of the campaign to which the adset belongs.
        group_ids (List[int]): The new IDs of the groups to which the adset belongs.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        adset = db.query(Adset).filter(Adset.id == adset_id).first()
        if not adset:
            return CustomResponse(status_code=404, message="Adset not found", data=None)

        campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
        if not campaign:
            return CustomResponse(status_code=404, message="Campaign not found", data=None)

        groups = db.query(Group).filter(Group.id.in_(group_ids)).all()
        if len(groups) != len(group_ids):
            return CustomResponse(status_code=404, message="One or more groups not found", data=None)

        adset.name = name
        adset.optimization_goal = optimization_goal
        adset.campaign = campaign
        adset.groups = groups
        db.commit()
        db.refresh(adset)
        return CustomResponse(status_code=200, message="Adset updated successfully", data=adset.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to update adset", error=str(e))

@router.delete("/adsets/{adset_id}", response_model=CustomResponse, tags=["adsets"])
def delete_adset(adset_id: int):
    """Delete an adset.

    Args:
        adset_id (int): The ID of the adset to delete.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        adset = db.query(Adset).filter(Adset.id == adset_id).first()
        if not adset:
            return CustomResponse(status_code=404, message="Adset not found", data=None)
        db.delete(adset)
        db.commit()
        return CustomResponse(status_code=200, message="Adset deleted successfully", data=None)
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to delete adset", error=str(e))
