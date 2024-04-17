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
    data["source"] = "pypi"
    payload = data
    headers = headerData
    r = requests.post(base + type, json=payload, headers=headers)
    return r.json()

def doPut(type, data, headerData):
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
    params["source"] = "pypi"
    headers = headerData
    r = requests.get("{}{}?{}".format(base, type, urlencode(buildParams(params))),
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
        return doPost("post", data, self.headers)

    def delete(self, data):
        return doDelete("delete", data, self.headers)
        
    def getPost(self, data):
        id = ""

        if 'id' in data:
            id = '/' + data.get('id')

        return doGet("post" + id, data, self.headers)
    
    def retryPost(self, data):
        return doPut("post/retry", data, self.headers)
    
    def updatePost(self, data):
        return doPut("post", data, self.headers)

    def history(self, params={}):
        id = ""

        if 'id' in params:
            id = '/' + params.get('id')

        return doGet("history" + id, params, self.headers)

    def media(self, params={}):
        return doGet("media", params, self.headers)
    
    def verifyMediaExists(self, params={}):
        return doPost("media/urlExists", params, self.headers)
    
    def mediaUploadUrl(self, params={}):
        return doGet("media/uploadUrl", params, self.headers)
    
    def mediaMeta(self, params={}):
        return doGet("media/meta", params, self.headers)
    
    def resizeImage(self, data):
        return doPost("media/resize", data, self.headers)

    def analyticsLinks(self, params={}):
        return doGet("analytics/links", params, self.headers)

    def analyticsPost(self, data):
        return doPost("analytics/post", data, self.headers)
    
    def analyticsSocial(self, params={}):
        return doPost("analytics/social", params, self.headers)

    def user(self, params={}):
        return doGet("user", params, self.headers)

    def upload(self, data):
        return doPost("upload", data, self.headers)

    def shorten(self, data):
        return doPost("shorten", data, self.headers)

    def addFeed(self, data):
        return doPost("feed", data, self.headers)

    def deleteFeed(self, data):
        return doDelete("feed", data, self.headers)
    
    def getFeeds(self, params={}):
        return doGet("feed", params, self.headers)
    
    def updateFeed(self, data):
        return doPut("feed", data, self.headers)

    def createProfile(self, data):
        return doPost("profiles/create-profile", data, self.headers)

    def deleteProfile(self, data):
        return doDelete("profiles/delete-profile", data, self.headers)
    
    def updateProfile(self, data):
        return doPut("profiles/profile", data, self.headers)
    
    def getProfiles(self, params={}):
        return doGet("profiles", params, self.headers)

    def generateJWT(self, data):
        return doPost("profiles/generateJWT", data, self.headers)
    
    def unlinkSocial(self, data):
        return doDelete("profiles/social", data, self.headers)

    def postComment(self, data):
        return doPost("comments", data, self.headers)

    def getComments(self, params={}):
        id = ""

        if 'id' in params:
            id = '/' + params.get('id')

        return doGet("comments" + id, params, self.headers)
    
    def deleteComments(self, data):
        id = ""

        if 'id' in data:
            id = '/' + data.get('id')

        return doDelete("comments" + id, data, self.headers)
    
    def replyComment(self, data):
        return doPost("comments/reply", data, self.headers)

    def setAutoSchedule(self, data):
        return doPost("auto-schedule/set", data, self.headers)

    def deleteAutoSchedule(self, data):
       return doDelete("auto-schedule/delete", data, self.headers)


    def listAutoSchedule(self, params={}):
        return doGet("auto-schedule/list", params, self.headers)


    def registerWebhook(self, data):
        return doPost("hook/webhook", data, self.headers)

    def unregisterWebhook(self, data):
        return doDelete("hook/webhook", data, self.headers)

    def listWebhooks(self, params={}):
        return doGet("hook/webhook", params, self.headers)
    
    def getBrandByUser(self, params={}):
        return doGet("brand/byUser", params, self.headers)
    
    def generatePost(self, params):
        return doPost("generate/post", params, self.headers)
    
    def generateRewrite(self, params):
        return doPost("generate/rewrite", params, self.headers)
    
    def generateTranscription(self, params):
        return doPost("generate/transcription", params, self.headers)
    
    def generateTranslation(self, params):
        return doPost("generate/translate", params, self.headers)
    
    def generateAltText(self, params):
        return doPost("generate/altText", params, self.headers)
    
    def autoHashtags(self, params):
        return doPost("hashtags/auto", params, self.headers)
    
    def recommendHashtags(self, params):
        return doGet("hashtags/recommend", params, self.headers)
    
    def checkBannedHashtags(self, params):
        return doGet("hashtags/banned", params, self.headers)
    
    def shortLink(self, params):
        return doPost("links", params, self.headers)
    
    def shortLinkAnalytics(self, params):
        id = ""

        if 'id' in params:
            id = '/' + params.get('id')

        return doGet("links" + id, params, self.headers)
    
    def reviews(self, params):
        return doGet("reviews", params, self.headers)
    
    def review(self, params):
        id = ""

        if 'id' in params:
            id = '/' + params.get('id')

        return doGet("reviews" + id, params, self.headers)
    
    def reviewReply(self, params):
        return doPost("reviews", params, self.headers)
    
    def deleteReviewReply(self, params):
        return doDelete("reviews", params, self.headers)

