import uuid

from sqlalchemy import Column, DateTime, Integer, Float, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import fun

from conn.db import Base


class User(Base):
    __tablename__ = "vendors"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
