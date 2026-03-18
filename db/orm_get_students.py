from sqlalchemy import select
from db.model import Registration

async def orm_get_students_all(session):
    query = select(Registration)
    result = await session.execute(query)
    return result.scalars().all()