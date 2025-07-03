from app import ma
from models import Guest, Episode, Appearance
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields

class GuestSchema(SQLAlchemySchema):
    class Meta:
        model=Guest
        load_instance=True
        
    id = auto_field()
    name = auto_field()
    occupation = auto_field()
    
class EpisodeSchema(SQLAlchemySchema):
    class Meta:
        model=Episode
        load_instance=True
        
    id = auto_field()
    date = auto_field()
    number = auto_field()
    
class AppearanceSchema(SQLAlchemySchema): 
    class Meta:
        model=Appearance
        load_instance=True
        
    id = auto_field()
    rating = auto_field()
    episode_id = auto_field()
    guest_id = auto_field()
    
    #nested relationships
    episode = fields.Nested(EpisodeSchema)
    guest = fields.Nested(GuestSchema)        