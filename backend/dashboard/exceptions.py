class DashboardException(Exception):
    def __init__(self, message, params=None, status=None):
        self.message = message
        self.params = params
        self.status = status


class InvalidInputException(DashboardException):
    pass