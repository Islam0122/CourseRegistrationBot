from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql.elements import and_

from .model import User
from .model import Course

async def orm_add_user(session: AsyncSession, telegram_id: int, username: str):
    new_user = User(
        telegram_id=telegram_id,
        username=username
    )
    try:
        session.add(new_user)
        await session.commit()
        return new_user

    except IntegrityError:
        await session.rollback()
        return None

async def orm_add_courses(session: AsyncSession, telegram_id: int, name: str, age: str, phone: str, course_type: str):
    new_course = Course(
        telegram_id=telegram_id,
        name=name,
        age=age,
        phone=phone,
        course_type=course_type
    )
    try:
        session.add(new_course)
        await session.commit()
        return new_course

    except IntegrityError:
        await session.rollback()
        return None

async def check_registration(session: AsyncSession, name: str ,course_type: str):

    query = select(Course).where(
        and_(
            Course.name == name,
            Course.course_type == course_type
        )
    )

    result = await session.execute(query)
    return result.scalars().first()