from fastapi import APIRouter, status
from app.schemas import Task, TaskCreate
from app.database import tasks_db, get_next_id

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    new_task = Task(id=get_next_id(), **task.model_dump())
    tasks_db.append(new_task)
    return new_task


@router.get("/", response_model=list[Task])
async def read_tasks():
    return tasks_db
