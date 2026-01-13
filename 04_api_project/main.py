from typing import List

from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

from models import UserResponse, CreateTicket
from db import Ticket, get_db

app = FastAPI(title="Ticketing Tool")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/create_ticket", response_model=UserResponse)
async def create_ticket(ticket: CreateTicket, db: Session = Depends(get_db)):
    new_ticket = Ticket(**ticket.model_dump())
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@app.get("/tickets", response_model=List[UserResponse])
async def get_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()