from typing import Optional, List
from pydantic import BaseModel

class Event(BaseModel):
    id: str
    provider: str
class Article(BaseModel):
    id: int
    featured: bool
    provider: str
    title: str
    description: str
    url: str
    image: str
    published: str
    content: str
    tags: list
    launches: Optional[List[Event]] = None
    events: Optional[List[Event]] = None
