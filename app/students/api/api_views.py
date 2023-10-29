from flask_restful import Resource, marshal_with
from app.models import  Student, db
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



class StudentResource(Resource):

    @marshal_with(student_serializer)
    def get(self, std_id):
        student =Student.get_specific_student(std_id)
        return student, 200

    @marshal_with(student_serializer)
    def put(self, std_id):
        student =Student.get_specific_student(std_id)
        student_args = student_request_parser.parse_args()
        student.name=student_args['name']
        student.image = student_args['image']
        student.email = student_args['email']
        student.address = student_args['address']
        student.track_id = student_args['track_id']
        db.session.add(student)
        db.session.commit()
        return student

        # parsing request arguments


        pass


    def delete(self, std_id):
        Student.delete_object(std_id)
        return  'no content', 204
