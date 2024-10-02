class DatabaseError(Exception):
    """Exception for database errors"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"DatabaseError, detail: {self.message}"
