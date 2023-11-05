from flask_restx import fields

from .extensions import api

course_model = api.model("Course", {
    "id": fields.Integer,
    "name": fields.String,
})

student_model = api.model("Student", {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "registration": fields.String,
    "course": fields.Nested(course_model)
})

course_input_model = api.model("CourseInput", {
    "name": fields.String,
    "description": fields.String,
    "course_load": fields.Integer
})

student_input_model = api.model("StudentInput", {
    "name": fields.String,
    "email": fields.String,
    "course_id": fields.Integer
})

enroll_input_model = api.model("CourseEnrollInput", {
    "name": fields.String,
    "email": fields.String,
})