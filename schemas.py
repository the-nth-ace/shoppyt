import typing
import strawberry


@strawberry.type
class Product:
    name: str
    price: float
    stock: int
    in_stock: bool
    vendor: "Vendor"


@strawberry.type
class Vendor:
    name: str
    email: str
    products: typing.List["Product"]


# def get_products_for_vendor(root) -> "Vendor":
#     return Vendor(name="")
