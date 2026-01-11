from fastapi import FastAPI
from db import model
from db.db import engine
from routers import blog_post
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.include_router(blog_post.router)
model.Base.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory="images"),name='images')\

origins=[
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



