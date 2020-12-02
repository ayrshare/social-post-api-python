import json
from ayrshare import SocialPost

with open('./API-KEY.json') as f:
    API_KEY = json.load(f)

social = SocialPost(API_KEY["key"])

# Post to Platforms
postResult = social.post({'post': 'Nice Posting 2', 'platforms': ['twitter']})
print(postResult)

# Delete the Post
deleteResult = social.delete({'id': postResult['id']})
print(deleteResult)

# Get History
# print(social.history())
