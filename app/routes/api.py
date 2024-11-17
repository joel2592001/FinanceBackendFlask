from flask import Blueprint, request, jsonify

from ..services.userService import addUser, loginUser
from ..schema.userSchema import userSchema, loginUserSchema

from ..services.transactionService import addTransaction, editTransaction, deleteTransaction
from ..schema.transactionSchema import transactionSchema, updateTransactionSchema, deleteTransactionSchema

from ..services.goalService import addGoal
from ..schema.goalSchema import addFinancialGoalSchema


from ..utils.response import sendResponse
from ..utils.validation import validate
from ..utils.asyncHandler import asyncHandler
from ..utils.jwtUtils import jwt_required

api_blueprint = Blueprint("api", __name__)

# Users API
@api_blueprint.route('/addUser', methods=["POST"])
@asyncHandler
def createUser():
    data = request.json

    validated_data, errors = validate(data, userSchema)
    if errors:
        return sendResponse(status="error", message="Validation failed", error=errors)

    response = addUser(validated_data)

    return jsonify(response)

@api_blueprint.route('/loginUser', methods=["POST"])
@asyncHandler
def signinUser():
    data = request.json
    validated_data, errors = validate(data, loginUserSchema)
    if errors:
        return sendResponse(status="error", message="Validation failed", error=errors)

    response = loginUser(validated_data)

    return jsonify(response)

# Transaction API
@api_blueprint.route('/addTransaction', methods=["POST"])
@asyncHandler
@jwt_required
def createTransaction():
    data = request.json

    validated_data, errors = validate(data, transactionSchema)
    if errors:
        return sendResponse(status="error", message="Validation failed", error=errors)

    response = addTransaction(validated_data)

    return jsonify(response)

@api_blueprint.route('/editTransaction', methods=["POST"])
@asyncHandler
@jwt_required
def updateExpense():
    data = request.json
    print(data, "data")
    validated_data, errors = validate(data, updateTransactionSchema)
    if errors:
        return sendResponse(status="error", message="Validation failed", error=errors)

    response = editTransaction(validated_data)

    return jsonify(response)

@api_blueprint.route('/deleteTransaction', methods=["POST"])
@asyncHandler
@jwt_required
def removeExpense():
    data = request.json
    
    validated_data, errors = validate(data, deleteTransactionSchema)
    if errors:
        return sendResponse(status="error", message="Validation failed", error=errors)

    response = deleteTransaction(validated_data)

    return jsonify(response)


# Financial Goal API
@api_blueprint.route('/addGoal', methods=["POST"])
@asyncHandler
# @jwt_required
def createGoal():
    data = request.json

    validated_data, errors = validate(data, addFinancialGoalSchema)
    if errors:
        return sendResponse(status="error", message="Validation failed", error=errors)

    response = addGoal(validated_data)

    return jsonify(response)