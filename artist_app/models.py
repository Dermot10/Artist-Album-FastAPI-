from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Artist(Base): 
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, unique= True, index = True)

    albums = relationship("Album", back_populates="owner")

class Album(Base): 
    __tablename__ = "albums"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, unique=True, index = True)
    genre = Column(String, index = True)
    year = Column(Integer, index = True)
    owner_id = Column(Integer, ForeignKey("artist.id"))

    owner = relationship("Artist", back_populates="albums")
