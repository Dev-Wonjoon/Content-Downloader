from sqlalchemy import Table, Column, Integer, ForeignKey, String
from src.models.base import Base

media_tag_association = Table(
    'media_tag_association',
    Base.metadata,
    Column('media_id', Integer, ForeignKey('media.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)