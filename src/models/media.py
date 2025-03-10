from src.models.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models.association import media_tag_association

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True, autoincrement=True)
    filepath = Column(String, nullable=False)
    
    instagram_post_id = Column(Integer, ForeignKey("instagram_post.id"), nullable=True)
    youtube_video_id = Column(Integer, ForeignKey("youtube_video.id"), nullable=True)

    tags = relationship(
        "Tag",
        secondary=media_tag_association,
        back_populates="media_items"
    )