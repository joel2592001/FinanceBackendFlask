from flask import Blueprint, request, jsonify

from ..schema.userSchema import userSchema
from ..services.userService import addUser

from ..services.transactionService import addTransaction, editTransaction, deleteTransaction
from ..schema.transactionSchema import transactionSchema, updateTransactionSchema, deleteTransactionSchema

from ..utils.response import sendResponse
from ..utils.validation import validate
from ..utils.asyncHandler import asyncHandler

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





# Transaction API
@api_blueprint.route('/addTransaction', methods=["POST"])
@asyncHandler
def createTransaction():
    data = request.json

    validated_data, errors = validate(data, transactionSchema)
    if errors:
        return sendResponse(status="error", message="Validation failed", error=errors)

    response = addTransaction(validated_data)

    return jsonify(response)


@api_blueprint.route('/editTransaction', methods=["POST"])
@asyncHandler
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
def removeExpense():
    data = request.json
    
    validated_data, errors = validate(data, deleteTransactionSchema)
    if errors:
        return sendResponse(status="error", message="Validation failed", error=errors)

    response = deleteTransaction(validated_data)

    return jsonify(response)
