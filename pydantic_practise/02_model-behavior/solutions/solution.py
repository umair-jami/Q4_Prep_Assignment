from pydantic import BaseModel, Field,computed_field 


class Booking_model(BaseModel):
    user_id:int
    room_id:int
    nights:int=Field(...,ge=1)
    rate_per_night:float
    
    
    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.rate_per_night
    
    

book1=Booking_model(user_id=1,room_id=101,nights=3,rate_per_night=100.0)
print(book1)
print(book1.total_cost)  # Output: 300.0