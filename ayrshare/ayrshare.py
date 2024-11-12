import requests
from urllib.parse import urlencode

base = 'http://localhost:5001/ayrshare-dev/us-central1/api/'
#'https://app.ayrshare.com/api/'

ERROR_MSG = {
    "status":
    "error",
    "message":
    "Wrong parameters. Please verify at https://docs.ayrshare.com/rest-api/endpoints",
}

def doPost(type, data, headerData):
    if data is None:
        data = {}

    data["source"] = "pypi"
    payload = data
    headers = headerData
    r = requests.post(base + type, json=payload, headers=headers)
    return r.json()

def doPut(type, data, headerData):
    if data is None:
        data = {}

    data["source"] = "pypi"
    payload = data
    headers = headerData
    r = requests.put(base + type, json=payload, headers=headers)
    return r.json()

# Build the parameters for the request and handle arrays
def buildParams (data) :
    params = {}
    for key, value in data.items():
        if type(value) is list:
            for i in range(len(value)):
                params[key + "[" + str(i) + "]"] = value[i]
        else:
            params[key] = value
    return params

def doGet(type, params, headerData):
    if params is None:
        params = {}

    params["source"] = "pypi"
    headers = headerData
    r = requests.get("{}{}?{}".format(base, type, urlencode(buildParams(params))),
                     headers=headers)
    return r.json()


def doDelete(type, data, headerData):
    if data is None:
        data = {}

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

    def post(self, data, headers=None):
        return doPost("post", data, self.headers)

    def delete(self, data=None):
        return doDelete("delete", data, self.headers)
        
    def getPost(self, data=None):
        if data is None:
            data = {}

        id = ""

        if 'id' in data:
            id = '/' + data.get('id')

        return doGet("post" + id, data, self.headers)
    
    def retryPost(self, data=None):
        return doPut("post/retry", data, self.headers)
    
    def updatePost(self, data=None):
        return doPut("post", data, self.headers)

    def history(self, params=None):
        if params is None:
            params = {}

        id = ""

        if 'id' in params:
            id = '/' + params.get('id')

        return doGet("history" + id, params, self.headers)

    def media(self, params=None):
        return doGet("media", params, self.headers)
    
    def verifyMediaExists(self, params=None):
        return doPost("media/urlExists", params, self.headers)
    
    def mediaUploadUrl(self, params=None):
        return doGet("media/uploadUrl", params, self.headers)
    
    def mediaMeta(self, params=None):
        return doGet("media/meta", params, self.headers)
    
    def resizeImage(self, data=None):
        return doPost("media/resize", data, self.headers)

    def analyticsLinks(self, params=None):
        return doGet("analytics/links", params, self.headers)

    def analyticsPost(self, data=None):
        return doPost("analytics/post", data, self.headers)
    
    def analyticsSocial(self, params=None):
        return doPost("analytics/social", params, self.headers)

    def user(self, params=None):
        return doGet("user", params, self.headers)

    def upload(self, data=None):
        return doPost("upload", data, self.headers)

    def shorten(self, data=None):
        return doPost("shorten", data, self.headers)

    def addFeed(self, data=None):
        return doPost("feed", data, self.headers)

    def deleteFeed(self, data=None):
        return doDelete("feed", data, self.headers)
    
    def getFeeds(self, params=None):
        return doGet("feed", params, self.headers)
    
    def updateFeed(self, data=None):
        return doPut("feed", data, self.headers)

    def createProfile(self, data=None):
        return doPost("profiles/create-profile", data, self.headers)

    def deleteProfile(self, data=None):
        return doDelete("profiles/delete-profile", data, self.headers)
    
    def updateProfile(self, data=None):
        return doPut("profiles/profile", data, self.headers)
    
    def getProfiles(self, params=None):
        return doGet("profiles", params, self.headers)

    def generateJWT(self, data=None):
        return doPost("profiles/generateJWT", data, self.headers)
    
    def unlinkSocial(self, data=None):
        return doDelete("profiles/social", data, self.headers)

    def postComment(self, data=None):
        return doPost("comments", data, self.headers)

    def getComments(self, params=None):
        if params is None:
            params = {}

        id = ""

        if 'id' in params:
            id = '/' + params.get('id')

        return doGet("comments" + id, params, self.headers)
    
    def deleteComments(self, data=None):
        if data is None:
            data = {}

        id = ""

        if 'id' in data:
            id = '/' + data.get('id')

        return doDelete("comments" + id, data, self.headers)
    
    def replyComment(self, data=None):
        return doPost("comments/reply", data, self.headers)

    def setAutoSchedule(self, data=None):
        return doPost("auto-schedule/set", data, self.headers)

    def deleteAutoSchedule(self, data=None):
       return doDelete("auto-schedule/delete", data, self.headers)


    def listAutoSchedule(self, params=None):
        return doGet("auto-schedule/list", params, self.headers)


    def registerWebhook(self, data=None):
        return doPost("hook/webhook", data, self.headers)

    def unregisterWebhook(self, data=None):
        return doDelete("hook/webhook", data, self.headers)

    def listWebhooks(self, params=None):
        return doGet("hook/webhook", params, self.headers)
    
    def getBrandByUser(self, params=None):
        return doGet("brand/byUser", params, self.headers)
    
    def generatePost(self, params=None):
        return doPost("generate/post", params, self.headers)
    
    def generateRewrite(self, params=None):
        return doPost("generate/rewrite", params, self.headers)
    
    def generateTranscription(self, params=None):
        return doPost("generate/transcription", params, self.headers)
    
    def generateTranslation(self, params=None):
        return doPost("generate/translate", params, self.headers)
    
    def generateAltText(self, params=None):
        return doPost("generate/altText", params, self.headers)
    
    def autoHashtags(self, params=None):
        return doPost("hashtags/auto", params, self.headers)
    
    def recommendHashtags(self, params=None):
        return doGet("hashtags/recommend", params, self.headers)
    
    def checkBannedHashtags(self, params=None):
        return doGet("hashtags/banned", params, self.headers)
    
    def shortLink(self, params=None):
        return doPost("links", params, self.headers)
    
    def shortLinkAnalytics(self, params=None):
        if params is None:
            params = {}

        id = ""

        if 'id' in params:
            id = '/' + params.get('id')

        return doGet("links" + id, params, self.headers)
    
    def reviews(self, params=None):
        return doGet("reviews", params, self.headers)
    
    def review(self, params=None):
        if params is None:
            params = {}

        id = ""

        if 'id' in params:
            id = '/' + params.get('id')

        return doGet("reviews" + id, params, self.headers)
    
    def reviewReply(self, params=None):
        return doPost("reviews", params, self.headers)
    
    def deleteReviewReply(self, params=None):
        return doDelete("reviews", params, self.headers)

