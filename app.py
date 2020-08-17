import os
from flask import Flask, request, abort, jsonify, render_template, session, redirect, url_for
import json
from functools import wraps
from models import setup_db, Actor, Movie
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# from auth import AuthError, requires_auth
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode
from auth import verify_decode_jwt, check_permissions
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.secret_key = 'Theawesomedeveloper'

    oauth = OAuth(app)

    auth0 = oauth.register(
        'auth0',
        client_id='ZjMwTsC1ReuY5060zbDOSfmBgaCC6okg',
        client_secret='LLKOeGYMrDWGiX-Y651omKKpOEML0p8igVDTk_CtyvlkQ9XbdSIefNrhQLOEzYeB',
        api_base_url='https://dev-vince.us.auth0.com',
        access_token_url='https://dev-vince.us.auth0.com/oauth/token',
        authorize_url='https://dev-vince.us.auth0.com/authorize',
        client_kwargs={
            'scope': 'openid profile email',
        },
    )

    setup_db(app)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    # /server.py
    def requires_auth(permission=''):
      def requires_auth_decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
          if 'profile' not in session:
            # Redirect to Login page here
            return redirect('/')
          token = session['profile']['token']
          payload = verify_decode_jwt(token)
          check_permissions(permission, payload)
          return f(payload, *args, **kwargs)

        return decorated
      return requires_auth_decorator

    @app.route('/')
    def home():
      return render_template('home.html')
    
    @app.route('/dashboard')
    @requires_auth('delete:actors')
    def dashboard(payload):
        auth = request.headers.get('Authorization', None)
        return render_template('dashboard.html',
                              userinfo=session['profile'],
                              userinfo_pretty=json.dumps(session['jwt_payload'], indent=4))

    # Here we're using the /callback route.
    @app.route('/callback')
    def callback_handling():
        # Handles response from token endpoint
        token = auth0.authorize_access_token()
        resp = auth0.get('userinfo')
        userinfo = resp.json()
        print(token['access_token'])
       
        # Store the user information in flask session.
        session['jwt_payload'] = userinfo
        session['profile'] = {
            'user_id': userinfo['sub'],
            'name': userinfo['name'],
            'picture': userinfo['picture'],
            'token': token['access_token']
        }
        return redirect('/dashboard')
    
    # /server.py

    @app.route('/login')
    def login():
        return auth0.authorize_redirect(redirect_uri='http://127.0.0.1:5000/callback', audience='casting_agency')

    @app.route('/logout')
    def logout():
        # Clear session stored data
        session.clear()
        # Redirect user to logout endpoint
        params = {'returnTo': url_for('home', _external=True), 'client_id': 'ZjMwTsC1ReuY5060zbDOSfmBgaCC6okg'}
        return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))
        
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