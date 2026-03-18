from db.model import Course
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select, update

async def orm_add_course(session: AsyncSession, name: str):
    course = Course(course_name=name)
    session.add(course)
    await session.commit()

async def get_all_course(session: AsyncSession):
    result = await session.execute(select(Course))
    return result.scalars().all()

async def orm_delete_course(session: AsyncSession, course_id: int):
    query = delete(Course).where(Course.course_id == course_id)
    await session.execute(query)
    await session.commit()

async def orm_edit_course(session: AsyncSession, course_id: int, course_name: str):
    course = (update(Course)
                .where(Course.course_id == course_id)
                .values(course_name=course_name)
              )
    await session.execute(course)
    await session.commit()