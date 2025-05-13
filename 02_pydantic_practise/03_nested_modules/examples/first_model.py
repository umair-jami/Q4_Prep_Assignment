from pydantic import BaseModel
from typing import Optional, List

class Address(BaseModel):
    street:str
    city:str
    state:str
    country:str
    postal_code:str

class User(BaseModel):
    id:int
    name:str
    address:Address
    postal_code:str
    
class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]=None

Comment.model_rebuild()  # Rebuild the model to handle forward references

address1=Address(street="123 Main St", city="Springfield", state="IL", country="USA", postal_code="62701")
user1=User(id=1, name="John Doe", address=address1, postal_code="62701")
comment1=Comment(id=1, content="This is a comment", replies=[
    Comment(id=2, content="This is a reply to the comment",replies=None),
    Comment(id=3, content="This is another reply", replies=[
        Comment(id=4, content="This is a nested reply", replies=None)
    ])
])