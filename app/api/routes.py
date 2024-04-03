from fastapi import APIRouter

from .v1.routes import router as v1_router


api_router = APIRouter()

api_router.include_router(v1_router, prefix="/v1")

# for all endpoint that stars with "/" return a message with the endpoint
# @api_router.get("/{path:path}")
# def root(path:str):
#     return {"message": f"Hello {path}!"}