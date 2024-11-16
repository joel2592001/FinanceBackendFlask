from cerberus import Validator

def validate(data,schema):
    
    validator = Validator(schema)
    
    if validator.validate(data):
        return data, None 
    else:
        return None, validator.errors 