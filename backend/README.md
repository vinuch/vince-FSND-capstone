# Casting Agency Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


### API endpoint Docs


##### GET '/actors'

- Fetches all actors
- Request Parameters: None
- Returns
```
{
  "actors": [
    {
      "age": 19,
      "attributes": "Black, super star dev",
      "bio": "Vince is a super star dev and him go make am very soon",
      "gender": "M",
      "id": 7,
      "image": "https://pbs.twimg.com/profile_images/1276578899057618944/ITQ81LmF_400x400.jpg",
      "name": "Vince{} 👾"
    },
    ....
    {
      "age": 21,
      "attributes": "genius, smart, badass",
      "bio": "This guy na oga for this work we dey look up to am but e no know",
      "gender": "M",
      "id": 10,
      "image": "https://pbs.twimg.com/profile_images/1147562733732278272/4D5XpoDK_400x400.jpg",
      "name": "Vicradon"
    },
  ],
  "success": true
}
```

##### POST '/actors'

- Creates new actor
- request parameters: None
- returns
```
{
  'success': True,
  'new': [
    {
      "age": 19,
      "attributes": "Black, super star dev",
      "bio": "Vince is a super star dev and him go make am very soon",
      "gender": "M",
      "id": 7,
      "image": "https://pbs.twimg.com/profile_images/1276578899057618944/ITQ81LmF_400x400.jpg",
      "name": "Vince{} 👾"
    },
    ....
    {
      "age": 21,
      "attributes": "genius, smart, badass",
      "bio": "This guy na oga for this work we dey look up to am but e no know",
      "gender": "M",
      "id": 10,
      "image": "https://pbs.twimg.com/profile_images/1147562733732278272/4D5XpoDK_400x400.jpg",
      "name": "Vicradon"
    },
  ]
}
```

##### PATCH '/actors/int:id'

- updates actor with id in url
- returns
```
{
  'success': True,
  'updated': [
    {
      "age": 19,
      "attributes": "Black, super star dev",
      "bio": "Vince is a super star dev and him go make am very soon",
      "gender": "M",
      "id": 7,
      "image": "https://pbs.twimg.com/profile_images/1276578899057618944/ITQ81LmF_400x400.jpg",
      "name": "Vince{} 👾"
    },
    ....
    {
      "age": 21,
      "attributes": "genius, smart, badass",
      "bio": "This guy na oga for this work we dey look up to am but e no know",
      "gender": "M",
      "id": 10,
      "image": "https://pbs.twimg.com/profile_images/1147562733732278272/4D5XpoDK_400x400.jpg",
      "name": "Vicradon"
    },
  ]
}
```

##### DELETE '/actors/int:question_id'

- Deletes actor with id in url
- returns
```
{
  'success': True,
  'delete': id
}
```

##### GET '/movies' 
- Fetches all movies
- request Parameters: none
- returns
```
{
  "movies": [
    {
      "cover_image": "https://images-na.ssl-images-amazon.com/images/I/710djTBQ8dL._AC_SY679_.jpg",
      "description": "Thor: Ragnarok is a 2017 American superhero film based on the Marvel Comics character Thor, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures. ... In Thor: Ragnarok, Thor must escape the alien planet Sakaar in time to save Asgard from Hela and the impending Ragnarök.",
      "genres": "action, thriller",
      "id": 14,
      "release_date": "10-08-2020",
      "title": "Thor Ragnarok"
    },
    .....
    {
      "cover_image": "https://www.naijaloaded.com.ng/wp-content/uploads/2020/02/Again-Wande-Coal-art.jpg",
      "description": "this is a shady description",
      "genres": "suspense",
      "id": 20,
      "release_date": "2020",
      "title": "Far from home"
    }
  ],
  "success": true
}
```

##### POST '/movies'

- Creates new movie
- request parameters: None
- returns
```
{
  'success': True,
  'new': [
    {
      "cover_image": "https://images-na.ssl-images-amazon.com/images/I/710djTBQ8dL._AC_SY679_.jpg",
      "description": "Thor: Ragnarok is a 2017 American superhero film based on the Marvel Comics character Thor, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures. ... In Thor: Ragnarok, Thor must escape the alien planet Sakaar in time to save Asgard from Hela and the impending Ragnarök.",
      "genres": "action, thriller",
      "id": 14,
      "release_date": "10-08-2020",
      "title": "Thor Ragnarok"
    },
    .....
    {
      "cover_image": "https://www.naijaloaded.com.ng/wp-content/uploads/2020/02/Again-Wande-Coal-art.jpg",
      "description": "this is a shady description",
      "genres": "suspense",
      "id": 20,
      "release_date": "2020",
      "title": "Far from home"
    }
  ]
}
```


##### PATCH '/movies/int:id'

- updates movie with id in url
- returns
```
{
  'success': True,
  'updated': [
    {
      "cover_image": "https://images-na.ssl-images-amazon.com/images/I/710djTBQ8dL._AC_SY679_.jpg",
      "description": "Thor: Ragnarok is a 2017 American superhero film based on the Marvel Comics character Thor, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures. ... In Thor: Ragnarok, Thor must escape the alien planet Sakaar in time to save Asgard from Hela and the impending Ragnarök.",
      "genres": "action, thriller",
      "id": 14,
      "release_date": "10-08-2020",
      "title": "Thor Ragnarok"
    },
    .....
    {
      "cover_image": "https://www.naijaloaded.com.ng/wp-content/uploads/2020/02/Again-Wande-Coal-art.jpg",
      "description": "this is a shady description",
      "genres": "suspense",
      "id": 20,
      "release_date": "2020",
      "title": "Far from home"
    }
  ]
}
```

##### DELETE '/movies/int:question_id'

- Deletes movie with id in url
- returns
```
{
  'success': True,
  'delete': id
}
```

## Testing
To run the tests, run
```
dropdb casting_agency
createdb casting_agency
psql casting_agency < casting_agency.psql
python test_app.py
```