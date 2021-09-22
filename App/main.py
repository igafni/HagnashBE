# Imports
# External
from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
# Internal
from .Routers.places import router as PlacesRouter
from .Routers.comments import router as CommentsRouter
from .Routers.resources.resources import router as ResourcesRouter

# from Routers.places import router as PlacesRouter
# from Routers.comments import router as CommentsRouter
# from Routers.resources.resources import router as ResourcesRouter


app = FastAPI()
app.mount("/static", StaticFiles(directory="statics"), name="static")

app.include_router(PlacesRouter)
app.include_router(CommentsRouter)
app.include_router(ResourcesRouter)

# uvicorn.run(app)