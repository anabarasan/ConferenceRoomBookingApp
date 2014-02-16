validactions = ['create', 'list', 'update', 'delete']

def errorhandling(action, response):
    if action in validactions:
        response.set_status(405, "Method Not Allowed")
    else:
        response.set_status(400, "Bad Request")