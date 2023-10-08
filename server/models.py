from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import declarative_base
from config import db


Base = declarative_base()


# Models go here!

user_exercise = db.Table("user_exercise",
                    # Base.metadata,
    db.Column("user_id",db.Integer, db.ForeignKey("users.id")),
    db.Column("exercise_id",db.Integer, db.ForeignKey("exercises.id"))  
)


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    _password_hash = db.Column(db.String)
    ratings = db.relationship("Rating", backref="ratings")
    comments = db.relationship("Comment", backref="comments")

    my_exercise = db.relationship("Exercise", secondary=user_exercise, backref='my_exercises')



    


    def __repr__(self):
        return f"<User {self.id},"\
            + f"id = {self.id}, "\
            + f"username = {self.username}, "\
            + f"first_name = {self.first_name}, "\
            + f"last_name = {self.last_name}, "\
            + ">"


class Exercise(db.Model, SerializerMixin):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    target_muscle = db.Column(db.String)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    weight = db.Column(db.Integer)

    exercise_rate = db.relationship('Rating', backref = 'exercise_rate', uselist = False)
    exercise_comment = db.relationship('Comment', backref = 'exercise_comment', uselist = False)
    
    def __repr__(self):
        return f"id = {self.id}, "\
            + f"exercise_name = {self.exercise_name}, "\
            + f"target_muscle = {self.target_muscle}, "\
            + f"sets = {self.sets}, "\
            + f"reps = {self.reps}, "\
            + f"weight = {self.weight}, "\
            + ">"
class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"))
    


class Rating(db.Model, SerializerMixin):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key = True)
    rate = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"))

 
    

    def __repr__(self):
        return f"<Rating {self.id},"\
            + f"id = {self.id}, "\
            + f"rate = {self.rate}, "\
            + f"user_id = {self.user_id}, "\
            + f"exercise_id = {self.exercise_id}, "\
            + ">"