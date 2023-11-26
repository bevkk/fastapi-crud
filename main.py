from fastapi import FastAPI, HTTPException, Response, status
from app.routes.routes import router

app = FastAPI()
post_router = router

app.include_router(post_router)