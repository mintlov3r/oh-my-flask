from flask import Blueprint
from flask import render_template


main = Blueprint("main", __name__)


@main.route('/')
def index():
    return "hello!"

@main.route('/<name>')
def get_name(name):
    return render_template("index.html", name=name)
