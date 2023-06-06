# Para crear la API y manejar excepciones
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  # Para definir los modelos
from typing import Text, Optional  # Tipos de datos
from datetime import datetime  # Para manejar fechas
from uuid import uuid4 as uuid  # Para generar ids
from falcon7b import factory
from fastapi.staticfiles import StaticFiles
# Cors
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI instance
app = FastAPI()

origins = [
    "*",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000"
]

# Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Item model
class Post(BaseModel):  # Hereda de BaseModel
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    description: Optional[Text]
    published_at: Optional[datetime]
    published: Optional[bool] = False


# Array de posts
arrPosts = [
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


# Ejemplo de cómo recibir parámetros
@app.get("/posts/{id}")
def read_post(id: str):
    for post in arrPosts:
        if post['id'] == id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")


@app.post("/posts/", response_model=Post, status_code=201)  # Status code
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


# ======================================================
#            ENDPOINTS PARA EJECUTAR EL MODELO
# ======================================================

@app.get("/falcon/", response_model=str, status_code=200)
async def model_response(question: str):
    print(question)
    respuesta = await factory(question=question)
    return respuesta


# @app.get("/posts/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# Path: main.py
