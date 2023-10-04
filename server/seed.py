#!/usr/bin/env python3

# Standard library imports

from random import randint, choice as rc
# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Rating


if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        
        # adding users
        # for _ in range(4):
        #     first_name = fake.first_name()
        #     last_name=fake.last_name()
        #     username = f"{first_name}_{last_name}"
        #     user = User(username=username,first_name=first_name,last_name=last_name)

        #     db.session.add(user)
        #     db.session.commit()

        db_users = db.session.query(User).all()

        for user in db_users:
            ratings = Rating(rate = randint(1,5), user_id = user.id)

            db.session.add(ratings)
            db.session.commit()

        import ipdb; ipdb.set_trace()

