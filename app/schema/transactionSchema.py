
expenseSchema = {
    "user_id": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        "regex": r"\S+", 
    },
    "amount": {
        "type": "float",
        "required": True,
        "min": 1,
    },
    "category": {
        "type": "string",
        "required": True,
        "allowed": [
            "Food", "Travelling", "Shopping", "Entertainment",
            "Insurance", "Other", "Rent", "Investment",
            "Salary", "Passive income", "Returns"
        ],
    },
    "description": {
        "type": "string",
        "required": False,
        "minlength": 3,
    },
    "type": {
        "type": "string",
        "required": True,
        "allowed": ["Income", "Expense"],
    },
}

