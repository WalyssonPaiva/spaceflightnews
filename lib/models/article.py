from typing import Optional, List
from pydantic import BaseModel

class Event(BaseModel):
    id: str
    provider: str
class Article(BaseModel):
    id: Optional[int] = None
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    updatedAt: str
    featured: bool
    launches: Optional[List[Event]] = None
    events: Optional[List[Event]] = None
