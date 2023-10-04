from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import declarative_base
from config import db
from typing import List

Base = declarative_base()


# Models go here!
# user_exercise = db.Table("user_exercise",
#                     Base.metadata,
#                     db.Column("user_id",db.Integer, db.ForeignKey("user.id")),
#                     db.Column("exercise_id",db.Integer, db.ForeignKey("exercise.id"))  
# )
# class UserExercise (db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column("user_id",db.Integer, db.ForeignKey("user.id"))
#     exercise_id = db.Column("exercise_id",db.Integer, db.ForeignKey("exercise.id"))

#     user = db.relationship('User', back_populates='exercises')
#     exercise = db.relationship('Exercise', back_populates='users')

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    
    ratings = db.relationship("Rating", backref="user")
    # exercises = db.relationship('UserExercise', back_populates='user')



    # def __repr__(self):
    #     return f"<User {self.id},"\
    #         + f"id = {self.id}, "\
    #         + f"username = {self.username}, "\
    #         + f"first_name = {self.first_name}, "\
    #         + f"last_name = {self.last_name}, "\
    #         + ">"


class Exercise(db.Model, SerializerMixin):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    target_muscle = db.Column(db.String)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    weight = db.Column(db.Integer)

#     users = db.relationship('UserExercise', back_populates='exercise')

#     def __repr__(self):
#         return f"id = {self.id}, "\
#             + f"exercise_name = {self.exercise_name}, "\
#             + f"target_muscle = {self.target_muscle}, "\
#             + f"sets = {self.sets}, "\
#             + f"reps = {self.reps}, "\
#             + f"weight = {self.weight}, "\
#             + ">"

class Rating(db.Model, SerializerMixin):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key = True)
    rate = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
 
    

    # def __repr__(self):
    #     return f"<Rating {self.id},"\
    #         + f"id = {self.id}, "\
    #         + f"rate = {self.rate}, "\
    #         + ">"