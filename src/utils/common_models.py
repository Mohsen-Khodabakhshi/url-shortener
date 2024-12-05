from datetime import datetime

from sqlmodel import SQLModel, Field


class BaseModel(SQLModel):
    __abstract__ = True

    created_at: float = Field(
        default_factory=lambda: datetime.timestamp(datetime.utcnow())
    )
    updated_at: float | None = Field(
        nullable=True,
        default_factory=lambda: datetime.timestamp(datetime.utcnow()),
        sa_column_kwargs={
            "onupdate": lambda: datetime.timestamp(datetime.utcnow()),
        },
    )
