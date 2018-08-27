import uuid
import requests
from requests.auth import HTTPBasicAuth
from request_logger import ResponseLogger


class Api(object):
    """ Wrapper to handle GitHub Api calls """

    _base_url = "https://api.github.com"
    _authorizations_url = "/authorizations"
    _repos_url = "/user/repos"

    def __init__(self, log_requests=True):
        self.logger = ResponseLogger()
        self.log_requests = log_requests

    def create_token(self,
                     username,
                     password,
                     scopes=["repo", "user"],
                     note="repo_creator token " + str(uuid.uuid4())):
        options = {"scopes": scopes, "note": note}
        token_r = requests.post(
            self._base_url + self._authorizations_url,
            json=options,
            auth=HTTPBasicAuth(username, password))
        if self.log_requests:
            self.logger.log(token_r)
        return token_r.json()

    def create_repo(self,
                    auth,
                    name="TestRepo" + str(uuid.uuid4()),
                    description="A repository created by repo_creator",
                    private=False,
                    auto_init=False):
        # api options for creating repository
        options = {
            "name": name,
            "description": description,
            "private": private,
            "auto_init": auto_init
        }

        # include token to authenticate as user
        headers = { "Authorization": "token " + auth.token }

        # api url should match base_url/user/repos
        full_url = self._base_url + self._repos_url

        repo_r = requests.post(full_url, headers=headers, json=options)

        if self.log_requests:
            print("Url: " + full_url)
            print("Headers: " + str(headers))
            print("JSON: " + str(options))
            self.logger.log(repo_r)
        return repo_r.json()
