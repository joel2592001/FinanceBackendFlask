from flask import Blueprint, request, jsonify
from ..services.transactionService import addTransaction
from ..schema.transactionSchema import transactionSchema
from ..utils.response import sendResponse
from ..utils.validation import validate

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route('/addTransaction', methods=["POST"])
def createExpense():
    data = request.json

    validated_data, errors = validate(data, transactionSchema)
    if errors:
        return sendResponse(status="error", message="Validation failed", error=errors)

    response = addTransaction(validated_data)

    return jsonify(response)


