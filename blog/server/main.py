from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import date
from deta import Deta


app = FastAPI()

api_key = 'SECRET_KEY'

deta = Deta(api_key)
db = deta.Base('blogDB')


class Blog(BaseModel):
    title: str
    content: str


@app.get("/")
async def test():
    return "This is home page. Visiting at: " + str(date.today())


@app.get("/blogs")
async def get_blogs():
    blogs = db.fetch()
    return blogs


@app.get("/blog/{key}")
async def get_blog(key: str):
    blog = db.get(key)
    return blog if blog else {{"error": "Not found"}, 404}


@app.post("/blog", status_code=201)
async def create_new_blog(blog: Blog):
    today = date.today()

    b = {
        "key": blog.title,
        "content": blog.content,
        "date": "Created: " + str(today),
    }

    db.put(b)
    return b


@app.patch("/blog/{key}")
async def update_blog(key: str, blog: Blog):
    today = date.today()
    b = {
        "key": blog.title,
        "content": blog.content,
        "date": "Updated: " + str(today),
    }

    try:
        db.update(b, key)
        return ({"success": "updated"}, 201)
    except Exception:
        return ({"error": "Not found"}, 404)


@app.delete("/blog/{key}")
async def delete_blog(key: str):
    try:
        db.delete(key)
        return ({"success": "deleted"}, 201)
    except Exception:
        return ({"error": "Not found"}, 404)
        