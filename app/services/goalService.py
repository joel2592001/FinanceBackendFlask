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


def editGoal(data):

    update_fields = {f"financialGoal.$.{key}": value for key,
                     value in data.items() if key != "userId" and key != "goalId"}
    
    update_fields["financialGoal.$.updatedDate"] = datetime.now()
    
    if len(update_fields) <= 1:  
        return sendResponse(status="error", message="At least one field must be updated!")
    
    print("update_fields::", update_fields)

    result = userCollection.update_one(
        {"userId": data["userId"], "financialGoal.goalId": data["goalId"]},
        {"$set": update_fields}
    )

    print("result::", result.matched_count, result.modified_count)

    if result.matched_count == 0:
        return sendResponse(status="error", message="Goal not found or user does not exist!")
    elif result.modified_count == 0:
        return sendResponse(status="error", message="No changes were made to the goal!")
    else:
        return sendResponse(status="success", message="Goal updated successfully!")


def deleteGoal(data):

    user_id = data.get("userId")
    goal_id = data.get("goalId")

    result = userCollection.update_one(
        {"userId": user_id, "financialGoal.goalId": goal_id},
        {"$pull": {"financialGoal": {"goalId": goal_id}}}
    )

    if result.modified_count > 0:
        return sendResponse(status="success", message="Goal deleted successfully!")
    else:
        return sendResponse(status="error", message="Goal not found or could not be deleted.")
