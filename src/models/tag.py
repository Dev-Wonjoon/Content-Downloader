from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models.base import Base
from src.models.association import media_tag_association

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(String, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    media_items = relationship(
        "Media",
        secondary=media_tag_association,
        back_populates="tags"
    )