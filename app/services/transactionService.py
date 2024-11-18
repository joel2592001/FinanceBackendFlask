from pymongo import MongoClient
import os
from ..utils.response import sendResponse
from datetime import datetime
import time

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["personalFinance"]

transactionCollection = db["transactions"]


def addTransaction(data):

    epoch_time = int(time.time())

    transaction_prefix = "IN" if data.get("type") == "Income" else "EX"
    transaction_id = f"{transaction_prefix}{epoch_time}"

    expense_data = {
        "userId": data.get("userId"),
        "transactionId": transaction_id,
        "amount": float(data.get("amount")),
        "category": data.get("category"),
        "description": data.get("description") or "No description",
        "type": data.get("type"),
        "createdDate": datetime.now(),
    }

    result = transactionCollection.insert_one(expense_data)

    if result.inserted_id:
        return sendResponse(status="success", message="Transactions added successfully!")
    else:
        return sendResponse(status="error", message="Failed to add transactions!")


def editTransaction(data):

    expense_data = {}

    if "amount" in data:
        expense_data["amount"] = float(data["amount"])
    if "category" in data:
        expense_data["category"] = data["category"]
    if "description" in data:
        expense_data["description"] = data["description"] or "No description"
    if "type" in data:
        expense_data["type"] = data["type"]

    expense_data["updatedDate"] = datetime.now()
    
    result = transactionCollection.update_one(
        {"userId": data["userId"],"transactionId": data["transactionId"]},  
        {"$set": expense_data} 
    )
    
    if result.matched_count == 0:
        return sendResponse(status="error", message="Transaction not found or user does not exist!")
    elif result.modified_count == 0:
        return sendResponse(status="error", message="No changes made!")
    else:
        return sendResponse(status="success", message="Transactions edited successfully!")



def deleteTransaction(data):
    
    result = transactionCollection.delete_one(
        {"userId": data["userId"], "transactionId": data["transactionId"]}
    )

    if result.deleted_count == 0:
        return sendResponse(status="error", message="Transaction not found")
    else:
        return sendResponse(status="success", message="Transaction deleted successfully!")