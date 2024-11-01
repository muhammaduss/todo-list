from sqlalchemy import select, delete
from app.models import Task
from app.db.db_config import session


class Tasks:
    model = Task

    @classmethod
    async def get_tasks(cls):
        async with session() as s:
            statement = select(cls.model).order_by(cls.model.id)
            result = await s.execute(statement)
            return result.scalars()

    @classmethod
    async def post_task(cls, data):
        async with session() as s:
            statement = select(cls.model).order_by(cls.model.id.desc())
            result = await s.execute(statement)
            last = result.scalars().first()
            if last is None:
                last_id = 0
            else:
                last_id = last.id

            task = cls.model(
                id=last_id + 1,
                title=data.title,
                description=data.description,
                status=data.status,
            )
            s.add(task)
            await s.commit()

    @classmethod
    async def update_task(cls, id, data):
        async with session() as s:
            statement = select(cls.model).filter(cls.model.id == int(id))
            result = await s.execute(statement)
            task = result.scalars().one()
            task.title = data.title
            task.description = data.description
            task.status = data.status
            await s.commit()

    @classmethod
    async def delete_task(cls, id):
        async with session() as s:
            statement = delete(cls.model).filter(cls.model.id == int(id))
            await s.execute(statement)
            await s.commit()
