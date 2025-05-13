from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    
class User(BaseModel):
    id: int
    name: str
    is_active: bool=True
    created_at: datetime
    address: Address
    tags: List[str]=[]
    
user  =User(
    id=1,
    name="John Doe",
    created_at=datetime(2023, 10, 1, 12, 30),
    address=Address(street="123 Main St", city="Springfield", postal_code="62701"),
    tags=["admin", "user"],
    
    model_config=ConfigDict(
        json_encoders={
            datetime:lambda v: v.strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
)

# Using model_dump to serialize the model
python_dict = user.model_dump()
print(python_dict)
# Using model_dump_json to serialize the model to JSON
print(" ")
print(" ")
print(" ")
json_str = user.model_dump_json()
print(json_str)