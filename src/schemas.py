from pydantic import BaseModel, Field
from typing import Any, List, Dict


class SocialGroupInfo(BaseModel):
    """Модель информации о группе социальной сети."""
    id: int
    description: str
    name: str
    screen_name: str
    is_closed: int


class PostInfo(BaseModel):
    """Модель информации о посте в группе социальной сети."""
    id: int
    text: str
    likes: int
    views: int
    reposts: int


class PostInfoList(BaseModel):
    """Модель списка постов."""
    items: List[PostInfo]
