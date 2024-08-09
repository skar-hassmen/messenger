from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import declared_attr

from utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    __absract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{camel_case_to_snake_case(cls.__name__)}s'