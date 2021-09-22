# Imports

from fastapi import FastAPI
import uvicorn
from .Routers.places import router as PlacesRouter
from .Routers.comments import router as CommentsRouter
from .Routers.resources.resources import router as ResourcesRouter


app = FastAPI()

app.include_router(PlacesRouter)
app.include_router(CommentsRouter)
app.include_router(ResourcesRouter)

#uvicorn.run(app)