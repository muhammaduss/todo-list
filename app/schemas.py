from pydantic import BaseModel


class TaskSerializer(BaseModel):
    title: str
    description: str
    status: str


class UserSerialzer(BaseModel):
    username: str
