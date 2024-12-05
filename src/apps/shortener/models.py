from sqlmodel import Field

from utils.common_models import BaseModel


class ShortenedUrl(BaseModel, table=True):
    id: int = Field(primary_key=True)
    main_url: str = Field(index=True)
    short_url: str = Field(index=True)
    active: bool = Field(default=True)
    expires_at: float | None = Field()
