from db.db import Base
from sqlalchemy import Column,Integer,String,DateTime

class DbPost(Base):
    __tablename__ = "post"
    id=Column(Integer,primary_key=True,index=True)
    image_url=Column(String)
    content=Column(String)
    title=Column(String)
    creator=Column(String)
    timestamp=Column(DateTime)

