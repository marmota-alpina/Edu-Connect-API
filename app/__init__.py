from flask import Flask
from flask_cors import CORS

from .course_resources import course_ns
from .students_resources import student_ns
from .extensions import api, db


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(course_ns)
    api.add_namespace(student_ns)

    # Creating database tables automatically based on the models.
    with app.app_context():
        db.create_all()

    return app
