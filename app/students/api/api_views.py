from flask_restful import Resource, marshal_with
from app.models import  Student
from app.students.api.serializers import student_serializer
from flask import  request
from app.students.api.parsers import student_request_parser
class StudentListClass(Resource):
    @marshal_with(student_serializer)
    def get(self):
        students= Student.get_all_students()
        return students


    @marshal_with(student_serializer)
    def post(self):
        # accept request parameters
        print(request.form)
        student_args=student_request_parser.parse_args()
        print(student_args)
        student = Student.save_object(student_args)
        return  student, 201
        # save object
        return  "Post Method"

