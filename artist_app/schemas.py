from datetime import datetime
from turtle import title
from pydantic import BaseModel
from typing import List, Union


class AlbumBase(BaseModel):
    title: str 
    genre : Union[str, None] = None

class AlbumCreate(AlbumBase):
    pass 
    
class Album(AlbumBase):
    id: int
    year: Union[int, None] = None
    owner_id: int 

    class Config: 
        orm_mode = True 

class UpdateAlbum(BaseModel):
    title: Union[str, None] = None
    genre: Union[str, None] = None
    year: Union[int, None] = None


class ArtistBase(BaseModel):
    name: str 

class ArtistCreate(ArtistBase): 
    pass

class Artist(ArtistBase): 
    id: Union[int, None] = None
    created_at: Union[datetime, None] = None
    albums : List[Album] = [] 

    class Config: 
        orm_mode = True 
