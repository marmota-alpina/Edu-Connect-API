from flask_restx import Resource, Namespace

# Import models, extensions, and the Course model
from .api_models import course_model, course_input_model, enroll_input_model, student_model
from .extensions import db
from .models import Course, Student

COURSE_NOT_FOUND = "Course not found"

# Create a Namespace for Courses with a description
course_ns = Namespace('Courses', description='Courses operations', path="/courses")


@course_ns.route("/")
class CourseListAPI(Resource):
    COURSE_ALREADY_EXISTS = "A course with the same name and course load already exists."

    @course_ns.marshal_list_with(course_model)
    def get(self):
        """
        Get a list of courses.

        This endpoint returns a list of all available courses.

        Responses:
            200 OK - List of courses
        """
        return Course.query.all()

    @course_ns.expect(course_input_model)
    @course_ns.marshal_with(course_model, code=201)
    @course_ns.response(409, 'Course already exists')
    def post(self):
        """
        Create a new course.

        This endpoint allows you to create a new course with the provided data.

        Request Body:
            - name (string): The name of the course.
            - description (string): The description of the course.
            - course_load (int): The course load in hours.

        Responses:
            201 Created - The created course
            409 Conflict - If the course name is already in use.
        """
        course = Course(name=course_ns.payload["name"], description=course_ns.payload["description"],
                        course_load=course_ns.payload["course_load"])
        course_exists = Course.query.filter_by(name=course.name, course_load=course.course_load).first()
        if course_exists:
            course_ns.abort(409, message=self.COURSE_ALREADY_EXISTS)
        db.session.add(course)
        db.session.commit()
        return course, 201


@course_ns.route("/<int:id>/students")
@course_ns.param('id', 'The course identifier')
@course_ns.response(200, 'Students enrolled in the course')
@course_ns.response(404, COURSE_NOT_FOUND)
class Students(Resource):
    @course_ns.marshal_list_with(student_model)
    def get(self, id):
        """
        Get a list of students enrolled in a course.

        This endpoint returns a list of all students enrolled in a course.

        Parameters:
            - id (int): The unique identifier of the course.

        Responses:
            200 OK - List of students
            404 Not Found - If the course with the given ID does not exist.
        """
        course = Course.query.get(id)
        if not course:
            course_ns.abort(404, message=COURSE_NOT_FOUND)
        return course.students


@course_ns.route("/<int:id>/enroll")
@course_ns.param('id', 'The course identifier')
@course_ns.response(201, 'Student enrolled successfully')
@course_ns.response(404, COURSE_NOT_FOUND)
@course_ns.response(409, 'Student already enrolled')
class CourseEnrollment(Resource):
    @course_ns.expect(enroll_input_model)
    @course_ns.marshal_with(student_model, code=201)
    def post(self, id):
        """
        Enroll a student in a course.

        This endpoint allows you to enroll a student in a specific course identified by its ID.

        Parameters:
            - id (int): The unique identifier of the course.

        Request Body:
            - name (string): The name of the student.
            - email (string): The email of the student.

        Responses:
            201 Created - The enrolled student
            404 Not Found - If the course with the given ID does not exist.
            409 Conflict - If the student is already enrolled in the course.
        """
        course = Course.query.get(id)
        if not course:
            course_ns.abort(404, message=COURSE_NOT_FOUND)

        student_exists = Student.query.filter_by(email=course_ns.payload["email"], course_id=course.id).first()
        if student_exists:
            course_ns.abort(409, message="Student already enrolled")

        total_of_students = Student.query.filter_by(course_id=id).count()
        registration = f"{course.id}{total_of_students + 1}".zfill(10)
        student = Student(name=course_ns.payload["name"], email=course_ns.payload["email"], course_id=course.id,
                          registration=registration)
        db.session.add(student)
        db.session.commit()
        return student, 201


@course_ns.route("/<int:id>")
@course_ns.response(404, COURSE_NOT_FOUND)
@course_ns.param('id', 'The course identifier')
class CourseAPI(Resource):
    @course_ns.marshal_with(course_model)
    def get(self, id):
        """
        Get a specific course by ID.

        This endpoint returns the details of a specific course identified by its ID.

        Parameters:
            - id (int): The unique identifier of the course.

        Responses:
            200 OK - Course details
            404 Not Found - If the course with the given ID does not exist.
        """
        course = Course.query.get(id)
        return course

    @course_ns.expect(course_input_model)
    @course_ns.marshal_with(course_model)
    @course_ns.response(200, 'Course updated successfully')
    def put(self, id):
        """
        Update a specific course by ID.

        This endpoint allows you to update the details of a specific course identified by its ID.

        Parameters:
            - id (int): The unique identifier of the course.

        Request Body:
            - name (string): The updated name of the course.

        Responses:
            200 OK - Updated course details
            404 Not Found - If the course with the given ID does not exist.
        """
        course = Course.query.get(id)
        if not course:
            course_ns.abort(404, message=("%s" % COURSE_NOT_FOUND))
        course.name = course_ns.payload["name"]
        course.description = course_ns.payload["description"]
        course.course_load = course_ns.payload["course_load"]
        db.session.commit()
        return course

    @course_ns.response(204, 'Course deleted successfully')
    @course_ns.response(409, 'Course has students enrolled')
    def delete(self, id):
        """
        Delete a specific course by ID.

        This endpoint allows you to delete a specific course identified by its ID.

        Parameters:
            - id (int): The unique identifier of the course.

        Responses:
            204 No Content - Course deleted successfully.
            404 Not Found - If the course with the given ID does not exist.
            409 Conflict - If the course name is already in use.
        """
        course = Course.query.get(id)
        total_of_students = Student.query.filter_by(course_id=id).count()

        if total_of_students > 0:
            course_ns.abort(409, message="Course has students enrolled")

        if not course:
            course_ns.abort(404, message=COURSE_NOT_FOUND)

        db.session.delete(course)
        db.session.commit()
        return {}, 204
