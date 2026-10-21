from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.menu import router as menu_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    #allow_origins=["https://guiafacilmaua.onrender.com", "https://guiafacilmaua.pages.dev"],
    allow_origins=["http://127.0.0.1:8000", "http://localhost:8000"],
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(router=menu_router)
