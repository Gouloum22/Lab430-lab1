"""
User DAO MongoDB (Data Access Object)
Auteur : Dyaa Abou Arida, 2026
"""
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from models.user import User
from bson import ObjectId

class UserDAOMongo:
    def __init__(self):
        try:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            env_path = os.path.join(base_dir, ".env")
            load_dotenv(dotenv_path=env_path)

            db_host = os.getenv("MONGODB_HOST")
            db_name = os.getenv("MYSQL_DB_NAME")
            db_username = os.getenv("DB_USERNAME")
            db_password = os.getenv("DB_PASSWORD")

            connection_string = f"mongodb://{db_username}:{db_password}@{db_host}:27017/"

            self.client = MongoClient(connection_string)
            self.db = self.client[db_name]
            self.collection = self.db["users"]

        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """
        rows = self.collection.find()
        return [
            User(str(row["_id"]), row["name"], row["email"])
            for row in rows
        ]

    def insert(self, user):
        """ Insert given user into MongoDB """
        new_user = {
            "name": user.name,
            "email": user.email
        }
        result = self.collection.insert_one(new_user)
        return str(result.inserted_id)

    def update(self, user):
        """ Update given user in MongoDB """
        filtre = {"_id": ObjectId(user.id)}
        modification = {"$set": {"name": user.name, "email": user.email}}

        self.collection.update_one(filtre, modification)

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        user_info = {
            "_id": ObjectId(user_id)
        }
        
        self.collection.delete_one(user_info)

    def delete_all(self): # extra
        """ Empty users table in MongoDB """
        self.collection.delete_many({})
        
    def close(self):
        self.client.close()