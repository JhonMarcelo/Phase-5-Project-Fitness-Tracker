#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, Flask, make_response
from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow

# Local imports
from config import app, db, api
# Add your model imports
from models import User

ma = Marshmallow(app)



# # Views go here!
# class UserSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = User

#     username = ma.auto_field()

# singular_user_schema = UserSchema()
# plural_user_schema = UserSchema(many=True)

# class Users(Resource):
#     def get(self):
#         users = User.query.all()
#         response = make_response(
#             singular_user_schema.dump(users),
#             200,
#         )
#         return response
    
#     def post(self):
#         new_user = User(
#             username = request.form['username'],
#             first_name = request.form['first_name'],
#             last_name = request.form['last_name'],
#         )
#         db.session.add(new_user)
#         db.session.commit()

#         response = make_response(
#             singular_user_schema.dump(new_user),
#             201,
#         )
#         return response
# api.add_resource(Users, '/users')


# @app.route('/')
# def index():
#     return '<h1>Project Server</h1>'


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

