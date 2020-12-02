from ayrshare import SocialPost

social = SocialPost('AJ3PGW1-8HZM8R4-GCWTVJW-YE153PE')

# Post to Platforms
postResult = social.post({'post': 'Nice Posting 2', 'platforms': ['twitter']})
print(postResult)

# Delete the Post
deleteResult = social.delete({'id': postResult['id']})
print(deleteResult)

# Get History
# print(social.history())