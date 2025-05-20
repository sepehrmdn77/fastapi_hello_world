from sqlalchemy import (
    Column,
    String,
    Integer,
    func,
    DateTime,
)
from core.database import Base


class HelloModel(Base):
    __tablename__ = "helloworld"
    id = Column(Integer, nullable=False, autoincrement=True,primary_key=True)
    text = Column(String, nullable=False)
    time = Column(
        DateTime, server_default=func.now(), server_onupdate=func.now(), nullable=False
    )
