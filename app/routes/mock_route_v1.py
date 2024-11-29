"""
user data operations module v1
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def test():
    """
    get user from database by username
    """
    try:
        return {"success": "public api test"}
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error getting test api: {e}")
        return {"message": "Error getting test api"}
