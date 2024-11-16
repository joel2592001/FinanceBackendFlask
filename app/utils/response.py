def sendResponse(status="success", message="", data=None, error=None):
    response = {
        "status": status,
        "message": message,
        "data": data,  # Default to empty dict if no data
        "error": error  # Default to empty dict if no error
    }
    return response  # Return the dictionary, not a Response object

