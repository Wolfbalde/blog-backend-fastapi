from fastapi import Depends, HTTPException
from sqlalchemy.orm.session import Session

from db.model import DbPost
from routers.schemas import PostBase
import datetime


def create_post(request: PostBase, db: Session):
    new_post = DbPost(
        title=request.title,
        content=request.content,
        timestamp=datetime.datetime.now(),
        image_url=request.image_url,
        creator=request.creator
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_posts(db: Session):
    return db.query(DbPost).all()

def delete_post(id: int, db: Session):
    post=db.query(DbPost).filter(DbPost.id==id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Not Found")

    db.delete(post)
    db.commit()
    return "ok"
