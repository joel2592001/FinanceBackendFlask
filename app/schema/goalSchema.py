addFinancialGoalSchema = {
    "userId": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # # "regex": r"\S+", 
    },
    "goalName": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # # "regex": r"\S+",
    },
    "targetAmount": {
        "type": "float",
        "required": True,
        "min": 1,
    },
    "currentAmount": {
        "type": "float",
        "required": True,
        "min": 1,
    },
    "description": {
        "type": "string",
        "required": False,
        "minlength": 3,
    },
    "startDate": {
        "type": "string",
        "required": True,
        "minlength": 3,
    },
    "endDate": {
        "type": "string",
        "required": True,
        "minlength": 3,
    },
    "status":{
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # "regex": r"\S+",
    }
}


updateFinancialGoalSchema = {
    "userId": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # # "regex": r"\S+", 
    },
    "goalId": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # # "regex": r"\S+", 
    },
    "goalName": {
        "type": "string",
        "required": False,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # # "regex": r"\S+",
    },
    "targetAmount": {
        "type": "float",
        "required": False,
        "min": 1,
    },
    "currentAmount": {
        "type": "float",
        "required": False,
        "min": 1,
    },
    "description": {
        "type": "string",
        "required": False,
        "minlength": 3,
    },
    "startDate": {
        "type": "string",
        "required": False,
        "minlength": 3,
    },
    "endDate": {
        "type": "string",
        "required": False,
        "minlength": 3,
    },
}

deleteFinancialGoalSchema = {
    "userId": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # # "regex": r"\S+", 
    },
    "goalId": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # # "regex": r"\S+", 
    },
}