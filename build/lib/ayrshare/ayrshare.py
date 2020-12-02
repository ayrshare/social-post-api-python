import requests
from urllib.parse import urlencode

base = 'https://app.ayrshare.com/api/'

ERROR_MSG = {
    "status": "error",
    "message": "Wrong parameters. Please check at https://docs.ayrshare.com/rest-api/endpoints",
}

def doPost(type, data, headerData):
    payload = data
    headers = headerData
    r = requests.post(base + type, json=payload, headers=headers)
    return r.json()


def doGet(type, params, headerData):
    headers = headerData
    r = requests.get("{}{}?{}".format(
        base, type, urlencode(params)), headers=headers)
    return r.json()


def doDelete(type, data, headerData):
    payload = data
    headers = headerData
    r = requests.delete(base + type, json=payload, headers=headers)
    return r.json()


class SocialPost:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + API_KEY}

    def post(self, data):
        if "post" not in data or "platforms" not in data:
            return ERROR_MSG

        return doPost("post", data, self.headers)

    def delete(self, data):
        if "id" not in data and "bulk" not in data:
            return ERROR_MSG

        return doDelete("delete", data, self.headers)

    def history(self, params={}):
        return doGet("history", params, self.headers)

    def media(self, params={}):
        return doGet("media", params, self.headers)

    def analytics(self, params={}):
        return doGet("analytics", params, self.headers)

    def user(self, params={}):
        return doGet("user", params, self.headers)

    def upload(self, data):
        if "file" not in data:
            return ERROR_MSG

        return doPost("upload", data, self.headers)

    def shorten(self, data):
        if "url" not in data:
            return ERROR_MSG

        return doPost("shorten", data, self.headers)

    def addFeed(self, data):
        if "url" not in data:
            return ERROR_MSG

        return doPost("feed", data, self.headers)

    def deleteFeed(self, data):
        if "id" not in data:
            return ERROR_MSG

        return doDelete("feed", data, self.headers)

    def createProfile(self, data):
        if "title" not in data:
            return ERROR_MSG

        return doPost("create-profile", data, self.headers)

    def deleteProfile(self, data):
        if "profileKey" not in data:
            return ERROR_MSG

        return doDelete("delete-profile", data, self.headers)
