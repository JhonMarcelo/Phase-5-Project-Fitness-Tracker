#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, Flask, make_response, session
from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Exercise, Rating, Comment

ma = Marshmallow(app)
api = Api(app)


# # Views go here!
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        include_relationship = True
        load_instance = True
        # If u wanna exclude ID : exclude = ["id"]

    username = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    password = ma.auto_field()


singular_user_schema = UserSchema()
plural_user_schema = UserSchema(many=True)


class ExerciseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Exercise
        include_relationship = True
        load_instance = True
    
    exercise_name = ma.auto_field()
    target_muscle = ma.auto_field()
    sets = ma.auto_field() 
    reps = ma.auto_field()
    weight = ma.auto_field()

singular_exercise_schema = ExerciseSchema()
plural_exercise_schema = ExerciseSchema(many=True)


class RatingSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Rating
        include_relationship = True
        load_instance = True

    rate = ma.auto_field()
    user_id = ma.auto_field()
    exercise_id = ma.auto_field()

singular_rating_schema = RatingSchema()
plural_rating_schema = RatingSchema(many=True)


class CommentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Comment
        include_relationship = True
        load_instance = True

    comment = ma.auto_field()
    user_id = ma.auto_field()
    exercise_id = ma.auto_field()

singular_comment_schema = CommentSchema()
plural_comment_schema = CommentSchema(many=True)


#######################USER######################

class Users(Resource):
    def get(self):
        users = User.query.all()
        response = make_response(
            plural_user_schema.dump(users),
            200,
        )
        return response
       
    def post(self):
        
        new_user = singular_user_schema.load(request.json)

        new_user.password_hash = new_user.password

        new_user.password = ""

        print(f'{new_user}')

        db.session.add(new_user)
        db.session.commit()

        response = make_response(
            singular_user_schema.dump(new_user),
            201,
        )
        return response
    



class getUserByID(Resource):
    def get(self, id):
        theUser = User.query.filter_by(id=id).first()

        response = make_response(
            singular_user_schema.dump(theUser),
            200,
        )
        return response
    def delete(self, id):
        
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

        response = make_response(
            singular_user_schema.dump(user),
            200,

        )

####################EXERCISE######################
class getUserExercise(Resource):
    def get(self,id):
        theUser = User.query.filter_by(id=id).first()
        
        userExercise = theUser.my_exercise

        response = make_response(
            plural_exercise_schema.dump(userExercise),
            200,
        )
        return response
    
    #Adding new user exercise
    def post(self,id):
        
        theUser = User.query.filter_by(id=id).first()
        fetched_exercise = singular_exercise_schema.load(request.json)
        
        
        db.session.add(fetched_exercise)
        db.session.commit()

        theUser.my_exercise.append(fetched_exercise)
        db.session.commit()

        response = make_response(
            singular_exercise_schema.dump(fetched_exercise),
            201,
        )
        return response
    #Updating exercise reps/sets/weight
    def patch(self,id,):
        user = User.query.filter_by(id=id).first()
        

        fetched_exercise = singular_exercise_schema.load(request.json)

        
        for ex in user.my_exercise:
                    if ex.exercise_name == fetched_exercise.exercise_name:
                        user.my_exercise.remove(ex)
                        
                        deletePreviousRecord = Exercise.query.filter_by(id=ex.id).first()
                        db.session.delete(deletePreviousRecord)
                        
                        db.session.commit()

                        user.my_exercise.append(fetched_exercise)
                        db.session.commit()
                        

        response = make_response(
            singular_exercise_schema.dump(fetched_exercise),
            200,
        )
        return response
    



class deleteExerciseFromUser(Resource):

    def delete(self,user_id,exercise_id):
        user = User.query.filter_by(id=user_id).first()
        exercise = Exercise.query.filter_by(id=exercise_id).first()

        user.my_exercise.remove(exercise)
        db.session.commit()

        response = make_response(
            singular_exercise_schema.dump(exercise),
            200,
        )
        return response
    
#######################RATING######################

class ExerciseRateByUser(Resource):

    # def get(self,id):
    #     theUser = User.query.filter_by(id=id).first()
        
    #     userExercise = theUser.my_exercise


    #     response = make_response(
    #         singular_rating_schema.dump(userExercise),
    #         200,
    #     )
    #     return response
    
#     #Adding new exercise rate
    def post(self,id):
        
        user = User.query.filter_by(id=id).first()
        fetched_data = singular_rating_schema.load(request.json)

        db.session.add(fetched_data)
        db.session.commit()

        response = make_response(
            singular_rating_schema.dump(fetched_data),
            201,
        )
        return response

# # import ipdb; ipdb.set_trace()

class ExerciseCommentByUser(Resource):
    def post(self,id):
        user = User.query.filter_by(id=id).first()
        fetched_data = singular_comment_schema.load(request.json)

        db.session.add(fetched_data)
        db.session.commit()

        response = make_response(
            singular_comment_schema.dump(fetched_data),
            201,
        )
        return response


class Login(Resource):
    def post(self):
        new_user = singular_user_schema.load(request.json)
        print(f'{new_user.password}')

        user = User.query.filter_by(username=new_user.username).first()
    
        if user and user.authenticate(new_user.password):
            session['user_id'] = user.id
            return make_response(user.to_dict(), 200)
        else:
            return make_response({}, 401)
    
# class CheckSession(Resource):
#     def get(self):
#         user_id = session['user_id']
#         if user_id:
#             user = User.query.filter(User.id == user_id).first()
#             return


api.add_resource(Login, '/login')
api.add_resource(Users, '/users')
api.add_resource(getUserByID, '/users/<int:id>')
api.add_resource(getUserExercise, '/exercise/<int:id>')
api.add_resource(ExerciseCommentByUser, '/exercise/comment/<int:id>')
api.add_resource(ExerciseRateByUser, '/exercise/rating/<int:id>')
api.add_resource(deleteExerciseFromUser, '/exercise/<int:user_id>/<int:exercise_id>')    

# @app.route('/login', methods=["POST"])
# def login():
#     data = request.get_json()
#     user = User.query.filter(User.username == data['username']).first()

#     if user:
#         if user.authenticate(data['password']):
#             session["user_id"] = user.is_delete
#             return user.to_dict(),200
#     else:
#         return {"errors":["Username or password incorrect"]},401

# def index():
#     return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

