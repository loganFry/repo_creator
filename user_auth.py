import json

class UserAuth:
    """ Class to contain all authentication information for a user """

    def __init__(self, username=None, token=None):
        self.username = username
        self.token = token

    def load(self, filename):
        try:
            with open(filename) as current_file:
                file_data = json.load(current_file)
                self.username = file_data["username"]
                self.token = file_data["token"]
        except FileNotFoundError:
            print("File does not exist")

    def is_valid(self):
        valid = self.username is not None and self.token is not None
        return valid


