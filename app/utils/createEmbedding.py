from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
import os
from scipy.spatial.distance import cosine
from datetime import datetime
import time


# Initialize the model for embeddings
model = SentenceTransformer('all-mpnet-base-v2')  # Choose the appropriate model

# MongoDB setup
# client = MongoClient(os.getenv("MONGODB_URI"))
# client = MongoClient("mongodb://joel:7092824762joel@sampledb-shard-00-00.z2dfw.mongodb.net:27017,sampledb-shard-00-01.z2dfw.mongodb.net:27017,sampledb-shard-00-02.z2dfw.mongodb.net:27017/?ssl=true&replicaSet=atlas-dfe532-shard-0&authSource=admin&retryWrites=true&w=majority&appName=sampleDb")  # Adjust with your MongoDB URI
# db = client["personalFinance"]
# userCollection = db["chatQuestions"]

# Function to create an embedding
def create_embedding(text):
    embedding = model.encode(text)
    return embedding

# Function to insert data with embedding into the database
# def insert_data_with_embedding(data):
    
#     embedding = create_embedding(data["question"])
    
#     epoch_time = int(time.time())
#     questionId = f"GL{epoch_time}"

    
#     data_to_insert = {
#         "questionId": questionId,
#         "question": data.get("question"),
#         "answer": data["answer"],
#         "questionType": data["questionType"],
#         "functionName": data["functionName"],
#         "embedding": embedding.tolist(),
#         "createdDate": datetime.now()
#     }

#     result = userCollection.insert_one(data_to_insert)
    
#     if result.inserted_id:
#         return {"status": "success", "message": "Data inserted successfully!"}
#     else:
#         return {"status": "error", "message": "Failed to insert data!"}

# # Function to find similar data based on embeddings
# def find_similar_data(query_text, user_id):
#     query_embedding = create_embedding(query_text)
    
#     stored_data = userCollection.find({"userId": user_id})

#     best_match = None
#     best_score = float('inf')  # Initialize to a high score (cosine distance)
    
#     for item in stored_data:
#         stored_embedding = item["embedding"]
#         score = cosine(query_embedding, stored_embedding)
        
#         if score < best_score:
#             best_score = score
#             best_match = item
    
#     if best_match:
#         return {"status": "success", "message": "Match found!", "best_match": best_match}
#     else:
#         return {"status": "error", "message": "No similar data found!"}



# # A general finance question with a static answer
# data_static = {
#            "question": "How much can I spend on entertainment this month?",
#     "answer": "You can spend {{variable}} on entertainment this month.",
#     "questionType": "DYNAMIC",
#     "functionName": "calculate_entertainment_budget"
# }

# # Insert static finance question
# response_static = insert_data_with_embedding(data_static)
# print(response_static)

