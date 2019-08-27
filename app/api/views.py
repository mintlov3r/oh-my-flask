from flask import Blueprint

# 蓝图
api = Blueprint("api", __name__)

@api.route('/<id>')
def return_id(id):
    return "hello! my id is {}".format(id)

@api.route('/')
def index():
    return "hello! welcome to my index page!"
