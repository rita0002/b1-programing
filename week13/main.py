from fastapi import FastAPI
from routes import users

app = FastAPI(
    title="User Management API",
    description="FastAPI backend for managing users",
    version="1.0.0",
)

app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"status": "healthy", "message": "API is running"}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "user-management", "version": "1.0.0"}
