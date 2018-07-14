import getpass
import json

from api import Api
from user_auth import UserAuth

# Config
user_data_filename = "user_data.txt"

# Create initial model of user authentication from file
user_data = UserAuth()
user_data.load(user_data_filename)

# Create api wrapper
api = Api()

# If the cached user credentials are valid, use them
if user_data.is_valid():
    print("Read cached user authentication from " + user_data_filename)
    print("Username: " + user_data.username)
    print("Oauth token: " + user_data.token)
# Otherwise get info from the user to create a new access token
else:
    username = input("Enter your Github username: ")
    password = getpass.getpass("Enter your Github password: ")

    # Make api call to create an access token
    print("Issuing request to create an Oauth token...")
    token_json = api.create_token(username, password)
    print("Success! Your authorization has succeeded")

    # Save the created token in memory to continue using it
    user_data.token = token_json["token"]

    # Add the entered username to the token dictionary and save the whole thing
    # to a file
    token_json["username"] = username
    with open(user_data_filename, 'w') as user_file:
        json.dump(token_json, user_file)

print("Issuing request to create your repository...")
repo_json = api.create_repo(user_data)
print()
