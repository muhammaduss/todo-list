from fastapi import APIRouter
from app.services.tasks.service import Tasks
from app.schemas import TaskSerializer
from typing import List

router_task = APIRouter(prefix="/tasks")


@router_task.get("/", response_model=List[TaskSerializer])
async def get_tasks():
    return await Tasks.get_tasks()


@router_task.post("/")
async def post_task(data: TaskSerializer):
    return await Tasks.post_task(data)


@router_task.put("/{id}")
async def update_task(id, data: TaskSerializer):
    return await Tasks.update_task(id, data)


@router_task.delete("/{id}")
async def delete_task(id):
    return await Tasks.delete_task(id)
