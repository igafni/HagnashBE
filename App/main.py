# Imports
# External
from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
# Internal
from starlette.middleware.cors import CORSMiddleware

from .Routers.places import router as PlacesRouter
from .Routers.comments import router as CommentsRouter
from .Routers.resources.resources import router as ResourcesRouter

# from Routers.places import router as PlacesRouter
# from Routers.comments import router as CommentsRouter
# from Routers.resources.resources import router as ResourcesRouter


app = FastAPI()
app.mount("/static", StaticFiles(directory="./App/statics"), name="static")
# app.mount("/static", StaticFiles(directory="statics"), name="static")
origins = [
    "http://localhost:3000"
    "https://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
    max_age=3600,
)
app.include_router(PlacesRouter)
app.include_router(CommentsRouter)
app.include_router(ResourcesRouter)

# uvicorn.run(app)
