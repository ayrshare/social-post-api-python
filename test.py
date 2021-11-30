import json, pprint
from ayrshare import SocialPost

# Add your API Key in a file names API-KEY.json { 'key': 'API KEY'}
with open('./API-KEY.json') as f:
    API_KEY = json.load(f)

social = SocialPost(API_KEY["key"])
pp = pprint.PrettyPrinter(indent=4)

# Post to Platforms
postResult = social.post({'post': 'The best post ever!', 'platforms': ['twitter']})
print(postResult)

# Delete the Post
deleteResult = social.delete({'id': postResult['id']})
print(deleteResult)

# Get History
# print(social.history())
