from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from extensions import db

class Guest(db.Model):
    
    __tablename__="guests"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String)
    
    
    appearances = db.relationship('Appearance',
                                  back_populates='guest',
                                  cascade="all, delete-orphan")
    
  
    
    
    def __repr__(self):
        return f"<Guest id is :{self.id},name is :{self.name}>"
    
class Episode(db.Model):
    
    __tablename__="episodes"
    
    id= db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    
    

    appearances = db.relationship('Appearance', back_populates='episode', cascade="all, delete-orphan")
    
    
    def __repr__(self):
        return f"<Episode id is :{self.id},title is :{self.title}>"
    
class Appearance(db.Model):
    
    __tablename__="appearances"        
    
    id = db.Column(db.Integer, primary_key=True)
    rating= db.Column(db.Float, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    
    
    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')
    
    @validates('rating')
    def validate_rating(self, key, rating):
        if not (0 <= rating <= 5):
            raise ValueError("Rating must be between 0 and 5")
        return rating
    
    def __repr__(self):
        return f"<Appearance id is :{self.id}>"