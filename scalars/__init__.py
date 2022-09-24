import uuid
import strawberry
import typing
from conn.db import db_sesssion as session
import models



@strawberry.type
class User:
    id: uuid.UUID
    username: str


@strawberry.type
class Vendor:
    id: uuid.UUID
    name: str
    produts: typing.List['Product']
    
    @classmethod
    def marshal(cls, model: models.Vendor) -> "Vendor":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
        )
    
@strawberry.type
class Product:
    id: uuid.UUID
    name: str
    price: float
    stock: int
    vendor: 'Vendor'
    
    @classmethod
    def marshal(cls, model: models.Product) -> "Product":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            price=model.price,
            stock=model.stock,
            vendor=Vendor.marshal(model.vendor)
        )
    
# MUTATIONS ARE FOR POST REQUESTS
    
@strawberry.type
class Query:
    @strawberry.field
    def products(self, info) -> typing.List[Product]:
        with session:
            return session.query(Product).all()
            
             