# casting-agency-backend

## motivation for the project

I took this certification to become a better developer.  
The concepts were familiar to me from C# and JS projects.  
Now I saw it from the Python perspective.

## project dependencies

- flask
- wsgi
- heroku
- postgresql

The current stack is the familiar Python one.  
I picked it as it was a requirement for the project.

## start app

```bash
# create virtual environment as a boundary for packages
mkproject casting-agency
# use the virtual environment
workon casting-agency
# switch to the working directory
cd casting-agency-backent
# install packages to the virtual environment
pip install -r requirements.txt
# install heroku
brew tap heroku/brew && brew install heroku
# start heroku
heroku local
```

## auth0 settings

login: https://127.0.0.1:4200/login  
redirect: http://localhost:4200/tabs/user-page  
logout: https://127.0.0.1/logout

### login url

https://pharrukh.eu.auth0.com/authorize?audience=casting-agency-api&response_type=token&client_id=fakhoCb5qW6ALehVUwIDnnILGG1RurHu&redirect_uri=http://localhost:4200/tabs/user-page

### tokens

can be found in the `.env` file or by running:

```bash
source setup.sh
```

## testing

```bash
dropdb casting_agency_testing
createdb casting_agency_testing
python test_flask_api.py
```

## manual testing

postman config file can be found in the root

## routes

## API endpoints

#### GET '/movies'

- Fetches a collection of movies.
- Request Arguments: None

Sample curl request:
`curl -X GET http://127.0.0.1:5000/movies`

Sample response:

```json
{
    "movies": [
      {
        "title":"Godfather",
        "release_date":"1973-04-03",
        "poster_url":"..."
      }
    ],
}
```

#### GET '/movies/<int:id>'

- Fetches a single movie.
- Request Arguments: id of the movie

Sample curl request:
`curl -X GET http://127.0.0.1:5000/movies/1`

Sample response:

```json
{
  "title":"Godfather",
  "release_date":"1973-04-03",
  "poster_url":"..."
}
```
#### DELETE '/movies/<int:id>'

- Removes a movie.
- Request Arguments: id of the movie

Sample curl request:
`curl -X DELETE http://127.0.0.1:5000/movies/1`

#### PATCH '/movies/<int:id>'

- Updates a single movie.
- Request Arguments: id of the movie

Sample curl request:
```sh
curl -X PATCH http://127.0.0.1:5000/movies/1 \
-d "{\"title\":\"Godfather II\"}"
```

Sample response:

```json
{
    "movies": [
      {
        "title":"Godfather",
        "release_date":"1973-04-03",
        "poster_url":"..."
      }
    ],
}
```

#### POST '/movies'

- Creates a single movie.
- Request Arguments: id of the movie

Sample curl request:
```sh
curl -X POST http://127.0.0.1:5000/movies \
-d "{
        \"title\":\"Godfather II\",
        \"release_date\":\"1973-04-03\",
        \"poster_url\":\"...\"
    }"
```

Sample response:

```json
{
    "movies": [
      {
        "title":"Godfather",
        "release_date":"1973-04-03",
        "poster_url":"..."
      }
    ],
}
```

#### GET '/actors'

- Fetches a collection of actors.
- Request Arguments: None

Sample curl request:
`curl -X GET http://127.0.0.1:5000/actors`

Sample response:

```json
{
    "actors": [
      {
        "name":"Al Pacino",
        "date_of_birth":"1940-04-03",
        "picture_url":"...",
        "gender":"M"
      }
    ],
}
```

#### GET '/actors/<int:id>'

- Fetches a single actor.
- Request Arguments: id of the actor

Sample curl request:
`curl -X GET http://127.0.0.1:5000/actors/1`

Sample response:

```json
{
  "name":"Al Pacino",
  "release_date":"1940-04-03",
  "picture_url":"...",
  "gender":"M"
}
```
#### DELETE '/actors/<int:id>'

- Removes a actor.
- Request Arguments: id of the actor

Sample curl request:
`curl -X DELETE http://127.0.0.1:5000/actors/1`

#### PATCH '/actors/<int:id>'

- Updates a single actor.
- Request Arguments: id of the actor

Sample curl request:
```sh
curl -X PATCH http://127.0.0.1:5000/actors/1 \
-d "{\"name\":\"AL PACHINO\"}"
```

Sample response:

```json
{
    "actors": [
      {
        "name":"AL PACHINO",
        "date_of_birth":"1940-04-03",
        "picture_url":"...",
        "gender":"M"
      }
    ],
}
```

#### POST '/actors'

- Creates a single actor.
- Request Arguments: id of the actor

Sample curl request:
```sh
curl -X POST http://127.0.0.1:5000/actors \
-d "{
        \"name\":\"AL PACHINO\",
        \"date_of_birth\":\"1940-04-03\",
        \"picture_url\":\"...\",
        \"gender\":\"M\"
    }"
```

Sample response:

```json
{
    "movies": [
      {
        "name":"AL PACHINO",
        "date_of_birth":"1940-04-03",
        "picture_url":"...",
        "gender":"M"
      }
    ],
}
```

## roles & scopes

- Casting Assistant
  - read:movie
  - read:actor
- Casting Director
  - read:movie
  - read:actor
  - update:movie
  - update:actor
  - delete:actor
  - create:actor
- Executive Director
  - read:movie
  - update:movie
  - delete:movie
  - create:movie
  - read:actor
  - update:actor
  - delete:actor
  - create:actor

## deploying project to Heroku

```sh
git push heroku main
```

## where the project lives

`https://rampa-rampa.herokuapp.com/`

## about the author

![normuradov logo](https://raw.githubusercontent.com/pharrukh/pharrukh/master/normuradov.png "Logo")

I inspire people and bring value.

[![github](https://raw.githubusercontent.com/pharrukh/pharrukh/master/icons/github.png "GitHub")](https://github.com/pharrukh)
[![linkedin](https://raw.githubusercontent.com/pharrukh/pharrukh/master/icons/linkedin.png "LinkedIn")](https://www.linkedin.com/in/farrukh-normuradov/)
[![stackoverflow](https://raw.githubusercontent.com/pharrukh/pharrukh/master/icons/stackoverflow.png "StackOverflow")](https://stackoverflow.com/users/3407539/farrukh-normuradov)
[![website](https://raw.githubusercontent.com/pharrukh/pharrukh/master/icons/website.png "normuradov.com")](https://www.normuradov.com/)
