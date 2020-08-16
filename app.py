import os
from flask import Flask, request, abort, jsonify
from models import setup_db, Actor, Movie
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/actors', methods=['GET', 'POST', 'DELETE'])
    def get_actors():
      if request.method == 'GET':
        actors_selection = Actor.query.all()
        actors = [actors.format() for actors in actors_selection]

        return jsonify({
            'success': True,
            'actors': actors
          
        })
      elif request.method == 'POST':
        res = request.get_json()
        attributes = res.get('attributes', None)
        name = res.get('name', None)
        age = res.get('age', None)
        gender = res.get('gender', None)
        try:
          new_actor = Actor(attributes=attributes, name=name, age=age, gender=gender)
          new_actor.insert()
          actors_selection = Actor.query.all()
          actors = [actors.format() for actors in actors_selection]

          return jsonify({
            'success': True,
            'new': actors
          })
        except:
          abort(401)


    @app.route('/movies', methods=['GET', 'POST'])
    def handle_movies():
      if request.method == 'GET':
        movies_selection = Movie.query.all()
        movies = [movies.format() for movies in movies_selection]
        print(request.method)
        return jsonify({
            'success': True,
            'movies': movies
          
        })
      elif request.method == 'POST':
        res = request.get_json()
        attributes = res.get('attributes', None)
        title = res.get('title', None)
        release_date = res.get('release_date', None)
        try:
          new_movie = Movie(attributes=attributes, title=title, release_date=release_date)
          new_movie.insert()
          movies_selection = Movie.query.all()
          movies = [movies.format() for movies in movies_selection]

          return jsonify({
            'success': True,
            'new': movies
          })
        except:
          abort(401)

    @app.route('/movies/<int:id>', methods=['GET', 'DELETE'])
    def handle_single_movie(id):
      movie_selection = Movie.query.filter_by(id=id).one_or_none()
      movie = movie_selection.format()

      if request.method == 'GET':
        print(movie)
        return jsonify({
            'success': True,
            'movie': movie
          
        })
      elif request.method == 'DELETE':
        try:
          movie_selection.delete()
          return jsonify({
            'success': True,
            'method': 'DELETE',
            'id': movie['id']
          })
        except:
          abort(401)
  

    return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)