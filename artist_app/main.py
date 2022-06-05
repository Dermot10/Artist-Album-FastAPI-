from fastapi import FastAPI, HTTPException, Query, Path
from typing import Union
from . import schemas

app = FastAPI()

album_collection = {}


@app.get("/get-album/{album_id}")
def get_album(album_id: int = Path(None, description="The ID of the album")):
    return album_collection[album_id]


@app.get("/get-album-name/")
def get_album(name: Union[str, None] = None):
    for album_id in album_collection:
        if album_collection[album_id].name == name:
            return album_collection[album_id]
        return {"Data": "Not found"}


@app.post("/create-album/{album_id}")
def create_album(album_id: int, album: schemas.Album):
    if album_id in album_collection:
        raise HTTPException(status_code=400, detail="album ID already exists")
    album_collection[album_id] = album
    return album_collection[album_id]


@app.put("/update-album/{album_id}")
def update_album(album_id: int, album: schemas.UpdateAlbum):
    if album_id not in album_collection:
        raise HTTPException(
            status_code=400, detail="album ID does not exists")
    if album.name != None:
        album_collection[album_id].name = album.name

    if album.genre != None:
        album_collection[album_id].genre = album.genre

    if album.year != None:
        album_collection[album_id].year = album.year

    return album_collection[album_id]


@app.delete("/delete-album/")
def delete_album(album_id: int = Query(..., description="The album ID to delete")):
    if album_id not in album_collection:
        raise HTTPException(
            status_code=400, detail="album ID does not exists")

    del album_collection[album_id]
    return {"Success": "Item Deleted"}
