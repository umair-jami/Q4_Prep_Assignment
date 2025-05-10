from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

product1=Product(id=1, name="Laptop", price=999.99, quantity=10)
print(product1)    