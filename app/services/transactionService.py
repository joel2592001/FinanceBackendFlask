from pymongo import MongoClient
import os
from ..utils.response import sendResponse

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["personalFinance"]

trancationCollection = db["transations"]


def add_expense(data):
    expense_data = {
        "user_id": data.get("user_id"),
        "amount": float(data.get("amount")),
        "category": data.get("category"),
        "description": data.get("description") or "No description",
        "type": data.get("type"),
    }

    result = trancationCollection.insert_one(expense_data)
    
    print("result::::",result)

    return sendResponse(status="success",message="Expense added successfully!",data={"expense_id": str(result.inserted_id)})

