from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException
from pydantic import ConfigDict, BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

app = FastAPI(title="Todo")

# Database
engine = create_engine("sqlite:///todo.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database model
class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String(100), nullable=False)
    author = Column(String(100), nullable=True)

Base.metadata.create_all(engine)

# Pydantic models
class CreateTask(BaseModel):
    task: str
    author: Optional[str] = None

class UpdateTask(CreateTask):
    pass

class UserResponse(CreateTask):
    id: int

    model_config = ConfigDict(from_attributes=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/all_todos", response_model=List[UserResponse])
def read_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

@app.post("/create_task", response_model=UserResponse)
def create_task(todo: CreateTask, db: Session = Depends(get_db)):
    new_task = Todo(**todo.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.put("/update_task/{task_id}", response_model=UserResponse)
def update_task(task_id: int, todo: UpdateTask, db: Session = Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    for field, value in todo.model_dump().items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task

@app.delete("/delete_task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}