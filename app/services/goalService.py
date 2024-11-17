from pymongo import MongoClient
import os
from ..utils.response import sendResponse
from datetime import datetime
import time


client = MongoClient(os.getenv("MONGODB_URI"))
db = client["personalFinance"]

userCollection = db["users"]


def addGoal(data):

    userId = data.get("userId")
    goalName = data.get("goalName").strip().lower()
    epoch_time = int(time.time())
    goalId = f"GL{epoch_time}"

    goalData = {
        "goalId": goalId,
        "goalName": goalName,
        "targetAmount": float(data.get("targetAmount")),
        "currentAmount": float(data.get("currentAmount")),
        "description": data.get("description") or "No description",
        "status": data.get("status"),
        "createdDate": datetime.now(),
        "startDate": data.get("startDate"),
        "endDate": data.get("endDate"),
    }

    # result = userCollection.update_one({"userId": userId}, {"$push": {"financialGoal": goalData}})

    result = userCollection.update_one(
        {
            "userId": userId,
            "financialGoal.goalName": {"$ne": goalName}
        },
        {
            "$push": {
                "financialGoal": goalData
            }
        }
    )

    if result.modified_count > 0:
        return sendResponse(status="success", message="Goal added successfully!")
    else:
        return sendResponse(status="error", message="Goal already exists or failed to add!")
