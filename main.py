import requests
from requests.auth import HTTPBasicAuth
import json
import getpass

user_data = {}
try:
    with open('user_data.txt') as user_file:
        print("Found user data file, attempting to parse")
        user_data = json.load(user_file)
except FileNotFoundError:
    print("User data file does not exist")

if "username" in user_data and "token" in user_data:
    print("Cached user data: ")
    print("Username: " + user_data["username"])
    print("Oauth token: " + user_data["token"])
else:
    username = input("Enter your GitHub username: ")
    password = getpass.getpass("Enter your Github password: ")
    print("Issuing request to create an Oauth token...")
    r_data = { "scopes": ["repo", "user"], "note": "repo_creator token" }
    token_r = requests.post("https://api.github.com/authorizations", 
                            json=r_data, 
                            auth=HTTPBasicAuth(username, password))
    parsed_json = token_r.json()
    print("Token request response: ")
    print(token_r)
    print(token_r.headers)
    print(json.dumps(parsed_json, indent=4))
    parsed_json["username"] = username
    with open('user_data.txt', 'w') as user_file:
        json.dump(parsed_json, user_file)
