from fastapi import FastAPI, HTTPException # Para crear la API y manejar excepciones
from pydantic import BaseModel # Para definir los modelos
from typing import Text, Optional # Tipos de datos
from datetime import datetime # Para manejar fechas
from uuid import uuid4 as uuid # Para generar ids

# Item model


class Post(BaseModel): # Hereda de BaseModel
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    description: Optional[Text]
    published_at: Optional[datetime]
    published: Optional[bool] = False


arrPosts = [ # Array de posts
    {
        "id": "3eced11e-690e-4a35-93cd-b52b708d3ec7",
        "title": "Mi primer post",
        "author": "Ale",
        "content": "Ningun contenido",
        "created_at": "2023-06-04T22:58:39.627345",
        "description": "Una descripción",
        "published_at": "2023-06-05T02:05:50.038000+00:00",
        "published": False
    },
    {
        "id": "9c870416-2a0c-4f82-855e-d0cd3ebed4c4",
        "title": "Mi primer post",
        "author": "Ale",
        "content": "Ningun contenido",
        "created_at": "2023-06-04T22:58:39.627345",
        "description": "Una descripción",
        "published_at": "2023-06-05T02:05:50.038000+00:00",
        "published": False
    },
    {
        "id": "98bc0e26-7716-47d9-96fd-c1ae7b305c90",
        "title": "Mi primer post",
        "author": "Ale",
        "content": "Ningun contenido",
        "created_at": "2023-06-04T22:58:39.627345",
        "description": "Una descripción",
        "published_at": "2023-06-05T02:05:50.038000+00:00",
        "published": False
    },
    {
        "id": "b8fef744-2a56-4e37-80ac-ab9b39c5b63f",
        "title": "Mi primer post",
        "author": "Ale",
        "content": "Ningun contenido",
        "created_at": "2023-06-04T22:58:39.627345",
        "description": "Una descripción",
        "published_at": "2023-06-05T02:05:50.038000+00:00",
        "published": False
    },]

# Create FastAPI instance
app = FastAPI() 


@app.get("/posts/")
def read_posts():
    return arrPosts


@app.get("/posts/{id}") # Path parameter
def read_post(id: str):
    for post in arrPosts:
        if post['id'] == id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")


@app.post("/posts/", response_model=Post, status_code=201) # Status code
async def create_post(post: Post):
    post.id = str(uuid())
    arrPosts.append(post.dict())
    return [{'message': 'Post received'}, {'data': arrPosts}]


@app.delete("/posts/{id}")
async def delete_post(id: str):
    for post in arrPosts:
        if post['id'] == id:
            arrPosts.remove(post)
            return [{'message': 'Post deleted', 'data': arrPosts}]
    raise HTTPException(status_code=404, detail="Post not found")


@app.put("/posts/{id}")
async def update_post(id: str, post: Post):
    for i in range(len(arrPosts)):
        if arrPosts[i]['id'] == id:
            arrPosts[i] = post.dict()
            return [{'message': 'Post updated', 'data': arrPosts}]
    raise HTTPException(status_code=404, detail="Post not found")

# @app.get("/posts/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# Path: main.py