import json
import requests


class ResponseLogger(object):
    """ Class to log details about HTTP request responses """

    def __init__(self, indent=4):
        self.updateIndent(indent)

    def updateIndent(self, newValue):
        self.indent = newValue
        if newValue > 0:
            self.indentToken = ""
            for i in range(1, newValue):
                self.indentToken += " "
        else:
            self.indentToken = ""

    def log(self, request):
        print("Response headers: ")
        print("{")
        for header, val in request.headers.items():
            print(self.indentToken + header + ": " + val)
        print("}")

        print("Response body: ")
        print(json.dumps(request.json(), indent=self.indent))
