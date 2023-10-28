from flask_sqlalchemy import SQLAlchemy
from flask import url_for
db= SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'students'
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    image= db.Column(db.String)

    @classmethod
    def get_all_students(cls):
        return cls.query.all()

    @classmethod
    def get_specific_student(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def delete_object(cls, id):
        std = cls.query.get_or_404(id)
        db.session.delete(std)
        db.session.commit()
        return True

    @property
    def delete_url(self):
        return url_for('students.delete', id=self.id)

    @property
    def show_url(self):
        return url_for('students.show', id=self.id)

    @classmethod
    def save_object(cls, requestdata):
        std = cls(**requestdata)
        db.session.add(std)
        db.session.commit()
        return std
