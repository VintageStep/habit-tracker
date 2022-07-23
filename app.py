import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# code starts running here
def create_app():
    app = Flask(__name__)
    # Getting connection string from .env 
    client = MongoClient(os.environ.get("MONGODB_URI"))
    # setting the DDBB
    app.db = client.get_default_database()
    # pages is registered in Blueprints and here we load it
    app.register_blueprint(pages)
    return app

