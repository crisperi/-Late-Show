from flask_restful import Resource
from flask import make_response, request
from models import Appearance
from extensions import db
from schemas import AppearanceSchema

# Import the Appearance model and schema

appearance_schema = AppearanceSchema()
appearances_schema = AppearanceSchema(many=True)



class Appearances(Resource):
    def post(self):
        data=request.get_json()
        try:
            new_appearance = appearance_schema.load(data,session=db.session)
            
        except Exception as e  :
                return {"error": "validation errors"}, 400
        
        db.session.add(new_appearance)
        db.session.commit()
        
        return appearance_schema.dump(new_appearance), 201