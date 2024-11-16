from pymongo import MongoClient
import os
from ..utils.response import sendResponse
from datetime import datetime
import time

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["personalFinance"]

userCollection = db["users"]


def addUser(data):

    epoch_time = int(time.time())
    user_id = f"USE{epoch_time}"

    user_data = {
        "userId": user_id,
        "name": data.get("name"),
        "email": data.get("email"),
        "password": data.get("password"),
        "age": data.get("age"),
        "salary": data.get("salary"),
        "savings": data.get("savings"),
        "accountState": data.get("accountState"),
        "createdDate": datetime.now(),
    }

    result = userCollection.insert_one(user_data)

    if result.inserted_id:
        return sendResponse(status="success", message="User added successfully!")
    else:
        return sendResponse(status="error", message="Failed to add user!")
