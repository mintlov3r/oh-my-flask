from flask import Blueprint


movie = Blueprint("movie", __name__)

@movie.route('/<id>')
def get_movie(id):
    return "hello, {}!".format(id)


@movie.route('/')
def movie_index():
    return "hello, welcome to movie index!"