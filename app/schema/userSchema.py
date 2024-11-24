
userSchema = {
    "name": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # "regex": r"\S+", 
        
    },
    "email": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # "regex": r"\S+", 
    },
    "password": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # "regex": r"\S+", 
    },
    "age": {
        "type": "integer",
        "required": True,
        "min": 1,
    },
    "salary": {
        "type": "float",
        "required": True,
        "min": 1,
    },
    "savings": {
        "type": "float", 
        "required": True,
        "min": 1,
    },
    "accountState": {
        "type": "string",
        "required": True,
        "allowed": ["ACTIVE", "INACTIVE"],
    },
}

loginUserSchema = {
    "email": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # "regex": r"\S+", 
    },
    "password": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # "regex": r"\S+", 
    },
    
}

userQuerySchema = {
    "userId": {
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # "regex": r"\S+", 
    },
    "query":{
        "type": "string",
        "required": True,
        "minlength": 3,
        "nullable": False,
        "empty": False,
        # "regex": r"\S+",
    }
}