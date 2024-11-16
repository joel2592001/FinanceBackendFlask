from flask import Blueprint, request, jsonify
from ..services.transactionService import add_expense
from ..schema.transactionSchema import expenseSchema
from ..utils.response import sendResponse
from ..utils.validation import validate

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route('/addExpense', methods=["POST"])
def create_expense():
    data = request.json

    validated_data, errors = validate(data,expenseSchema) 
    if errors:
        return sendResponse(status="error",message="Validation failed",error=errors)

    response = add_expense(validated_data)  
    
    return jsonify(response)
