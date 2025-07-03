from flask_restful import Resource
from flask import make_response, request
from models import db,Appearance

class Appearances(Resource):
    def post(self):
        data=request.get_json()
        try:
            new_appearance = Appearance(
                rating=data.get("rating"),
                episode_id=data.get("episode_id"),
                guest_id=data.get("guest_id")
            )

            db.session.add(new_appearance)
            db.session.commit()

            return make_response({
                "id": new_appearance.id,
                "rating": new_appearance.rating,
                "episode_id": new_appearance.episode_id,
                "guest_id": new_appearance.guest_id
            }, 201)

        except Exception as e:
            db.session.rollback()
            return make_response({"error": str(e)}, 400)
        