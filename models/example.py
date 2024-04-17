from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Example(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    author: str
    year: int
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    is_published: bool = Field(default=True)