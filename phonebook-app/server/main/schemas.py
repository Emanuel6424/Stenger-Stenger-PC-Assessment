from pydantic import BaseModel

# Schema for input data (new contact)


class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str

# Schema for updating contact info


class ContactUpdate(BaseModel):
    first_name: str
    last_name: str
    phone: str

# Schema for returning contact data (with ID)


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone: str

    class Config:
        orm_mode = True  # Allows conversion from SQLAlchemy model
