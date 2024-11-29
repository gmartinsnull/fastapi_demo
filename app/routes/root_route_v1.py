"""
user data operations module v1
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/",
    tags=["root"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def test():
    """
    get user from database by username
    """
    try:
        # token_username: str = access_token.get("sub")
        return {"success": "public root api"}
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error getting root: {e}")
        return {"message": "Error getting root"}
