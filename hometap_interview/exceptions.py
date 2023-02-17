class NotFoundException(Exception):
    """
    Generic exception for handling 404's.  Handled in the Flask app as a reqistered error handler.
    """


class RequiredParametersMissing(Exception):
    """
    Generic exception for handling bad requests where required query params are missing.  
    Handled in the Flask app as a registered error handler
    """
