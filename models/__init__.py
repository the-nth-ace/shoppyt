from enum import unique
import uuid
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func
from conn.db import Base


class UUIDMixin(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class TimeStampedMixin(object):
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class User(UUIDMixin, TimeStampedMixin, Base):
    username = Column(String, unique=True)
    password = Column(String)

    def as_dict(self):
        return {
            'id': self.id,
            "userame": self.username,
            
        }

class Vendor(UUIDMixin, TimeStampedMixin, Base):
    name = Column(String)
    products = relationship("Product", backpopulates="vendor")

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            
        }

class Product(UUIDMixin, TimeStampedMixin, Base):
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    vendor_id = Column(UUID(as_uuid=True), ForeignKey("vendor.id"))
    vendor = relationship("Vendor", back_populates="products", lazy="dynamic")

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'vendor_id': self.vendor_id
        }