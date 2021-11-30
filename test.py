import json
from ayrshare import SocialPost

with open('./API-KEY.json') as f:
    API_KEY = json.load(f)

social = SocialPost(API_KEY["key"])

# Post to Platforms
# postResult = social.post({'post': 'I want to see more', 'platforms': ['twitter']})
# print(postResult)
# print(postResult['id'])

# Delete the Post
# deleteResult = social.delete({'id': postResult['id']})
deleteResult = social.delete({'id': "NzFIBXhD4pd1N5r2LtCu"})
print(deleteResult)

# Get History
# print(social.history())