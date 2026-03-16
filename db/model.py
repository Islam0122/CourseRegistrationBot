from sqlalchemy import DateTime, BigInteger, String, func, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class TimestampMixin:
    created: Mapped[DateTime] = mapped_column(
        DateTime,
        default=func.now()
    )

class User(TimestampMixin, Base):
<<<<<<< HEAD
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(String(255))

class Course(TimestampMixin, Base):
    __tablename__ = "courses"
    course_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(255))
    age: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(255))
    course_type: Mapped[str] = mapped_column(String(255))

=======
    __tablename__ = "users"  # название таблицы в базе данных
    id: Mapped[int] = mapped_column(primary_key=True) # Уникальный идентификатор пользователя в базе
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True) # Telegram ID пользователя (уникальный)
    username: Mapped[str] = mapped_column(String(255))  # Username пользователя Telegram

class Registrations(TimestampMixin, Base):
    __tablename__ = "registrations"  # название таблицы в базе данных
    id: Mapped[int] = mapped_column(primary_key=True) # Уникальный идентификатор пользователя в базе
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True) # Telegram ID пользователя (уникальный)
    course_id: Mapped[int] = mapped_column(Integer)  # Username пользователя Telegram
>>>>>>> 3d3b67c5c0d4e1c62b69ef99b107d7976669b24c
