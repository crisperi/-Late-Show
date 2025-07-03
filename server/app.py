from flask import Flask, request, jsonify
from flask_cors import CORS
from extensions import db, ma, migrate
from flask_restful import Api
from dotenv import load_dotenv
import os 

from resources.episodes import Episodes
from resources.guests import Guests
from resources.appearances import Appearances

# Load environment variables
load_dotenv()

# Initialize the app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Enable CORS
CORS(app)


#INIT EXTENSIONS
db.init_app(app)
ma.init_app(app)      
migrate.init_app(app, db)

# Initialize Flask-RESTful API
api = Api(app)

# Add resource routes
api.add_resource(Episodes, '/episodes', '/episodes/<int:id>')
api.add_resource(Guests, '/guests')
api.add_resource(Appearances, '/appearances')

# Run the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
