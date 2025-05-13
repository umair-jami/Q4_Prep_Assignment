# Importing necessary components from the Pydantic library.
# BaseModel is the base class for defining data models.
# field_validators, model_validator, and computed_field are decorators for validation and computed properties.
# The #type: ignore[import] comment suppresses type-checking errors for imports (useful if the type checker has issues).
from pydantic import BaseModel, field_validators, model_validator, computed_field #type: ignore[import]

# Defining a User model that inherits from Pydantic's BaseModel.
# This class represents a user with a username field.
class User(BaseModel):
    # The username field is defined as a string (str).
    username: str
    
    # The @field_validators decorator is used to define a validator for the 'username' field.
    # It runs validation logic for the specified field (here, 'username').
    @field_validators('username')
    # The validator function takes the class (cls) and the value (v) of the field.
    def username_length(cls, v):
        # Check if the username length is less than 3 characters.
        if len(v) < 3:
            # If the condition is not met, raise a ValueError with a descriptive message.
            raise ValueError('Username must be at least 3 characters long')
        # If validation passes, return the value (v) unchanged.
        return v

# Defining a PasswordCheck model that inherits from BaseModel.
# This class validates that a password and its confirmation match.
class PasswordCheck(BaseModel):
    # Two fields: password and confirm_pass, both strings.
    password: str
    confirm_pass: str
    
    # The @model_validator decorator is used to validate the entire model after all fields are set.
    # mode='after' means the validation happens after the model's fields are populated.
    @model_validator(mode='after')
    # The validator function takes the class (cls) and the model instance (value).
    def check_password(cls, value):
        # Compare the password and confirm_pass fields of the model instance.
        if value.password != value.confirm_pass:
            # If they don't match, raise a ValueError with a descriptive message.
            raise ValueError('Password and confirm password do not match')
        # If validation passes, return the model instance unchanged.
        return value

# Defining a Product model that inherits from BaseModel.
# This class represents a product with a name, price, and quantity.
class Product(BaseModel):
    # Three fields: name (string), price (float), and quantity (integer).
    name: str
    price: float
    quantity: int
    
    # The @computed_field decorator marks a method as a computed field.
    # This field is calculated dynamically and included in the model's serialization.
    @computed_field
    # The @property decorator makes total_price behave like a read-only property.
    @property
    def total_price(self) -> float:
        # Calculate the total price by multiplying price and quantity.
        # The return type is explicitly annotated as float.
        return self.price * self.quantity