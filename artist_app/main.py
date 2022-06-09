from fastapi import FastAPI, HTTPException, Query, Path, Depends
from sqlalchemy.orm import Session
from typing import Union, List 
from .database import SessionLocal, engine
from . import crud, models, schemas
import psycopg2


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db(): 
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()


@app.post("/artists/", response_model=schemas.Artist, status_code=201)
def create_artist(artist: schemas.ArtistCreate, db:Session = Depends(get_db)):
    db_artist = crud.create_artist(db=db, artist=artist)
    if db_artist: 
        return f"Succes {db_artist} created"
    raise HTTPException(status_code=400, detail= "Artist already exists") 

@app.get("/", response_model=List[schemas.Artist])
def read_artists(skip: int = 0, limit = 100, db: Session = Depends(get_db)):
    artists = crud.get_artists(db, skip=skip, limit=limit)
    return artists

@app.get("/artist/{artist_id}", response_model=schemas.Artist)
def read_artist(artist_id: int, db : Session = Depends(get_db)): 
    db_artist = crud.get_artist(db, artist_id= artist_id)
    if db_artist is None: 
        raise HTTPException(status=404, detail="Artist not found in database")
    return db_artist

@app.get("/artist/{artist_name}", response_model=schemas.Artist)
def read_artist_by_name(artist_name:str, db: Session = Depends(get_db)): 
    db_artist = crud.get_artist_by_name(db, artist_name= artist_name)
    if db_artist is None: 
        raise HTTPException(status=404, detail="Artist not found in database")
    return  db_artist


@app.delete("/delete-artist/{artist_id}")
def delete_artist(artist_id: int = Query(..., description="The artist ID to delete"), db: Session = Depends(get_db)):
    artist = crud.delete_artist(db, artist_id = artist_id)
    if not artist:
        raise HTTPException(
            status_code=400, detail="artist ID does not exists")

    return {"Success": "Artist Deleted"}




@app.post("/artists/{artist_id}/albums/", response_model= schemas.Album)
def create_album(artist_id: int, album: schemas.AlbumCreate, db:Session = Depends(get_db)): 
    return crud.create_artist_album(db=db, album=album, artist_id=artist_id)

@app.get("/albums/", response_model= List[schemas.Album])
def read_albums(skip: int =0, limit: int = 100, db : Session = Depends(get_db)): 
    albums = crud.get_albums(db, skip=skip, limit =limit)
    return albums

@app.get("/albums/{album_title}", response_model= schemas.Album)
def read_album_name(album_title: str, db: Session = Depends(get_db)): 
    album = crud.get_album_by_name(db, album_title = album_title)
    return album

@app.put("/update-album/{album_id}", response_model=schemas.Album)
def update_album(album_id: int, album: schemas.UpdateAlbum, db: Session = Depends(get_db)):
    album = crud.update_album(db, album_id= album_id)
    if album_id is None: 
        raise HTTPException(
            status_code=400, detail="album ID does not exists")
    return album 


@app.delete("/delete-album/{album_id}")
def delete_album(album_id: int = Query(..., description="The album ID to delete"), db: Session = Depends(get_db)):
    album = crud.delete_album(db, album_id = album_id)
    if not album:
        raise HTTPException(
            status_code=400, detail="album ID does not exists")

    return {"Success": "Item Deleted"}
