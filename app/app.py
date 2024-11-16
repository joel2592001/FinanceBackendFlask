from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Flask app and MongoDB client
def create_app():
    app = Flask(__name__)

    # Get the MongoDB URI from the environment
    mongo_uri = os.getenv("MONGODB_URI")
    client = MongoClient(mongo_uri)
    db = client["personalFinance"]  # Set the specific database name

    # Check MongoDB connection
    try:
        client.admin.command("ping")
        print("MongoDB connected successfully!")
    except Exception as e:
        print("MongoDB connection failed:", e)

    app.config["db"] = db

    # Register routes
    from .routes.api import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
