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
        self.database_name = "test_casting_agency"
        self.database_path = "postgres://{}/{}".format('mac@localhost:5432', self.database_name)
        self.headers = {'Content-Type': 'application/json', 'Authorization': ' Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhESDN2QzhGQkJxMjNGdkZ1N1l2bCJ9.eyJpc3MiOiJodHRwczovL2Rldi12aW5jZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY0MGY1OWJmZTQ1MjcwMDZkOTNhZDA5IiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE1OTgzMDg1MzAsImV4cCI6MTU5ODMxNTczMCwiYXpwIjoiWmpNd1RzQzFSZXVZNTA2MHpiRE9TZm1CZ2FDQzZva2ciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllcyJdfQ.J9aIVIBKxh97m4FweTobe3djjs21-fyOv-ULoLEnEHY6RnSF7udgt4N7LHUti5PtihURZl-8UtuQpUysagvRg7JK4tGPxmPB5VHfpKUeWO09Y8xKHAmH15jToRu3BVV8sPO7q_ay4JvYKWQIcDaGxn77G2GxysPN8pK63my4z--nOJ3rLYVIRhgBqz0u9rAVKh7Ybd2GsLtQ8m3OtCqxVAmW0M4KfxcdlF4do2AefKaw8mhQZzL4W4IM9mKLOsMF0Cfbg9th-bAK-zL8m9XOlMldF_G8tRkwtfenPWEVbk1O1Hu3U-2cjLYgjKCfnHWybQdXGonMKCMiPqIQ3g01mA'}
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