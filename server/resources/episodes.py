from flask_restful import Resource
from flask import make_response, request
from extensions import db
from models import Episode
from schemas import EpisodeSchema

# Import the Episode model and schema
episode_schema = EpisodeSchema()
episodes_schema =EpisodeSchema(many=True)

class Episodes(Resource):
    def get(self,id=None):
        #get all episodes or if it has id get one episode 
        if id is None :
            episodes=Episode.query.all()
            return episodes_schema.dump(episodes),200
        
        else:
            episode=Episode.query.get(id)
            if not episode:
                return {"error":"Episode not found"},404
            return episode_schema.dump(episode),200
        
    def delete(self,id):
            episode =Episode.query.get(id)
            if not episode:
                return {"error":"Episode not found"},404
            
            db.session.delete(episode)
            db.session.commit()
            return {"message":"Episode deleted successfully"},200