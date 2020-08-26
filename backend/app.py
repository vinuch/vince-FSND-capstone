import os
from flask import Flask, request, abort, jsonify, render_template, session, redirect, url_for
import json
from functools import wraps
from models import setup_db, Actor, Movie
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from auth import verify_decode_jwt, check_permissions
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.secret_key = 'Theawesomedeveloper'

    setup_db(app)
    cors = CORS(app, resources={r"*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def home():
        return render_template('home.html')


    @app.route('/actors', methods=['GET', 'POST', 'PATCH', 'DELETE'])
    @requires_auth('get:actors')
    def get_actors(payload):
        if request.method == 'GET':
            actors_selection = Actor.query.all()
            actors = [actors.format() for actors in actors_selection]

            return jsonify({
                'success': True,
                'actors': actors

            })
        elif request.method == 'POST':
            res = request.get_json()
            if (not res):
                abort(422)

            attributes = res.get('attributes', None)
            name = res.get('name', None)
            age = res.get('age', None)
            gender = res.get('gender', None)
            bio = res.get('bio', None)
            image = res.get('image', None)
            # print(attributes)
            try:
                new_actor = Actor(attributes=attributes, name=name,
                                  age=age, gender=gender, bio=bio, image=image)
                new_actor.insert()
                actors_selection = Actor.query.all()
                actors = [actors.format() for actors in actors_selection]

                return jsonify({
                    'success': True,
                    'new': actors
                })
            except:
                abort(422)

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_single_actor(payload, id):
        res = request.get_json()
        if (not res):
            abort(422)

        attributes = res.get('attributes', None)
        name = res.get('name', None)
        age = res.get('age', None)
        gender = res.get('gender', None)
        bio = res.get('bio', None)
        image = res.get('image', None)
        try:
            current_actor = Actor.query.get(id)
            current_actor.name = name
            current_actor.age = age
            current_actor.gender = gender
            current_actor.bio = bio
            current_actor.image = image

            current_actor.update()
            actors_selection = Actor.query.all()
            actors = [actors.format() for actors in actors_selection]

            return jsonify({
                'success': True,
                'updated': actors
            })
        except:
          abort(422)

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_single_actor(payload, id):
        try:
            actor_to_delete = Actor.query.get(id)
            actor_to_delete.delete()

            return jsonify({
                'success': True,
                'delete': id
            })
        except:
            abort(422)

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
      if request.method == 'GET':
            movies_selection = Movie.query.all()
            movies = [movies.format() for movies in movies_selection]
            return jsonify({
                'success': True,
                'movies': movies

            })


    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(payload):
      if request.method == 'POST':
        res = request.get_json()
        if not res: 
          abort(422)
        cover_image = res.get('image', None)
        title = res.get('title', None)
        release_date = res.get('release_date', None)
        description = res.get('description', None)
        genres = res.get('genres', None)

        try:
            new_movie = Movie(title=title, release_date=release_date,
                              description=description, genres=genres, cover_image=cover_image)
            new_movie.insert()
            movies_selection = Movie.query.all()
            movies = [movies.format() for movies in movies_selection]

            return jsonify({
                'success': True,
                'movies': movies
            })
        except:
            abort(401)

    @app.route('/movies/<int:id>', methods=['GET'])
    @requires_auth('get:movies')
    def get_single_movie(payload, id):
      movie_selection = Movie.query.filter_by(id=id).one_or_none()
      movie = movie_selection.format()

      if request.method == 'GET':
          return jsonify({
              'success': True,
              'movie': movie

          })


    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_single_movie(payload, id):
      res = request.get_json()
      if (not res):
          abort(422)

      title = res.get('title', None)
      description = res.get('description', None)
      release_date = res.get('release_date', None)
      genres = res.get('genres', None)
      image = res.get('image', None)
      try:
          current_movie = Movie.query.get(id)
          current_movie.title = title
          current_movie.description = description
          current_movie.release_date = release_date
          current_movie.genres = genres
          current_movie.image = image

          current_movie.update()
          movies_selection = Movie.query.all()
          movies = [movies.format() for movies in movies_selection]

          return jsonify({
              'success': True,
              'updated': movies
          })
      except:
          abort(422)
      
  
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_single_movie(payload, id):
      try:
          movie_to_delete = Movie.query.get(id)
          movie_to_delete.delete()

          return jsonify({
              'success': True,
              'delete': id
          })
      except:
          abort(422)

    @app.errorhandler(401)
    def Unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
          "success": False, 
          "error": 422,
          "message": "unprocessable"
        }), 422


    @app.errorhandler(404)
    def not_found(error):
      return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not Found"
      }), 404



    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code
        
        
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
