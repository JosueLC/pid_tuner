# FastAPI server with React SPA
# endpoints starts with /api are handled by FastAPI,
# endpoints starts with / are handled by React SPA

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.api.routes import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api")

# Mount spa files in ./spa/build folder
app.mount("/spa", StaticFiles(directory="./app/spa/build"), name="spa")
app.mount("/static", StaticFiles(directory="./app/spa/build/static"), name="static")
# If the path is not starts with "/api/" redirects to spa with all parameters
# @app.get("/{path:path}")
@app.get("/")
# def spa(path: str):
def spa():
    return RedirectResponse(url="/spa/index.html")