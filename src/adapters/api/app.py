from fastapi import FastAPI

from src.adapters.api import routes as ImageRouter

app = FastAPI(title="PhotoDetect", version="0.1")


app.include_router(ImageRouter.router, tags=['images'], prefix='/api/images')
