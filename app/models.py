from sqlalchemy import Column, Integer, String, Numeric
from .database import Base

class users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)