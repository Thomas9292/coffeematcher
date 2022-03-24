class MatchingError(Exception):
    """Error raised when matching fails"""

    message = "\nOops\n\nThe non-deterministic matching algorithm did not find a viable solution. Please rerun the script to try again.\n"
