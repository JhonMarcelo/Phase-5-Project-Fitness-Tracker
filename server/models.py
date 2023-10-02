from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

class User(db.model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __repr__(self):
        return f"<User {self.id},"\
            + f"id = {self.id}, "\
            + f"username = {self.username}, "\
            + f"first_name = {self.first_name}, "\
            + f"last_name = {self.last_name}, "\
            + ">"

class Exercise(db.model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    target_muscle = db.Column(db.String)
    

    def __repr__(self):
        return f"<User {self.id},"\
            + f"id = {self.id}, "\
            + f"username = {self.username}, "\
            + f"first_name = {self.first_name}, "\
            + f"last_name = {self.last_name}, "\
            + ">"
