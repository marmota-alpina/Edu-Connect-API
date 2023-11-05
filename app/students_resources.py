from flask_restx import Resource, Namespace

# Import models, extensions, and the Student model
from .api_models import student_model, student_input_model
from .extensions import db
from .models import Student, Course

# Create a Namespace for Students with a description
student_ns = Namespace('Students', description='Students operations', path="/students")


@student_ns.route("/")
class StudentListAPI(Resource):
    @student_ns.marshal_list_with(student_model)
    def get(self):
        """
        Get a list of students.

        This endpoint returns a list of all available students.

        Responses:
            200 OK - List of students
        """
        return Student.query.all()


@student_ns.route("/<int:id>")
@student_ns.response(404, 'Student not found')
@student_ns.param('id', 'The student identifier')
class StudentAPI(Resource):
    @student_ns.marshal_with(student_model, code=200)
    def get(self, id):
        """
        Get details of a specific student by ID.

        This endpoint returns the details of a specific student identified by their ID.

        Parameters:
            - id (int): The unique identifier of the student.

        Responses:
            200 OK - Student details
            404 Not Found - If the student with the given ID does not exist.
        """
        student = Student.query.get(id)
        if student is None:
            return student_ns.abort(404, "Student not found")

        return student

    @student_ns.response(400, 'Course not exists')
    @student_ns.expect(student_input_model)
    @student_ns.marshal_with(student_model, code=200)
    def put(self, id):
        """
        Update details of a specific student by ID.

        This endpoint allows you to update the details of a specific student identified by their ID.

        Parameters:
            - id (int): The unique identifier of the student.

        Request Body:
            - name (string): The updated name of the student.
            - course_id (int): The updated course ID to which the student belongs.

        Responses:
            200 OK - Updated student details
            400 Bad Request - If the course ID does not exist.
            404 Not Found - If the student with the given ID does not exist.
        """
        student = Student.query.get(id)
        if student is None:
            return "Student not found", 404
        student.name = student_ns.payload["name"]
        student.course_id = student_ns.payload["course_id"]

        course = Course.query.get(student.course_id)
        if not course:
            student_ns.abort(400, message="Course not exists")

        db.session.commit()
        return student

    def delete(self, id):
        """
        Delete a specific student by ID.

        This endpoint allows you to delete a specific student identified by their ID.

        Parameters:
            - id (int): The unique identifier of the student.

        Responses:
            204 No Content - Student deleted successfully
            404 Not Found - If the student with the given ID does not exist.
        """
        student = Student.query.get(id)
        if not student:
            student_ns.abort(404, message="Student not found")

        db.session.delete(student)
        db.session.commit()
        return {}, 204
