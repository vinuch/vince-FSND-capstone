import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_name = "casting_agency"
database_path = "postgres://{}/{}".format('mac@localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
'''
def setup_db(app, database_path=database_path):
    migrate = Migrate(app, db)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Movie(db.Model):
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  attributes = Column(String)
  title = Column(String)
  release_date = Column(String)

  def __init__(self, attributes, title, release_date):
    self.attributes = attributes
    self.title = title
    self.release_date = release_date

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'attributes': self.attributes,
      'title': self.title,
      'release_date': self.release_date,
    }
  

class Actor(db.Model):
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  attributes = Column(String)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)
  
  def __init__(self, attributes, name, age, gender):
    self.attributes = attributes
    self.name = name
    self.age = age
    self.gender = gender

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'attributes': self.attributes,
      'name': self.name,
      'age': self.age,
      'gender': self.gender,
    }