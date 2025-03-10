from sqlalchemy import Column, Integer, String, ForeignKey
from src.models.base import Base

class YoutubeVideo(Base):
    __tablename__ = "youtube_video"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(ForeignKey())
    filepath = Column(ForeignKey())
    created_at = Column(String)