import requests
from requests.auth import HTTPBasicAuth
import uuid
import json

class Api:
    """ Wrapper to handle GitHub Api calls """

    _base_url = "https://api.github.com"
    _authorizations_url = "/authorizations"

    def __init__(self):
        pass

    def create_token(self, username, password, 
                    scopes=["repo", "user"], 
                    note="repo_creator token " + str(uuid.uuid4()),
                    debug=True):        
        r_data = { "scopes": scopes, "note": note }
        token_r = requests.post(self._base_url + self._authorizations_url, 
                json=r_data, 
                auth=HTTPBasicAuth(username, password))
        parsed_body = token_r.json()
        if debug:
            print("Response headers: ")
            for header, val in token_r.headers.items():
                print("    " + header + ": " + val)                    
            print("Response body: ")
            print(json.dumps(parsed_body, indent=4))
        return parsed_body
