import json, pprint
from ayrshare import SocialPost

# API-KEY.json example:
# {
#   "key": "your-ayrshare-api-key",
#   "profile_key": "optional — Business Plan profile key; omit if unused",
#   "twitter_consumer_key": "optional — X Developer App API Key (BYO)",
#   "twitter_consumer_secret": "optional — X Developer App API Secret Key (BYO)"
# }
#
# X/Twitter posting requires BYO consumer credentials on the request (set_twitter_byo).
# See https://docs.ayrshare.com/dashboard/connect-social-accounts/x-twitter-byo-keys

print("Loading API-KEY.json...")
try:
    with open('./API-KEY.json', encoding='utf-8') as f:
        cfg = json.load(f)
    ayr_key = cfg['key']
except FileNotFoundError:
    raise SystemExit(
        "API-KEY.json not found in the current directory. "
        "Create it with at least {\"key\": \"<your-ayrshare-api-key>\"} — "
        "see the comment at the top of test.py for the full schema."
    )
except json.JSONDecodeError as exc:
    raise SystemExit(f"API-KEY.json is invalid JSON: {exc}")
except KeyError:
    raise SystemExit("API-KEY.json is missing required field: 'key'.")

social = SocialPost(ayr_key)

profile_key = cfg.get("profile_key")
if profile_key:
    social.setProfileKey(profile_key)

ck = (cfg.get("twitter_consumer_key") or "").strip()
cs = (cfg.get("twitter_consumer_secret") or "").strip()
if ck and cs:
    social.set_twitter_byo(ck, cs)
    print("Twitter/X BYO headers enabled (consumer key + secret).")
else:
    print(
        "WARNING: twitter_consumer_key / twitter_consumer_secret missing — "
        "X/Twitter requests will fail (BYO is enforced). "
        "Add both fields to API-KEY.json or use platforms without twitter."
    )

pp = pprint.PrettyPrinter(indent=4)

print("Running Tests...")

# Post to Platforms
postResult = social.post({'randomPost': True, 'platforms': ['twitter']})
print(postResult)

# /post returns the Ayrshare post ID at the top level as `id`.
# Per-platform IDs (e.g. the Twitter status ID) live under `postIds`,
# but getPost/delete/analytics all take the Ayrshare-level `id`.
# See https://www.ayrshare.com/docs/apis/overview#social-post-id
ayr_post_id = postResult.get('id')
if not ayr_post_id:
    raise SystemExit(f"Post failed; no Ayrshare id in response: {postResult}")

# Get Post
getResult = social.getPost({'id': ayr_post_id})
print(getResult)

# Retry Post
# retryResult = social.retryPost({'id': 'sEe25WkXQnAz188IrrzX'})
# print(retryResult)

# Update Post
#updateResult = social.updatePost({'id': 'L1chosWRlwaur5fXJU5v', 'scheduleDate': '2024-12-31T12:31:00Z'})
#print(updateResult)

# Delete the Post
deleteResult = social.delete({'id': ayr_post_id})
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