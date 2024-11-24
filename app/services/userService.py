from pymongo import MongoClient
import os
from ..utils.response import sendResponse
from datetime import datetime
import time
from bcrypt import hashpw, gensalt, checkpw
from ..utils.jwtUtils import generate_jwt_token
from ..utils.createEmbedding import create_embedding

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["personalFinance"]

userCollection = db["users"]
queryCollection = db["chatQuestions"]


def addUser(data):

    user_email = data.get("email").strip().lower()

    existing_user = userCollection.find_one({"email": user_email})
    if existing_user:
        return sendResponse(status="error", message="Email already exists!")

    epoch_time = int(time.time())
    user_id = f"USE{epoch_time}"

    plain_password = data.get("password")
    hashed_password = hashpw(plain_password.encode(
        "utf-8"), gensalt()).decode("utf-8")
    print("hashed_password::", hashed_password)

    user_data = {
        "userId": user_id,
        "name": data.get("name"),
        "financialGoal": [],
        "email": user_email,
        "password": hashed_password,
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


def loginUser(data):
    print("login data inside the service::", data)

    user_email = data.get("email").strip().lower()
    plain_password = data.get("password")

    user = userCollection.find_one({"email": user_email})

    if not user:
        return sendResponse(status="error", message="Invalid email or password!")

    if not checkpw(plain_password.encode("utf-8"), user["password"].encode("utf-8")):
        return sendResponse(status="error", message="Invalid email or password!")

    token = generate_jwt_token(user["userId"])
    print("token::", token)

    return sendResponse(status="success", message="Login successful!", data={"token": token, "userId": user["userId"], "name": user["name"]})


def userQuery(data):

    userQuery = data.get("query")

    query_embedding = create_embedding(userQuery).tolist()
    
    # print("query_embedding::", query_embedding)

    results = queryCollection.aggregate([
        {
            "$vectorSearch": {
                "queryVector": query_embedding,  
                "path": "embedding",                       
                "numCandidates": 10,                      
                "limit": 3,                                
                "index": "financeAI"
            }
        }
    ])

    for result in results:
        print("result::", result["question"], )


