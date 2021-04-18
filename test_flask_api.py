import os
import unittest
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, abort, jsonify
from src.api import app
from src.database.models import setup_db, db_drop_and_create_all
load_dotenv()

executive_token = os.environ['EXECUTIVE_TOKEN']
director_token = os.environ['DIRECTOR_TOKEN']
assistant_token = os.environ['ASSISTANT_TOKEN']

headers = {'Authorization': f'Bearer {executive_token}'}

base_url = 'https://www.normuradov.com/assets/casting-agency'


class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.database_name = "casting_agency_testing"
        self.database_path = "postgresql://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            db_drop_and_create_all()

    def test_get_movies(self):
        response = self.client().get(
            '/movies', headers=headers)

        self.assertEqual(response.status_code, 200)

        json_data = response.get_json()
        self.assertIsNotNone(json_data['movies'])

    def test_get_single_movie(self):
        response = self.client().get(
            '/movies/1',
            headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_post_movie_create(self):
        movie = {'title': 'Godfather II',
                 'release_date': '1973-01-01',
                 'poster_url': f'{base_url}/the_godfather.png'}
        response = self.client().post('/movies',
                                      json=movie,
                                      headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_patch_movie_update(self):
        response = self.client().patch('/movies/1',
                                       json={'title': 'Godfather...'},
                                       headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_movie(self):
        response = self.client().delete(
            '/movies/1',
            headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_get_actors(self):
        response = self.client().get(
            '/actors', headers=headers)

        self.assertEqual(response.status_code, 200)

        json_data = response.get_json()
        self.assertIsNotNone(json_data['actors'])

    def test_get_single_actor(self):
        response = self.client().get(
            '/actors/1',
            headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_post_actor_create(self):
        actor = {'name': 'Nickolas Cage',
                 'date_of_birth': '1963-01-01',
                 'gender': 'M',
                 'picture_url': f'{base_url}/the_godfather.png'}
        response = self.client().post('/actors',
                                      json=actor,
                                      headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_patch_actor_update(self):
        response = self.client().patch('/actors/1', json={'name': '-'},
                                       headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_actors(self):
        response = self.client().delete(
            '/actors/1',
            headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_get_non_existing_endpoint(self):
        response = self.client().get('/non-existing-endpoint')
        self.assertEqual(response.status_code, 404)

    def test_not_allowed_method(self):
        response = self.client().delete('/movies')
        self.assertEqual(response.status_code, 405)

    def test_not_authorized(self):
        response = self.client().get('/movies')
        self.assertEqual(response.status_code, 401)

    def test_bad_request(self):
        response = self.client().post('/actors',
                                      json={'name': 'Nickolas Cage'},
                                      headers=headers)
        self.assertEqual(response.status_code, 400)

    def test_assistant_can_get_movies(self):
        response = self.client().get(
            '/movies', headers={'Authorization': f'Bearer {assistant_token}'})

        self.assertEqual(response.status_code, 200)

    def test_assistant_can_get_actors(self):
        response = self.client().get(
            '/actors', headers={'Authorization': f'Bearer {assistant_token}'})

        self.assertEqual(response.status_code, 200)

    def test_assistant_can_not_delete_movie(self):
        response = self.client().delete(
            '/movies/1',
            headers={'Authorization': f'Bearer {assistant_token}'})
        self.assertEqual(response.status_code, 403)

    def test_director_can_get_movies(self):
        response = self.client().get(
            '/movies', headers={'Authorization': f'Bearer {director_token}'})

        self.assertEqual(response.status_code, 200)

    def test_director_can_not_delete_movie(self):
        response = self.client().delete(
            '/movies/1', headers={'Authorization': f'Bearer {director_token}'})
        self.assertEqual(response.status_code, 403)

    def test_executive_can_get_movies(self):
        response = self.client().get(
            '/movies', headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_executive_can_delete_movie(self):
        response = self.client().delete(
            '/movies/1',
            headers=headers)
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
