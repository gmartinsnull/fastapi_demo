"""
Create a FastAPI app
Root endpoint returns the app description
"""

from fastapi import FastAPI
from .routes import test_route_v1, root_route_v1
from .routes.middleware import AuthMiddleware


def create_app():
    """
    create FastAPI app
    """
    fastapi = FastAPI()
    fastapi.include_router(root_route_v1.router)
    fastapi.include_router(test_route_v1.router, prefix="/v1")
    return fastapi


app = create_app()

# add custom authentication to app
app.add_middleware(AuthMiddleware)
