from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
import datetime


Base = declarative_base()


class IDModelMixin:
    id = Column(Integer, primary_key=True, nullable=False)


class DateTimeModelMixin:
    create_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    update_at = Column(DateTime, default=datetime.datetime.now(), nullable=False, onupdate=datetime.datetime.now())
