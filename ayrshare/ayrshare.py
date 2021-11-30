import requests
from urllib.parse import urlencode

base = 'https://app.ayrshare.com/api/'

ERROR_MSG = {
    "status":
    "error",
    "message":
    "Wrong parameters. Please verify at https://docs.ayrshare.com/rest-api/endpoints",
}


def doPost(type, data, headerData):
    data["source"] = "pypi"
    payload = data
    headers = headerData
    r = requests.post(base + type, json=payload, headers=headers)
    return r.json()


def doGet(type, params, headerData):
    params["source"] = "pypi"
    headers = headerData
    r = requests.get("{}{}?{}".format(base, type, urlencode(params)),
                     headers=headers)
    return r.json()


def doDelete(type, data, headerData):
    data["source"] = "pypi"
    payload = data
    headers = headerData
    r = requests.delete(base + type, json=payload, headers=headers)
    return r.json()


class SocialPost:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + API_KEY
        }

    def post(self, data):
        if "post" not in data or "platforms" not in data:
            return ERROR_MSG

        return doPost("post", data, self.headers)

    def delete(self, data):
        if "id" not in data or "bulk" not in data:
            return ERROR_MSG

        return doDelete("delete", data, self.headers)

    def history(self, params={}):
        id = ""

        if 'id' in params:
            id = '/' + params.get('id')

        return doGet("history" + id, params, self.headers)

    def media(self, params={}):
        return doGet("media", params, self.headers)

    def analyticsLinks(self, params={}):
        return doGet("analytics/links", params, self.headers)

    def analyticsPost(self, data):
        if "id" not in data:
            return ERROR_MSG

        return doPost("analytics/post", data, self.headers)

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

        return doPost("profiles/create-profile", data, self.headers)

    def deleteProfile(self, data):
        if "profileKey" not in data:
            return ERROR_MSG

        return doDelete("profiles/delete-profile", data, self.headers)

    def generateJWT(self, data):
        if "domain" not in data or "privateKey" not in data or "profileKey" not in data:
            return ERROR_MSG

        return doPost("profiles/generateJWT", data, self.headers)

    def postComment(self, data):
        if "id" not in data or "platforms" not in data or "comment" not in data:
            return ERROR_MSG

        return doPost("comments", data, self.headers)

    def getComments(self, params={}):
        return doGet("comments", params, self.headers)

    def setAutoSchedule(self, data):
        if "schedule" not in data:
            return ERROR_MSG

        return doPost("auto-schedule/set", data, self.headers)

    def deleteAutoSchedule(self, data):
       return doDelete("auto-schedule/delete", data, self.headers)


    def listAutoSchedule(self, params={}):
        return doGet("auto-schedule/list", params, self.headers)


    def registerWebook(self, data):
        if "action" not in data or "url" not in data:
            return ERROR_MSG

        return doPost("hook/webhook", data, self.headers)

    def unregisterWebhook(self, data):
        if "action" not in data:
            return ERROR_MSG

        return doDelete("hook/webhook", data, self.headers)

    def listWebhooks(self, params={}):
        return doGet("hook/webhook", params, self.headers)

