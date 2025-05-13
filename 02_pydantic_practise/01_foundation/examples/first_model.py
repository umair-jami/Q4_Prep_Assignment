from pydantic import BaseModel
from typing import List, Dict, Optional

# class User(BaseModel):
#     id:int
#     name:str
#     email:str
#     is_active:bool
    
# input_data={'id':101,'name':"chain",'email':"info@gmail.com",'is_active':True}
# user=User(**input_data)
# print(user)


# Example 2: Nested Models
class Cart(BaseModel):
    item_id: int
    quantity: Dict[str,int]
    items:List[str]
    
class BlogPost(BaseModel):
    title:str
    content:str
    image_url:Optional[str]=None
