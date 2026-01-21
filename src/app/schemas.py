from pydantic import BaseModel, Field
from typing import Optional


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
