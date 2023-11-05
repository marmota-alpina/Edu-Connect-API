from .extensions import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text, nullable=True)
    course_load = db.Column(db.Integer)
    students = db.relationship("Student", back_populates="course")


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), nullable=True)
    registration = db.Column(db.String(10), unique=True)
    course_id = db.Column(db.ForeignKey("course.id"))

    course = db.relationship("Course", back_populates="students")
