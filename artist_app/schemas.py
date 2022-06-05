from pydantic import BaseModel
from typing import List, Union


class Album(BaseModel):
    name: str
    genre: str
    year: Union[int, None] = None


class UpdateAlbum(BaseModel):
    name: Union[str, None] = None
    genre: Union[str, None] = None
    year: Union[int, None] = None
