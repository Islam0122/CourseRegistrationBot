from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from .model import User

""" ADD USER """
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