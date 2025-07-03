from flask_restful import Resource
from flask import make_response, request
from models import db,Guest

class Guests(Resource):
    def get(self):
        #get all guest
        guests=Guest.query.all()
        return [guest.to_dict() for guest in guests],200