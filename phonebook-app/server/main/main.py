from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contacts_routes import router as contacts_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contacts_router)


@app.get("/")
def home():
    return {"message": "Phone Book API is running!"}
