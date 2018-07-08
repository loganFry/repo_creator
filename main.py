import requests
from requests.auth import HTTPBasicAuth
import json

username = input("Enter your GitHub username: ")
password = input("Enter your Github password: ")
print("Issuing request to create an Oauth token...")
r_data = { "scopes": ["repo", "user"], "note": "test repo_creator token" }
token_r = requests.post("https://api.github.com/authorizations", 
                        json=r_data, 
                        auth=HTTPBasicAuth(username, password))
parsed_json = json.loads(token_r.text)
print(token_r)
print(json.dumps(parsed_json, indent=4))
