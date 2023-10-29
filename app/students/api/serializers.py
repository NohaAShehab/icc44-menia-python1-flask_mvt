from flask_restful import  fields
track_serializer={
    "id":fields.Integer,
    "name":fields.String,
}

student_serializer={
    "id":fields.Integer,
    "name":fields.String,
    'email':fields.String,
    "image":fields.String,
    'grade':fields.Integer,
    "address":fields.String,
    "created_at":fields.DateTime,
    "updated_at":fields.DateTime,
    'track_id':fields.Integer,
    'track':fields.Nested(track_serializer)
    }

