from fastapi import APIRouter
from database.database import SessionLocal
from database.models import Group
from utils.custom_response import CustomResponse

router = APIRouter()

@router.post("/groups", response_model=CustomResponse, tags=["groups"])
def create_group(name: str):
    """Create a new group.

    Args:
        name (str): The name of the group.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        new_group = Group(name=name)
        db.add(new_group)
        db.commit()
        db.refresh(new_group)
        return CustomResponse(status_code=201, message="Group created successfully", data=new_group.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to create group", error=str(e))

@router.get("/groups", response_model=CustomResponse, tags=["groups"])
def get_all_groups():
    """Get all groups.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        groups = db.query(Group).all()
        groups_json = [group.to_json() for group in groups]
        return CustomResponse(status_code=200, message="Success", data=groups_json)
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to retrieve groups", error=str(e))

@router.get("/groups/{group_id}", response_model=CustomResponse, tags=["groups"])
def get_group_by_id(group_id: int):
    """Get a group by ID.

    Args:
        group_id (int): The ID of the group to retrieve.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        group = db.query(Group).filter(Group.id == group_id).first()
        if not group:
            return CustomResponse(status_code=404, message="Group not found", data=None)
        return CustomResponse(status_code=200, message="Success", data=group.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to retrieve group", error=str(e))

@router.patch("/groups/{group_id}", response_model=CustomResponse, tags=["groups"])
def partial_update_group(group_id: int, name: str = None):
    """Update a group partially using PATCH method.

    Args:
        group_id (int): The ID of the group to update.
        name (str, optional): The new name of the group. Defaults to None.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        group = db.query(Group).filter(Group.id == group_id).first()
        if not group:
            return CustomResponse(status_code=404, message="Group not found", data=None)
        if name:
            group.name = name
        db.commit()
        db.refresh(group)
        return CustomResponse(status_code=200, message="Group updated successfully", data=group.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to update group", error=str(e))

@router.put("/groups/{group_id}", response_model=CustomResponse, tags=["groups"])
def update_group(group_id: int, name: str):
    """Update a group using PUT method.

    Args:
        group_id (int): The ID of the group to update.
        name (str): The new name of the group.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        group = db.query(Group).filter(Group.id == group_id).first()
        if not group:
            return CustomResponse(status_code=404, message="Group not found", data=None)
        group.name = name
        db.commit()
        db.refresh(group)
        return CustomResponse(status_code=200, message="Group updated successfully", data=group.to_json())
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to update group", error=str(e))

@router.delete("/groups/{group_id}", response_model=CustomResponse, tags=["groups"])
def delete_group(group_id: int):
    """Delete a group.

    Args:
        group_id (int): The ID of the group to delete.

    Returns:
        CustomResponse: Response containing status code, message, and data.
    """
    try:
        db = SessionLocal()
        group = db.query(Group).filter(Group.id == group_id).first()
        if not group:
            return CustomResponse(status_code=404, message="Group not found", data=None)
        db.delete(group)
        db.commit()
        return CustomResponse(status_code=200, message="Group deleted successfully", data=None)
    except Exception as e:
        return CustomResponse(status_code=500, message="Failed to delete group", error=str(e))
