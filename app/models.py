from flask_sqlalchemy import SQLAlchemy
from datetime import  datetime
from flask import url_for
db= SQLAlchemy()


class Track(db.Model):
    __tablename__='tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    students = db.relationship('Student', backref='track')

    @classmethod
    def get_all_tracks(cls):
        return cls.query.all()

    @classmethod
    def get_specific_track(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def delete_object(cls, id):
        std = cls.query.get_or_404(id)
        db.session.delete(std)
        db.session.commit()
        return True

    @classmethod
    def save_object(cls, requestdata):
        std = cls(**requestdata)
        db.session.add(std)
        db.session.commit()
        return std

    @property
    def delete_url(self):
        return url_for('tracks.delete', id=self.id)

    @property
    def show_url(self):
        return url_for('tracks.show', id=self.id)



class Student(db.Model):
    __tablename__ = 'students'
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    image= db.Column(db.String)
    grade = db.Column(db.Integer, default=10)
    address = db.Column(db.String, default='Cairo')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at=  db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=True)
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
