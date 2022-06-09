from sqlalchemy.orm import Session
from . import models,  schemas
from .schemas import ArtistCreate, AlbumCreate

def get_artist(db: Session, artist_id: int): 
    return db.query(models.Artist).filter(models.Artist.id == artist_id).first()

def get_artist_by_name(db: Session, artist_name:str): 
    return db.query(models.Artist).filter(models.Artist.name == artist_name).first()

def get_artists(db: Session, skip: int =0, limit: int =100): 
    return db.query(models.Artist).offset(skip).limit(limit).all()

def create_artist(db: Session, artist: ArtistCreate):
    db_artist = models.Artist(name= artist.name)
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def delete_artist(db:Session, artist_id: int): 
    db_artist_to_delete = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    try: 
        if not db_artist_to_delete:
            return  "album ID does not exist"
    except: 
        db.delete(db_artist_to_delete)
        db.commit()
        return {"Artist Deleted": True}

def get_albums(db: Session, skip: int= 0, limit: int=100): 
    return db.query(models.Album).offset(skip).limit(limit).all()

def get_album_by_name(db: Session, album_title:str): 
     return db.query(models.Album).filter(models.Album.title == album_title).first()

def create_artist_album(db:Session, album: AlbumCreate, artist_id: int):
    db_album = models.Album(**album.dict(), owner_id=artist_id)
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album


def update_album(db:Session, album_id: int):
    db_album_to_update = db.query(models.Album).filter(models.Album.id == album_id).first()
    try: 
        if not db_album_to_update: 
            return "album ID does not exist"
    except: 
        db.update(db_album_to_update)
        db.commit()
        db.refresh(db_album_to_update)
        return db_album_to_update

def delete_album(db:Session, album_id: int): 
    db_album_to_delete = db.query(models.Album).filter(models.Album.id == album_id).first()
    try: 
        if not db_album_to_delete:
            return  "album ID does not exist"
    except: 
        db.delete(db_album_to_delete)
        db.commit()
        return {"Album Deleted": True}