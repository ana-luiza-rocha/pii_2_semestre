from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.menu import router as menu_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://guiafacilmaua.onrender.com", "http://127.0.0.1:5500"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(router=menu_router)