import uuid
from sqlalchemy import Column, DateTime, String, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from conn.db import Base


class UUIDMixin(object):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class TimeStampedMixin(object):
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class User(UUIDMixin, TimeStampedMixin, Base):
    username = Column(String(255))
