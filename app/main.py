from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db

# Initialize the app
app = FastAPI(
    title="TinyApp API",
    description="A hypersmall FastAPI project",
    version="1.0.0"
)

# Creates the table if it doesn't exist yet - fine for learning,
# in real projects, you'd use a migration tool (Alembic) instead
models.Base.metadata.create_all(bind=engine)

# --- Endpoints ---

@app.post("/add_user")
def create_user(first_name: str, last_name: str, db: Session = Depends(get_db)):
    user = models.users(first_name=first_name, last_name=last_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(models.users).all()

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.users).filter(models.users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
