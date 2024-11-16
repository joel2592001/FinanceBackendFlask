from pymongo import MongoClient
import os
from ..utils.response import sendResponse
from datetime import datetime
import time

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["personalFinance"]

trancationCollection = db["transactions"]


def addTransaction(data):

    epoch_time = int(time.time())  

    transaction_prefix = "IN" if data.get("type") == "Income" else "EX"
    transaction_id = f"{transaction_prefix}{epoch_time}"
    
    expense_data = {
        "user_id": data.get("user_id"),
        "trancactionId": transaction_id,
        "amount": float(data.get("amount")),
        "category": data.get("category"),
        "description": data.get("description") or "No description",
        "type": data.get("type"),
        "createdDate": datetime.now(),
    }

    result = trancationCollection.insert_one(expense_data)
    
    print("result::::",result)

    return sendResponse(status="success",message="Transactions added successfully!")


