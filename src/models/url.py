from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.models.base import Base

class Url(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True, autoincrement=True)
    path = Column(String, nullable=False)

    instagram_posts = relationship("InstagramPost", back_populates="url")
    youtube_videos = relationship("YoutubeVideo", back_populates="url")