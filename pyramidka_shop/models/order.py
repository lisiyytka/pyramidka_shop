from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text
)

from .meta import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    phone = Column(Text)
    tea_list = Column(Text)
    price = Column(Integer)


Index('my_index', Order.name, unique=True, mysql_length=255)
