# casting-agency-backend

## where the project lives

`https://rampa-rampa.herokuapp.com/`

## start app

```bash
pip install -r requirements.txt

brew tap heroku/brew && brew install heroku
heroku local
```

## auth0 settings

https://127.0.0.1:4200/login
http://127.0.0.1/login-result, http://localhost:4200/tabs/user-page
https://127.0.0.1/logout

### login url

https://pharrukh.eu.auth0.com/authorize?audience=casting-agency-api&response_type=token&client_id=fakhoCb5qW6ALehVUwIDnnILGG1RurHu&redirect_uri=http://localhost:4200/tabs/user-page

### tokens

can be found in the `.env` file

## testing

dropdb casting_agency_testing
createdb casting_agency_testing
python test_flask_app.py

## manual testing

postman config file can be found in the root

## Documentation of API behavior

- movies
- GET
- DELETE
- PATCH
- POST

- actors
- GET
- DELETE
- PATCH
- POST

## RBAC

- Casting Assistant
  - can view actors and movies
- Casting Director
  - manages actors
  - can update movies
- Executive Director
  - manages actors and movies

## about the author

![normuradov logo](https://raw.githubusercontent.com/pharrukh/pharrukh/master/normuradov.png "Logo")

I inspire people and bring value.

[![github](https://raw.githubusercontent.com/pharrukh/pharrukh/master/icons/github.png "GitHub")](https://github.com/pharrukh)
[![linkedin](https://raw.githubusercontent.com/pharrukh/pharrukh/master/icons/linkedin.png "LinkedIn")](https://www.linkedin.com/in/farrukh-normuradov/)
[![stackoverflow](https://raw.githubusercontent.com/pharrukh/pharrukh/master/icons/stackoverflow.png "StackOverflow")](https://stackoverflow.com/users/3407539/farrukh-normuradov)
[![website](https://raw.githubusercontent.com/pharrukh/pharrukh/master/icons/website.png "normuradov.com")](https://www.normuradov.com/)
