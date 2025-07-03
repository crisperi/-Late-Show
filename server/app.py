from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from dotenv import load_dotenv
import os

from models import db
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

# Initialize database and migrations

db = SQLAlchemy()

migrate = Migrate()
ma= Marshmallow()


# Initialize Flask-RESTful API
api = Api(app)

#INIT EXTENSIONS
db.init_app(app)
ma.init_app(app)      
migrate.init_app(app, db)


# Root route
@app.route('/')
def index():
    return "<h1>Welcome to the Late Show API</h1>"

# Add resource routes
api.add_resource(Episodes, '/episodes', '/episodes/<int:id>')
api.add_resource(Guests, '/guests')
api.add_resource(Appearances, '/appearances')

# Run the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
