import random
import shutil
import string

from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm.session import Session
from db import db_post
from db.db import get_db
from routers.schemas import PostBase

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

@router.post("/")
def post_blog(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create_post(request,db)

@router.get("/all")
def get_all_posts(db: Session = Depends(get_db)):
    return db_post.get_posts(db)

@router.delete("/{id}")
def delete_post(id: int, db:Session = Depends(get_db)):
    return db_post.delete_post(id,db)

@router.post("/image")
def upload_image(image: UploadFile = File(...)):
    letter=string.ascii_lowercase
    rand_str="".join(random.choice(letter) for _ in range(6))
    new =f'_{rand_str}.'
    filename=new.join(image.filename.rsplit('.',1))
    path = f'images/{filename}'

    with open(path,'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename':path}