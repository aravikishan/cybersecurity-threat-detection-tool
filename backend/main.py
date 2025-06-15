from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@db/threat_detection"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)

@app.post("/api/users/")
async def create_user(username: str, email: str):
    db = SessionLocal()
    user = User(username=username, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/api/alerts/")
async def get_alerts():
    return [{"alert": "Suspicious activity detected"}]