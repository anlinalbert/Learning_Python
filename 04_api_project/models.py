from pydantic import BaseModel, ConfigDict


class CreateTicket(BaseModel):
    title: str
    description: str

class UserResponse(BaseModel):
    id: int
    title: str
    description: str

    model_config = ConfigDict(from_attributes=True)