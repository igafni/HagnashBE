# Imports

from fastapi import FastAPI
import uvicorn
from Routers.items import router as ItemsRouter
from Routers.comments import router as CommentsRouter
from Routers.resources.resources import router as ResourcesRouter


app = FastAPI()

app.include_router(ItemsRouter)
app.include_router(CommentsRouter)
app.include_router(ResourcesRouter)

uvicorn.run(app, host="127.0.0.1", port=5000)
