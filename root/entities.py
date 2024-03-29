from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import TIMESTAMP
import datetime

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    username = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    first_name = Column(String)
    second_name = Column(String)


class Messenger(Base):
    __tablename__ = 'messenger'
    messenger_id = Column(Integer, primary_key=True)
    messenger_name = Column(String, nullable=False)


class User_messengers(Base):
    __tablename__ = 'user_messengers'
    user_messenger_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    messenger = Column(Integer, nullable=False)


class Message(Base):
    __tablename__ = 'message'
    messege_id = Column(Integer, primary_key=True)
    recipient = Column(String, nullable=False)
    sender = Column(String, nullable=False)
    date_sent = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    messenger = Column(Integer)
    content = Column(String, nullable=False)
    catagory = Column(String)


class Clicks(Base):
    __tablename__ = 'clicks'
    click_id = Column(Integer, primary_key=True)
    date_click = Column(TIMESTAMP, nullable=False)
    message = Column(Integer, nullable=False)


class Catagory(Base):
    __tablename__ = 'catagory'
    catagory_name = Column(String, primary_key=True)
    population = Column(Integer)
