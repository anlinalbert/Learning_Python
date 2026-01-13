from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///ticketing_tool.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autoflush=False,autocommit=False, bind=engine)
Base = declarative_base()

class Ticket(Base):
    __tablename__ = "ticket"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    priority = Column(String)

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()