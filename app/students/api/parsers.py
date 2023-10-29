from flask_restful import reqparse

student_request_parser = reqparse.RequestParser()

student_request_parser.add_argument("name", type=str, help='Student name is required', required=True)
student_request_parser.add_argument("image", type=str)
student_request_parser.add_argument("email", type=str)
student_request_parser.add_argument("address", type=str)
student_request_parser.add_argument("track_id", type=int)
