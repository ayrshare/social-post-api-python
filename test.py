import json, pprint
from ayrshare import SocialPost

# Add your API Key in a file names API-KEY.json { 'key': 'API KEY'}
print("Loading API Key...")
with open('./API-KEY.json') as f:
    API_KEY = json.load(f)

print("Initializing SocialPost...")

social = SocialPost(API_KEY["key"])
social.setProfileKey('PROFILE_KEY')
pp = pprint.PrettyPrinter(indent=4)

print("Running Tests...")

# Post to Platforms
postResult = social.post({'randomPost': True, 'platforms': ['twitter']})
print(postResult)

# Get Post
getResult = social.getPost({ 'id': postResult['posts'][0]['id']})
print(getResult)

# Retry Post
# retryResult = social.retryPost({'id': 'sEe25WkXQnAz188IrrzX'})
# print(retryResult)

# Update Post
#updateResult = social.updatePost({'id': 'L1chosWRlwaur5fXJU5v', 'scheduleDate': '2024-12-31T12:31:00Z'})
#print(updateResult)

# Delete the Post
deleteResult = social.delete({'id': postResult['posts'][0]['id']})
print(deleteResult)

# Get History
print(social.history())

# Verify Media Exists
#print(social.verifyMediaExists({'mediaUrl': 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg'}))

# Get Media Upload URL
#print(social.mediaUploadUrl({ 'fileName': 'tree.jpg', 'contentType': 'image/jpeg'}))

# Get Media Meta
#print(social.mediaMeta({'url': 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg'}))

# Resize Image
#print(social.resizeImage({'imageUrl': 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg', 'platform': 'twitter'}))

# Get Analytics Post
#print(social.analyticsPost({'id': 'sEe25WkXQnAz188IrrzX'}))

# Get Analytics Social
#print(social.analyticsSocial({'platforms': ['twitter', 'linkedin', 'facebook']}))

# Add Feed
#print(social.addFeed({'url': 'https://www.ayrshare.com/feed.xml'}))

# Delete Feed
#print(social.deleteFeed({'id': 'JjSuWHtjML0SXhH5-MUrE'}))

# Get Feed
#print(social.getFeeds())

# Update Feed
#print(social.updateFeed({'id': 'BArIfIZjJAH_rcKV07Rvy', 'autoHashtag': 'true'}))

# Update Profile
#print(social.updateProfile({'profileKey': '1CCPGDX-ZZT4J2Z-H7H3NRJ-A52SZ54', 'title': 'Test Profile'}))

# Get Profiles
#print(social.getProfiles())

# Unlink Social
#print(social.unlinkSocial({'platform': 'twitter'}))

# Post Comment
#print(social.postComment({'id': 'XOVUGutufIy5UZFb01e0', 'comment': 'Great post on Ayrshare!'}))

# Get Comments
#print(social.getComments({'id': 'XOVUGutufIy5UZFb01e0'}))

# Delete Comments
#print(social.deleteComments({'id': 'XOVUGutufIy5UZFb01e0'}))

# Reply Comment
#print(social.replyComment({'commentId': 'ACwgIY0QX1Zmvs6qU2pl0', 'comment': 'Replying to the comment', 'platforms': ['instagram']}))

# Get Brand By User
#print(social.getBrandByUser({'platforms': ['twitter', 'instagram'], 'twitterUser': 'postpostpost121', 'instagramUser': '@ayrshare'}))

# Generate Post
#print(social.generatePost({'text': 'Yay'}))

# Generate Rewrite
#print(social.generateRewrite({'post': 'Yay'}))

# Generate Transcription
# print(social.generateTranscription({'videoUrl': 'https://img.ayrshare.com/random/landscape5.mp4'}))

# Generate Translation
#print(social.generateTranslation({'text': 'Hello', 'lang': 'es'}))

# Generate Alt Text
#print(social.generateAltText({'url': 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg'}))

# Auto Hashtags
#print(social.autoHashtags({'post': 'The best post ever!'}))

# Recommend Hashtags
#print(social.recommendHashtags({'keyword': 'food'}))

# Check Banned Hashtags
# print(social.checkBannedHashtags({'hashtag': 'food'}))

# Get short link
#print(social.shortLink({'url': 'https://www.ayrshare.com'}))

# Short link analytics
#print(social.shortLinkAnalytics({'id': 'qR--d8'}))

# Get Reviews
#print(social.reviews({ 'platform': 'facebook'}))

# Get Single Review
#print(social.review({ 'platform': 'facebook', 'id': '10114455408676943'}))

# Reply to Review
#print(social.reviewReply({ 'platform': 'facebook', 'reviewId': '10114455408676943', 'reply': 'Thanks for the review!'}))

# Delete Review Reply
#print(social.deleteReviewReply({ 'platform': 'gmb', 'reviewId': '10114455408676943'}))