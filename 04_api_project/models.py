from pydantic import BaseModel, ConfigDict


class CreateTicket(BaseModel):
    title: str
    description: str
    priority: str

class UserResponse(CreateTicket):
    id: int

    model_config = ConfigDict(from_attributes=True)