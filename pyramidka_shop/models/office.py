from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text
)

from .meta import Base


class Office(Base):
    __tablename__ = 'offices'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    adr = Column(Text)


class OfficeHandler:
    def __init__(self, office: Office):
        self.name = office.name
        self.adr = office.adr
        self.link = "https://www.google.ru/maps/search/" + office.adr.replace(' ', '+')


Index('my_index', Office.adr, unique=True, mysql_length=255)
