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
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(String(255))

class Registration(TimestampMixin, Base):
    __tablename__ = "registration"
    course_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(255))
    age: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(255))
    course_type: Mapped[str] = mapped_column(String(255))

class Course(TimestampMixin, Base):
    __tablename__ = "courses"
    course_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    course_name: Mapped[str] = mapped_column(String(255))