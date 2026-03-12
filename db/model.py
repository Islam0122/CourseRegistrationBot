from sqlalchemy import DateTime, BigInteger, String, func, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# Базовый класс для всех ORM моделей
# Все таблицы базы данных будут наследоваться от него
class Base(DeclarativeBase):
    pass


# Mixin для добавления поля времени создания записи
# Это поле автоматически будет добавляться в таблицы,
# которые наследуют этот класс
class TimestampMixin:
    created: Mapped[DateTime] = mapped_column(
        DateTime,
        default=func.now()  # автоматически ставит текущее время
    )


# Модель пользователя
class User(TimestampMixin, Base):
    __tablename__ = "users"  # название таблицы в базе данных
    id: Mapped[int] = mapped_column(primary_key=True) # Уникальный идентификатор пользователя в базе
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True) # Telegram ID пользователя (уникальный)
    username: Mapped[str] = mapped_column(String(255))  # Username пользователя Telegram

class Registrations(TimestampMixin, Base):
    __tablename__ = "registrations"  # название таблицы в базе данных
    id: Mapped[int] = mapped_column(primary_key=True) # Уникальный идентификатор пользователя в базе
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True) # Telegram ID пользователя (уникальный)
    course_id: Mapped[int] = mapped_column(Integer)  # Username пользователя Telegram
