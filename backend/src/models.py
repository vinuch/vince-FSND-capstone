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
  genres = Column(String)
  title = Column(String)
  release_date = Column(String)
  cover_image = Column(String)
  description = Column(String)

  def __init__(self, attributes, title, release_date):
    self.cover_image = cover_image
    self.description = description
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
      'genres': self.genres,
      'title': self.title,
      'release_date': self.release_date,
      'cover_image': self.cover_image,
      'description': self.description,
    }
  

class Actor(db.Model):
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  attributes = Column(String)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)
  bio = Column(String)
  image = Column(String)
# INSERT INTO actors (name, age, attributes, gender, bio, image) VALUES ('Edeh Vincent', 19, 'Black, super star dev', 'M', 'Vince is a super star dev', 'https://pbs.twimg.com/profile_images/1276578899057618944/ITQ81LmF_400x400.jpg');
  
  def __init__(self, attributes, name, age, gender, bio, image):
    self.attributes = attributes
    self.name = name
    self.age = age
    self.gender = gender
    self.bio = bio
    self.image = image

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
      'bio': self.bio,
      'image': self.image,
    }