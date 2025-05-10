from pydantic import BaseModel, Field #type: ignore[import]
from typing import List, Dict, Optional
class Employee(BaseModel):
    id: int
    name:str=Field(..., min_length=3, max_length=50, description="Name of the employee",examples="Umair jami")
    department:Optional[str]='General'
    salary:float=Field(...,ge=0, )