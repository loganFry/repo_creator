import json
import getpass
from user_auth import UserAuth
from api import Api

user_data_filename = "user_data.txt"
user_data = UserAuth()
user_data.load(user_data_filename)
base_url = "https://api.github.com"

if user_data.is_valid():
    print("Read cached user authentication from " + user_data_filename)
    print("Username: " + user_data.username)
    print("Oauth token: " + user_data.token)
else:
    username = input("Enter your Github username: ")
    password = getpass.getpass("Enter your Github password: ")    
    api = Api()
    print("Issuing request to create an Oauth token...")
    token_json = api.create_token(username, password, debug=False)
    print("Success! Your authorization has succeeded")
    user_data.token = token_json["token"]
    token_json["username"] = username
    with open(user_data_filename, 'w') as user_file:
        json.dump(token_json, user_file)
