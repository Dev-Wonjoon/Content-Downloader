from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base

class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)

    posts = relationship("InstagramPost", back_populates="author")


class InstagramPost(Base):
    __tablename__ = "instagram_post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey("author.id"))
    url_id = Column(Integer, ForeignKey("url.id"))
    
    author = relationship("Author", back_populates="posts")
    url = relationship("Url", back_populates="instagram_posts")
    media_items = relationship("Media", back_populates="instagram_post")