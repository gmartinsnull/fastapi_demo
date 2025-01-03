"""
Create a FastAPI app
Root endpoint returns the app description
"""

from fastapi import FastAPI
from .routes import mock_route_v1
from .routes.middleware import AuthMiddleware


def create_app():
    """
    create FastAPI app
    """
    fastapi = FastAPI()
    fastapi.include_router(mock_route_v1.router, prefix="/v1")
    return fastapi


app = create_app()

# add custom authentication to app
app.add_middleware(AuthMiddleware)


@app.get("/")
async def root():
    """
    root test endpoint
    """
    return {"message": "Welcome to fastapi demo API!"}
