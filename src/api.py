from flask import Flask,  request, jsonify, render_template, abort
from flask_cors import CORS
from database.models import setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

# db_drop_and_create_all()


@app.route('/actors', methods=['GET'])
@requires_auth('read:actor')
def get_actors():
    return jsonify({'success': True, 'actors': get_actors_short()})


@app.route('/actors/<int:id>', methods=['GET'])
@requires_auth('read:actor')
def get_actor(id):
    actor = Actor.query.get(id)
    if not actor:
        abort(404)
    return jsonify(actor.short())


@app.route('/actors', methods=['POST'])
@requires_auth('create:actor')
def create_actor():
    actor = request.get_json()

    if 'name' not in actor or 'date_of_birth' not in actor or 'picture_url' not in actor or 'gender' not in actor:
        abort(400)

    new_actor = Actor(
        name=actor['name'], date_of_birth=actor['date_of_birth'], picture_url=actor['picture_url'], gender=actor['gender'])
    new_actor.insert()

    return jsonify({'success': True, 'actors': get_actors_short()})


@app.route('/actors/<int:id>', methods=['PATCH'])
@requires_auth('update:actor')
def update_actor(id):
    actor = Actor.query.get(id)
    if not actor:
        abort(404)

    update_data = request.get_json()

    if 'name' in update_data:
        actor.name = update_data['name']

    if 'date_of_birth' in update_data:
        actor.date_of_birth = update_data['date_of_birth']

    if 'picture_url' in update_data:
        actor.picture_url = update_data['picture_url']

    actor.update()

    return jsonify({'success': True, 'actors': get_actors_short()})


@app.route('/actors/<int:id>', methods=['DELETE'])
@requires_auth('delete:actor')
def delete_actor(id):
    actor = Actor.query.get(id)
    if not actor:
        abort(404)
    actor.delete()
    return '', 204


def get_actors_short():
    return [actor.short() for actor in Actor.query.all()]


@app.route('/movies', methods=['GET'])
@requires_auth('read:movie')
def get_movies():
    return jsonify({'success': True, 'movies': get_movies_short()})


@app.route('/movies/<int:id>', methods=['GET'])
@requires_auth('read:movie')
def get_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        abort(404)
    return jsonify(movie.short())


@app.route('/movies', methods=['POST'])
@requires_auth('create:movie')
def create_movie():
    movie = request.get_json()

    new_movie = Movie(
        title=movie['title'], release_date=movie['release_date'], poster_url=movie['poster_url'])
    new_movie.insert()

    return jsonify({'success': True, 'movies': get_movies_short()})


@app.route('/movies/<int:id>', methods=['PATCH'])
@requires_auth('update:movie')
def update_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        abort(404)

    update_data = request.get_json()

    if 'title' in update_data:
        movie.title = update_data['title']

    if 'release_date' in update_data:
        movie.release_date = update_data['release_date']

    if 'poster_url' in update_data:
        movie.poster_url = update_data['poster_url']

    movie.update()

    return jsonify({'success': True, 'movies': get_movies_short()})


@app.route('/movies/<int:id>', methods=['DELETE'])
@requires_auth('delete:movie')
def delete_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        abort(404)
    movie.delete()
    return '', 204


def get_movies_short():
    return [movie.short() for movie in Movie.query.all()]


@app.route('/health', methods=['GET'])
def get_health():
    return jsonify({'healthy': True})


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    # TODO: this can be improved
    if error.status_code == 401:
        return render_template('errors/401.html'), 401
    if error.status_code == 403:
        return render_template('errors/403.html'), 403
    return render_template('errors/500.html'), 500


@app.errorhandler(401)
def server_error(error):
    return render_template('errors/401.html'), 401


@app.errorhandler(403)
def server_error(error):
    return render_template('errors/403.html'), 403


@app.errorhandler(422)
def server_error(error):
    return render_template('errors/422.html'), 422


@app.errorhandler(405)
def server_error(error):
    return render_template('./errors/405.html'), 405


@app.errorhandler(409)
def server_error(error):
    return render_template('./errors/405.html'), 409
