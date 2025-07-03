from flask_restful import Resource
from flask import make_response, request
from extensions import db
from models import Guest
from schemas import GuestSchema

# Import the Guest model and schema

guest_schema = GuestSchema()
guests_schema = GuestSchema(many=True)


class Guests(Resource):
    def get(self):
        #get all guest
        guests=Guest.query.all()
        return guests_schema.dump(guests),200