import json, pprint
from ayrshare import SocialPost

with open('./API-KEY.json') as f:
    API_KEY = json.load(f)

social = SocialPost(API_KEY["key"])
pp = pprint.PrettyPrinter(indent=4)

# Post to Platforms
""" 
postResult = social.post({
    'post':
    'Love my TikTok posting',
    'platforms': ['tiktok'],
    'mediaUrls': [
        'https://images.ayrshare.com/1gXNW1Foi8hj8d6gbRX5jm5yS9c2/3e0610e3-9171-4d12-a86e-09412a40708c-mp4.mp4'
    ]
})
pp.pprint(postResult)
"""

# Delete the Post
# deleteResult = social.delete({'id': postResult['id']})
# pp.pprint(deleteResult)

# Get History
# pp.pprint(social.history())

# Get History with Id
pp.pprint(social.history({'id': "LIpdMT04M4ba26P3YLDn"}))
