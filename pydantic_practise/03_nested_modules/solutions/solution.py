from pydantic import BaseModel
from typing import List

class Lesson(BaseModel):
    lesson_id: int
    lesson_name: str
    duration: int  # in minutes
    
class Module(BaseModel):
    module_id: int
    module_name: str
    lessons: List[Lesson]
    
class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]