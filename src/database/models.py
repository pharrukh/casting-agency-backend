import os
from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import date
from dotenv import load_dotenv

load_dotenv()
database_name = os.environ['DATABASE_NAME']
user_name = os.environ['USER_NAME']
user_password = os.environ['USER_PASSWORD']
server_host = os.environ['SERVER_HOST']

database_path_default = "postgresql://{}/{}".format(
    f'{user_name}:{user_password}@{server_host}:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path_default):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''


def db_drop_and_create_all():
    base_url = 'https://www.normuradov.com/assets/casting-agency'
    db.drop_all()
    db.create_all()
    movie = Movie(
        title='The Godfather',
        poster_url=f'{base_url}/the_godfather.png',
        release_date='1972-03-24'
    )
    movie.insert()
    actor_one = Actor(
        name='Marlon Brando',
        picture_url=f'{base_url}/marlon_brando.png',
        gender='M',
        date_of_birth='1924-04-03'
    )
    actor_one.insert()
    actor_two = Actor(
        name='Al Pacino',
        picture_url=f'{base_url}/al_pacino.png',
        gender='M',
        date_of_birth='1940-04-25'
    )
    actor_two.insert()


class BaseModel():

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
    '''

    def update(self):
        db.session.commit()


class Movie(BaseModel, db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer(), primary_key=True)
    title = Column(String(80), unique=True)
    poster_url = Column(String(100))
    release_date = Column(DateTime)

    '''
    short()
        short form representation of the Movie model
    '''

    def short(self):
        return {
            'id': self.id,
            'title': self.title,
            'poster_url': self.poster_url,
            'release_date': self.release_date
        }

    def __repr__(self):
        return json.dumps(self.short())


class Actor(BaseModel, db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer(), primary_key=True)
    name = Column(String(80))
    picture_url = Column(String(100))
    date_of_birth = Column(DateTime)
    date_of_passing_away = Column(DateTime)
    gender = Column(String(1))

    '''
    short()
        short form representation of the Actor model
    '''

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': calculate_age(self.date_of_birth),
            'gender': self.gender,
        }

    def __repr__(self):
        return json.dumps(self.short())


def calculate_age(born):
    today = date.today()
    return (today.year - born.year -
            ((today.month, today.day) < (born.month, born.day)))
