from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

api = Api(version='1.0.0', title='Edu-Connect API', description='An MVP Project for Edu-Connect')
db = SQLAlchemy()
