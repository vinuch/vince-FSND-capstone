import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie, db


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency"
        self.database_path = "postgres://{}/{}".format('mac@localhost:5432', self.database_name)
        self.headers = {'Content-Type': 'application/json', 'Authorization': ' Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhESDN2QzhGQkJxMjNGdkZ1N1l2bCJ9.eyJpc3MiOiJodHRwczovL2Rldi12aW5jZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY0MGY1OWJmZTQ1MjcwMDZkOTNhZDA5IiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE1OTg0ODM0MjgsImV4cCI6MTU5ODQ5MDYyOCwiYXpwIjoiWmpNd1RzQzFSZXVZNTA2MHpiRE9TZm1CZ2FDQzZva2ciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllcyJdfQ.yY5Yqpv8asB4wZxL5ViZiJ66uttXwy_QypZjJRWwJPL-fYwCoMLJHztXL38ouIC9nrE5BVNYYHO3u151K89iHPSpeiq2LcvDTK3_13PJ-SVziKk9OGEAZDDClVVioukgprfB_1h5IRzaIHA0Ej1J6xYBF-lPU4P_2YvszUxWlzlfRYoB6NKvJaK3TDH4PxHWJ5VG8LzchSNAEXmz3r38xp2dZKwsvcgbH6YM964bgFx_S7fUXRPjNE6MkYOhnPMxxOpR7MKsUWzKVRlOlW9PFjLobNQB3z2v4N1FbUkApSNHJQQO_Y843sT1MYuVAhf-TeaBEeWA7xLfZsckjk8XMQ'}
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_actors_with_token(self):
        res = self.client().get('/actors', headers=self.headers)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_actors_without_token(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_patch_actor_with_token(self):
        res = self.client().patch('/actors/7', headers=self.headers, json={
          "attributes" : "boring, test",
          "name" : "new test name",
          "age" : 40,
          "gender" : "M",
          "bio" : "this is a test bio",
          "image" : "https://pbs.twimg.com/profile_images/1284932516344926211/ONltY7nU_400x400.jpg"
        })
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    def test_patch_actor_error(self):
        res = self.client().patch('/actors/1', headers=self.headers, json={})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_post_actor_with_token(self):
        res = self.client().post('/actors', headers=self.headers, json={
          "attributes" : "boring, test",
          "name" : "Dillion Megida",
          "age" : 40,
          "gender" : "M",
          "bio" : "this is a test bio",
          "image" : "https://pbs.twimg.com/profile_images/1239530354454790144/eYVvZ06d_400x400.jpg"
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new'])

    def test_post_actor_error(self):
        res = self.client().post('/actors', headers=self.headers, json={})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
 
    def test_delete_actor_with_token(self):
        res = self.client().delete('/actors/10', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_delete_actor_error(self):
        res = self.client().delete('/actors/1', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

# TEST MOVIE ENDPOINTS

    def test_get_movies_with_token(self):
        res = self.client().get('/movies', headers=self.headers)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_movies_without_token(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        
    def test_patch_movie_with_token(self):
        res = self.client().patch('/movies/14', headers=self.headers, json={
          "genres" : "suspense",
          "release_date" : "2020",
          "description" : "this is a shady description",
          "title" : "Far from home",
          "image" : "https://www.naijaloaded.com.ng/wp-content/uploads/2020/02/Again-Wande-Coal-art.jpg",
        })
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    def test_patch_movie_error(self):
        res = self.client().patch('/movies/1', headers=self.headers, json={})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_post_movie_with_token(self):
        res = self.client().post('/movies', headers=self.headers, json={
          "genres" : "suspense",
          "release_date" : "2020",
          "description" : "this is a shady description",
          "title" : "Far from home",
          "image" : "https://www.naijaloaded.com.ng/wp-content/uploads/2020/02/Again-Wande-Coal-art.jpg",
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_post_movie_error(self):
        res = self.client().post('/movies', headers=self.headers, json={})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
 
    def test_delete_movie_with_token(self):
        res = self.client().delete('/movies/16', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_delete_movie_error(self):
        res = self.client().delete('/movies/500', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
  

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()