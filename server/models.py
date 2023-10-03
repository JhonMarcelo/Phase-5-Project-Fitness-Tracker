from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
user_exercise = db.Table('user_to_exercise',
                            db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                            db.Columm('exercise_id', db.Integer, db.ForeignKey('channel.id'))
                         )

class User(db.model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    my_exercise = db.relationship('Exercise', secondary=user_exercise, backref = 'exercises')

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
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    

    def __repr__(self):
        return f"<User {self.id},"\
            + f"id = {self.id}, "\
            + f"exercise_name = {self.exercise_name}, "\
            + f"target_muscle = {self.target_muscle}, "\
            + f"sets = {self.sets}, "\
            + f"reps = {self.reps}, "\
            + f"weight = {self.weight}, "\
            + ">"
