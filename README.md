# Social Media APIs for Posting, Scheduling, and Analytics

![Ayrshare logo](https://www.ayrshare.com/wp-content/uploads/2020/08/ayr-logo-2156-reduced.png)

The Social Media API is a Python wrapper SDK for [Ayrshare's APIs](https://www.ayrshare.com). While most of the capabliites are supported, the Python wrapper SDK is not as feature complete as the [Ayrshare's APIs](https://www.ayrshare.com/docs/introduction).
The Social Media API is a Python wrapper SDK for [Ayrshare's APIs](https://www.ayrshare.com). While most of the capabliites are supported, the Python wrapper SDK is not as feature complete as the [Ayrshare's APIs](https://www.ayrshare.com/docs/introduction).

## What is Ayrshare?

Ayrshare is a powerful set of APIs that enable you to send social media posts, get analytics, manage comments, do DMs, and more to *X/Twitter*, *Instagram*, *Facebook*, *LinkedIn*, *YouTube*, *Google Busienss Profile*, *Pinterest*, *TikTok*, *Reddit*, and *Telegram* on behalf of your users or clients.

The Ayrshare Social API handles all the setup and maintenance for the social media networks. One API to rule them all (yeah, went there). See the full list of [full list of features](https://www.ayrshare.com/docs/apis/overview).
The Ayrshare Social API handles all the setup and maintenance for the social media networks. One API to rule them all (yeah, went there). See the full list of [full list of features](https://www.ayrshare.com/docs/apis/overview).

Get started with a [free plan](https://www.ayrshare.com/pricing), or if you have a platform or manage multiple users check out the [Business Plan](https://www.ayrshare.com/business-plan-for-multiple-users/).

For more information on setup, see our installation [video](https://youtu.be/G8M6DZdtcMc) or our [Quick Start Guide](https://www.ayrshare.com/docs/quickstart).
For more information on setup, see our installation [video](https://youtu.be/G8M6DZdtcMc) or our [Quick Start Guide](https://www.ayrshare.com/docs/quickstart).

## Installation

`pip install social-post-api`

## Setup

**1.** Create a free [Ayrshare account](https://app.ayrshare.com).

   ![alt Social Accounts Setup](https://www.ayrshare.com/wp-content/uploads/Ayrshare-login.png)

**2.** Enable your social media accounts such as C/Twitter, Facebook, LinkedIn, Reddit, Instagram, Google Business Profile, Telegram, TikTok, or YouTube in the Ayrshare dashboard.

   ![alt Social Accounts Setup](https://www.ayrshare.com/wp-content/uploads/Ayrshare-social-linking.png)
  
**3.** Copy your API Key from the Ayrshare dashboard. Used for authentication.

   ![alt API Key](https://www.ayrshare.com/wp-content/uploads/Ayrshare-API-key.png)

## Getting Started

### Initialize Social Media API

Create a new Social Post object with your API Key.

``` python
from ayrshare import SocialPost
social = SocialPost('DJED-DKEP-SJWK-WJKS') # get an API Key at ayrshare.com
```

### History, Post, Delete Example

This simple example shows how to post, get history, and delete the post. This example assumes you have a free API key from [Ayrshare](https://www.ayrshare.com) and have enabled X/Twitter, Facebook, and LinkedIn. Note, Instagram, Telegram, YouTube, TikTok, and Reddit also available.

``` python
from ayrshare import SocialPost
social = SocialPost('8jKj782Aw8910dCN') # get an API Key at ayrshare.com

# Post to Platforms Twitter, Facebook, and LinkedIn
postResult = social.post({'post': 'Nice Posting 2', 'platforms': ['twitter', 'facebook', 'linkedin']})
print(postResult)

# Delete
deleteResult = social.delete({'id': postResult['id']})
print(deleteResult)

# History
print(social.history())
```

## Social API

### Post

[Published a new post](https://www.ayrshare.com/docs/apis/post/overview) to the specified social networks either immediately or at scheduled future date with the Social API. Returns a promise that resolves to an object containing the post ID and post status (success, error). See the [post endpoint](https://www.ayrshare.com/docs/apis/post/post) for the full capabilities.

``` python
postResponse = social.post({
    # Required
    'post': 'Best post ever!',

  # Required: Social media platforms to post.
  # Accepts an array of strings with values: "facebook", "twitter", "linkedin", "pinterest", "reddit", or "telegram".
    'platforms': ['twitter', 'facebook', 'linkedin', 'pinterest', 'telegram', 'instagram'],

  # Optional: URLs of images to include in the post or for Instagram
  'mediaUrls': ['https://img.ayrshare.com/012/gb.jpg'],

  # Optional: Datetime to schedule a future post. 
  # Accepts an ISO-8601 UTC date time in format "YYYY-MM-DDThh:mm:ssZ". Example: 2021-07-08T12:30:00Z
  'scheduleDate': '2020-08-07T15:17:00Z',

  # Optional: Shorten links in the post for all platforms similar to bit.ly.
  # Only URLS starting with http or https will be shortened. Default value: true.
  'shorten_links': true
})
```

### Delete

Delete a post with a given post ID, obtained from the "post" response. Returns a promise with the delete status. Also, can bulk delete multiple IDs at once using the "bulk" key. See the [delete endpoint](https://www.ayrshare.com/docs/apis/post/delete-post) for more details.
Delete a post with a given post ID, obtained from the "post" response. Returns a promise with the delete status. Also, can bulk delete multiple IDs at once using the "bulk" key. See the [delete endpoint](https://www.ayrshare.com/docs/apis/post/delete-post) for more details.

``` python
deleteResponse = social.delete({
    # Required
    'id': 'POST ID',                          # Optional, but required if "bulk" not present
    'bulk': ['Post ID 1', 'Post ID 2', ...]   # Optional, but required if "id" not present
  })
```

### Get Post

Get a post with a given post ID. Returns a promise that resolves to a post object. See the [get post endpoint](https://www.ayrshare.com/docs/apis/post/get-post) for more details.
Get a post with a given post ID. Returns a promise that resolves to a post object. See the [get post endpoint](https://www.ayrshare.com/docs/apis/post/get-post) for more details.

``` python
getResponse = social.getPost({
    # Required
    'id': 'POST ID',
  })
```

### Retry Post

Retry a failed post with a given post ID. Returns a promise that resolves to an object with the post status. See the [retry post endpoint](https://www.ayrshare.com/docs/apis/post/retry-post) for more details.
Retry a failed post with a given post ID. Returns a promise that resolves to an object with the post status. See the [retry post endpoint](https://www.ayrshare.com/docs/apis/post/retry-post) for more details.

``` python
retryResponse = social.retryPost({
    # Required
    'id': 'POST ID',
  })
```

### Update Post

Update a post with a given post ID. Returns a promise that resolves to an object with status and update info. See the [update post endpoint](https://www.ayrshare.com/docs/apis/post/retry-post) for more details.

``` python
updateResponse = social.updatePost({
    'id': 'POST ID',                         # Required: ID of the post to update
    'scheduleDate': '2024-08-07T15:17:00Z',  # Optional: Datetime to schedule a future post.
    'approved': 'true',                         # Optional: Approve the post to send it.
    'youTubeOptions': {                         # Optional: YouTube specific options
      'title': 'New Title',
      'description': 'New Description',
      'visibility': 'unlisted',
      'categoryId': 24,
    },
    'notes': 'New notes',                      # optional: Notes about the post
  })
``` 

### History

Get a [history](https://www.ayrshare.com/docs/apis/history/overview) of all posts and their current status in descending order. Returns a promise that resolves to an array of post objects. See the [history endpoint](https://www.ayrshare.com/docs/apis/history/get-history) for more details.

``` python
historyResponse = social.history({
  'lastRecords': 10,    # optional: returns the last X number of history records
  'lastDays': 30,       # optional: returns the last X number of days of history records. Defaults to 30 if not present.
})
```

### Upload Media

Upload and store a new image. Returns a URL referencing the image. Can be used in "image_url" in "post". See the [media endpoint](https://www.ayrshare.com/docs/apis/media/overview) for more details.

``` python
uploadResponse = social.upload({
  # Required: The image as a Base64 encoded string. Example encoding: https://www.base64-image.de/
  'file': 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ...',

  # Optional
  'fileName': 'test.png',

  # Optional
    'description': 'best image'
})
```

### Get Media

Get all media URLS. Returns a promise that resolves to an array of URL objects. See the [media endpoint](https://www.ayrshare.com/docs/apis/media/get-media-in-gallery) for more details.
Get all media URLS. Returns a promise that resolves to an array of URL objects. See the [media endpoint](https://www.ayrshare.com/docs/apis/media/get-media-in-gallery) for more details.

``` python
mediaResponse = social.media()
```

### Verify Media Exists

Verify that the media file exists when uploaded. See the [media verify exists endpoint](https://www.ayrshare.com/docs/apis/media/verify-media-url) for more details.
Verify that the media file exists when uploaded. See the [media verify exists endpoint](https://www.ayrshare.com/docs/apis/media/verify-media-url) for more details.

``` python
verifyResponse = social.verifyMediaExists({
  # Required: URL of the media file
  'mediaUrl': 'https://img.ayrshare.com/012/gb.jpg',
})
```

### Resize Image

Get image resized according to social network requirements. See the [resize image endpoint](https://www.ayrshare.com/docs/apis/media/resize) for more details.
Get image resized according to social network requirements. See the [resize image endpoint](https://www.ayrshare.com/docs/apis/media/resize) for more details.

``` python
resizeResponse = social.resizeImage({
  'imageUrl': "https://theImage.jpg", # required: URL of the image to resize
  'platform': "facebook" # required: Platform to resize the image for. 
  'watermarkUrl': "https:#theWatermark.png", # optional: URL of the watermark image to add to the image.
  'effects': { color: "#A020F0" } # optional: Change opacity, colors, etc. See endpoint for more details.
  'dimensions': { width: 1200, height: 628 } # optional: Width and height of the image. Required if platform is not specified.
  'mode': "blur" # optional. See endpoint for more details.
})
```

### User

Get data about the logged in [user](https://www.ayrshare.com/docs/apis/user/overview), such as post quota, used quota, active social networks, and created date. See the [user endpoint](https://www.ayrshare.com/docs/apis/user/profile-details) for more details.

``` python
user = social.user()
```

### Shorten URL

Shorten a URL and return the shortened URL. See the [shorten endpoint](https://www.ayrshare.com/docs/apis/links/create-short-link) for more details.

``` python
shortenResponse = social.shorten({
    # Required: URL to shorten
    'url': 'https://theURLtoShorten.com/whatmore',
  })
```

### Analytics

Get [analytics](https://www.ayrshare.com/docs/apis/analytics/overview) on shortened links and shares, likes, shares, and impressions with for a post or at the accounts level. See the [analytics endpoint](https://www.ayrshare.com/docs/apis/analytics/post) for more details.

``` python
analytics = social.analyticsLinks({
  # Optional range 1-7, default 1 day.
  'lastDays': 3
})
```

``` python
analytics = social.analyticsPost({
  'id': 'Post ID',
  'platforms': ['twitter', 'linkedin'] # optional: filter by platform
})
```

### Social Analytics

Get analytics on a social network. Returns a promise that resolves to an object containing the analytics data. See the [social analytics endpoint](https://www.ayrshare.com/docs/apis/analytics/social) for more details.

```python
analytics = social.analyticsSocial({
  'platforms': ['twitter', 'linkedin'] # required
})
```

### Add an RSS or Substack Feed

Add a new RSS or Substack feed to auto post all new articles. Returns a promise that resolved to an object containing the feed ID. See [How to Automate Your Blog or Newsletter](https://www.ayrshare.com/how-to-automatically-post-your-blog-or-newsletter-to-social-media/) for more info.

``` python
feedResponse = social.addFeed({
  # Required: URL to shorten
  'url': 'https://theRSSFeed',

  # Optional: Value: "rss" or "substack". 
  # If not set, defaults to "rss"
    'type': 'RSS',
})
```

### Delete an RSS or Substack Feed

Delete an RSS feed for a given ID.

``` python
feedResponse = social.deleteFeed({
  # Required: ID of the feed
  'id': 'Feed ID',
})
```

### Get Feeds

Get all registered RSS feeds. Returns a promise that resolves to an array of feed objects. See the [RSS Feeds](https://www.ayrshare.com/docs/apis/feeds/overview) for more details.

``` python
feedsResponse = social.getFeeds()
```

### Update Feed

Update an RSS feed for a given ID. Returns a promise that resolves to an object containing the feed ID. See the [update feed endpoint](https://www.ayrshare.com/docs/apis/feeds/update-feed) for more details.
Update an RSS feed for a given ID. Returns a promise that resolves to an object containing the feed ID. See the [update feed endpoint](https://www.ayrshare.com/docs/apis/feeds/update-feed) for more details.

``` python
feedResponse = social.updateFeed({
    'id': 'Feed ID', # required: ID of the feed
    'useFirstImage': 'true', # optional: Use the first image in the article to add to the post.
    'autoHashtag': 'true', # optional: Automatically add hashtags to the post.
  })
```

### Get Comments

Get comments for a post. See the [comments endpoint](https://www.ayrshare.com/docs/apis/comments/overview) for more details.

``` python
getCommentsResponse = social.getComments({
  # Required: ID of the Post
  'id': 'Post Id',
})
```

### Post a Comment

Add a comment to a post. See the [create comment endpoint](https://www.ayrshare.com/docs/apis/comments/post-comment) for more details.

``` python
postCommentResponse = social.postComment({
  # Required: ID of the Post
  'id': 'Post Id',
  'platforms': ['facebook', 'instagram'],
  'comment': 'The best comment ever!',
})
```

### Delete Comments

Delete either a single comment or all comments under a post that were sent via Ayrshare. Available for Facebook, Instagram, LinkedIn, Reddit, TikTok, X/Twitter, and YouTube. See the [delete comments endpoint](https://www.ayrshare.com/docs/apis/comments/post-comment) for more details.

``` python
deleteCommentResponse = social.deleteComments({
    'id': "Pkdo9sjk2", # required: Post top-level ID or social comment ID
    'platforms': ["instagram", "facebook"], # optional: Required only if using the social comment id.
  })
```

### Reply Comment

Reply to a comment. Available for Facebook, Instagram, LinkedIn, TikTok, X/Twitter, and YouTube. See the [reply comment endpoint](https://www.ayrshare.com/docs/apis/comments/reply-to-comment) for more details.
Reply to a comment. Available for Facebook, Instagram, LinkedIn, TikTok, X/Twitter, and YouTube. See the [reply comment endpoint](https://www.ayrshare.com/docs/apis/comments/reply-to-comment) for more details.

``` python
replyCommentResponse = social.replyComment({
    'commentId': 'Pkdo9sjk2', # required: The Ayrshare commentId returned from the POST comment endpoint. Be sure to use the top level commentId.
    'platforms': ['instagram', 'facebook'], # required: Array of platforms to post the reply. Values: facebook, instagram, linkedin, tiktok, twitter, youtube
    'comment': 'What a comment' # required: The reply to add to the comment.
  })
```

## Business Functions for Multiple Users - Business or Enterprise Plan Required

The [Business Plan](https://www.ayrshare.com/business-plan-for-multiple-users/) allows you to create, manage, and post on behalf of client profiles via the API or Dashboard GUI. You can [integrate](https://www.ayrshare.com/docs/multiple-users/business-plan-overview) Ayrshare into your platform, product, or agency and give your clients social media capabilites. Please [contact us](mailto:contact@ayrshare.com) with any questions.

A User Profile PROFILE_KEY can be set with the `setProfileKey` method.

``` python
social = SocialPost(API_KEY)
social.setProfileKey('PROFILE_KEY')
```

Replace `PROFILE_KEY` with the PROFILE_KEY of the profile you want to use.

Please see the [Authorization](https://www.ayrshare.com/docs/apis/overview#authorization) docs for more details.

### Create Profile

Create a new account [profile](https://www.ayrshare.com/docs/apis/profiles/overview) under the primary account. See the [create profile endpoint](https://www.ayrshare.com/docs/apis/profiles/create-profile) for more details.

``` python
createProfileResponse = social.createProfile({
    # Required: title
    'title': 'New Profile Title',
})
```

### Delete Profile

Delete a profile owned by the primary account. See the [delete profile endpoint](https://www.ayrshare.com/docs/apis/profiles/delete-profile) for more details.
Delete a profile owned by the primary account. See the [delete profile endpoint](https://www.ayrshare.com/docs/apis/profiles/delete-profile) for more details.

``` python
deleteProfileResponse = social.deleteProfile({
    # Required: profileKey - the API Key of the profile to delete
    'profileKey': 'JI9s-kJII-9283-OMKM',
  })
```

### Generate a JWT URL

Generate a JWT Token and URL used for authorizing a user's access to the Social Account linking page. See the [generate JWT endpoint](https://www.ayrshare.com/docs/apis/profiles/generate-jwt) for more details.
Generate a JWT Token and URL used for authorizing a user's access to the Social Account linking page. See the [generate JWT endpoint](https://www.ayrshare.com/docs/apis/profiles/generate-jwt) for more details.

``` python
generateJWTResponse = social.generateJWT({
    'domain': 'mydomain',
    'privateKey': 'private key data...',
    'profileKey': 'JI9s-kJII-9283-OMKM',
  })
```

### Update Profile

Update a profile owned by the primary account. See the [update profile endpoint](https://www.ayrshare.com/docs/apis/profiles/update-profile) for more details.
Update a profile owned by the primary account. See the [update profile endpoint](https://www.ayrshare.com/docs/apis/profiles/update-profile) for more details.

``` python
updateProfileResponse = social.updateProfile({
  'profileKey': 'JI9s-kJII-9283-OMKM',  #Required: profileKey - the API Key of the profile to update
  'title': 'This is a great new title' #Optional: the new title of the profile
  'disableSocial': ['facebook', 'linkedin'] #Optional: an array of social networks to disable
  'hideTitle': 'true' #Optional: hide the title of the profile
  'displayTitle': 'true' #Optional: display the title of the profile
  })
```

### Get Profiles

Get all the profiles associated with the primary account. See the [get profile endpoint](https://www.ayrshare.com/docs/apis/profiles/get-profiles) for more details.
Get all the profiles associated with the primary account. See the [get profile endpoint](https://www.ayrshare.com/docs/apis/profiles/get-profiles) for more details.

``` python
getProfileResponse = social.getProfiles()
```

### Unlink Social Network

Unlink a social account for a given user profile owned by the primary account. See the [unlink social network endpoint](https://www.ayrshare.com/docs/apis/profiles/unlink-social-network) for more details.
Unlink a social account for a given user profile owned by the primary account. See the [unlink social network endpoint](https://www.ayrshare.com/docs/apis/profiles/unlink-social-network) for more details.

``` python
unlinkResponse = social.unlinkSocial({
    'profileKey': "JI9s-kJII-9283-OMKM",     # Required: profileKey - the API Key of the profile to unlink for.
    'platform': "facebook"
  })
```

### Get Brand Info on a User

Get brand information on users and companies public social media accounts. See the [brand endpoint](https://www.ayrshare.com/docs/apis/brand/overview) for more details.

``` python
brandResponse = social.getBrandByUser({
    'platforms': ['instagram', 'facebook'],
    'instagramUser': '@ayrshare',
    'facebookUser': 'ayrshare',
  })
```

### Auto Hashtags

Automatically add hashtags to your post. See the [auto hashtags endpoint](https://www.ayrshare.com/docs/apis/hashtags/overview) for more details.

``` python
autoHashtagsResponse = social.autoHashtags({
    'post': 'I love social media', # required: Post text to add hashtags for.
    'position': 'auto' # optional: Position of the hashtags. Values: 'auto', 'end'. Default: 'auto'.
    'max': 2 # optional: Maximum number of hashtags to add, ranging 1-5. Default: 2.
})
```

### Recommend Hashtags

Get suggestions for hashtags based on a keyword. See the [recommend hashtags endpoint](https://www.ayrshare.com/docs/apis/hashtags/recommend-hashtags) for more details.
Get suggestions for hashtags based on a keyword. See the [recommend hashtags endpoint](https://www.ayrshare.com/docs/apis/hashtags/recommend-hashtags) for more details.

``` python
recommendHashtagsResponse = social.recommendHashtags({
    'keyword': 'social media', # required: Keyword to get hashtags for.
})
```

### Check Banned Hashtags

Check if a hashtag is banned on Instagram or other social networks. See the [check banned hashtags endpoint](https://www.ayrshare.com/docs/apis/hashtags/check-hashtags) for more details.
Check if a hashtag is banned on Instagram or other social networks. See the [check banned hashtags endpoint](https://www.ayrshare.com/docs/apis/hashtags/check-hashtags) for more details.

``` python
checkBannedHashtagsResponse = social.checkBannedHashtags({
    'hashtag': 'socialmedia', # required: Hashtag to check.
})
```

### Get All Reviews

Retrieve all the reviews for the specified platform. See the [get all reviews endpoint](https://www.ayrshare.com/docs/apis/reviews/get-reviews) for more details.
Retrieve all the reviews for the specified platform. See the [get all reviews endpoint](https://www.ayrshare.com/docs/apis/reviews/get-reviews) for more details.

``` python
allReviewsResponse = social.reviews({
    'platform': 'facebook', # required: Platform to get reviews for. Currently available: "facebook", "gmb"
})
```

### Get Single Review

Retrieve a single review. See the [get single review endpoint](https://www.ayrshare.com/docs/apis/reviews/get-one-review) for more details.
Retrieve a single review. See the [get single review endpoint](https://www.ayrshare.com/docs/apis/reviews/get-one-review) for more details.

``` python
singleReviewResponse = social.review({
    'id': 'Review ID', # required
    'platform': 'gmb', # required: Platform to get review for. Currently available: "gmb"
})
```

### Reply to Review

Reply to a review. See the [reply to review endpoint](https://www.ayrshare.com/docs/apis/reviews/reply-review) for more details.
Reply to a review. See the [reply to review endpoint](https://www.ayrshare.com/docs/apis/reviews/reply-review) for more details.

``` python
replyReviewResponse = social.replyReview({
    'reviewId': 'Review ID', # required: Review ID to reply to.
    'platform': 'facebook', # required: Platform to reply to review for. Currently available: "facebook", "gmb"
    'reply': 'Thank you for the review' # required: Text of the reply to the review.
})
```

### Delete Review Reply

Delete a review reply. See the [delete review reply endpoint](https://www.ayrshare.com/docs/apis/reviews/reply-review) for more details.

``` python
deleteReplyReviewResponse = social.deleteReplyReview({
    'reviewId': 'Review ID', # required: Review ID to delete reply for.
    'platform': 'gmb', # required: Platform to delete reply for. Currently available: "gmb"
})
```

## Max Pack Required

### Generate Post

Generate a new social post using ChatGPT. Token limits applicable. See the [generate post endpoint](https://www.ayrshare.com/docs/apis/generate/post-text) for more details.
Generate a new social post using ChatGPT. Token limits applicable. See the [generate post endpoint](https://www.ayrshare.com/docs/apis/generate/post-text) for more details.

``` python
generatePostResponse = social.generatePost({
    'text': 'I love social media', # required: Description of what the post should be about. 
    'hashtags': 'true', #optional: Include hashtags in the post. Default: true
    'emojis': 'true', # optional: Include emojis in the post. Default: false
    'twitter': 'true', # optional: Construct a post 280 or few characters. Default: false
})
```

### Generate Rewrite

Generate variations of a social media post using ChatGPT. Token limits applicable. See the [generate rewrite endpoint](https://www.ayrshare.com/docs/apis/generate/rewrite-post) for more details.
Generate variations of a social media post using ChatGPT. Token limits applicable. See the [generate rewrite endpoint](https://www.ayrshare.com/docs/apis/generate/rewrite-post) for more details.

``` python
generateRewriteResponse = social.generateRewrite({
    'post': 'I love social media', # required: The post text to be rewritten. 
    'emojis': 'true', # optional: Include emojis in the post. Default: false
    'hashtags': 'true', # optional: Include hashtags in the post. Default: false
    'twitter': 'true', # optional: Construct a post 280 or few characters. Default: false
    'rewrites': 5, # optional: Number of rewrites to generate. Default: 5
})
```

### Generate Transcription

Provide a transcription of a video file. See the [generate transcription endpoint](https://www.ayrshare.com/docs/apis/generate/transcribe-video) for more details.
Provide a transcription of a video file. See the [generate transcription endpoint](https://www.ayrshare.com/docs/apis/generate/transcribe-video) for more details.

``` python
generateTranscriptionResponse = social.generateTranscription({
  'videoUrl': 'https://theVideo.mp4', # required: URL encoded video URL. The video must be hosted by Ayrshare.
})
```

### Generate Translation

Translate text for a post to over 100 different languages. See the [generate translation endpoint](https://www.ayrshare.com/docs/apis/generate/translate-post) for more details.
Translate text for a post to over 100 different languages. See the [generate translation endpoint](https://www.ayrshare.com/docs/apis/generate/translate-post) for more details.

``` python
generateTranslationResponse = social.generateTranslation({
  'text': 'I love social media', # required: The text to be translated.
  'lang': 'es', # required: The language code to translate the text to. 
})
```

### Generate Sentiment Analysis

Generate a sentiment analysis on a social media post or comment to understand if the text is positive, negative, or neutral and recommendations on improving the text for a more positive reaction. See the [generate sentiment analysis endpoint](https://www.ayrshare.com/docs/apis/generate/sentiment) for more details.

``` python
generateSentiment= social.generateSentiment({
  'text': 'I love social media' # required: The text to generate a sentiment analysis for.
})
```

### Generate Alt Text

Create AI-generated alt text for your images.  See the [generate alt text endpoint](https://www.ayrshare.com/docs/apis/generate/sentiment) for more details.

``` python
generateAltTextResponse = social.generateAltText({
    'url': 'https://theImage.jpg', # required: URL of the image to generate alt text for.
    'keywords': ['social media', 'ayrshare'], # optional: Keywords to help the AI generate better alt text.
    'lang': 'en' # optional: The language code to generate the alt text in. Default: 'en'
})
```

### Shorten link

Provide a URL and a shortened link will be returned. See the [shorten link endpoint](https://www.ayrshare.com/docs/apis/links/overview) for more details.

``` python
shortenLinkResponse = social.shortLink({
    'url': 'https://theURL.com', # required: URL to shorten.
    'utmId': '1234', # optional: UTM ID to track the link. See more details about utm parameters at endpoint link above.
    'utmSource': 'source', # optional
    'utmMedium': 'medium', # optional
    'utmCampaign': 'campaign', # optional
    'utmTerm': 'term', # optional
    'utmContent': 'content', # optional
})
```

### Analytics for Shortened Links

Return analytics for all shortened links or a single link for a given link ID. See the [analytics link endpoint](https://www.ayrshare.com/docs/apis/links/link-analytics) for more details.
Return analytics for all shortened links or a single link for a given link ID. See the [analytics link endpoint](https://www.ayrshare.com/docs/apis/links/link-analytics) for more details.

``` python
analyticsLinkResponse = social.shortLinkAnalytics({
    'id': 'Link ID', # optional: Link ID to get analytics for.
    'fromCreatedDate': '2023-07-08T12:30:00Z', # optional: Get history of links shortened after this date.
    'toCreatedDate': '2023-07-08T12:30:00Z', # optional: Get history of links shortened before this date.
    'fromClickDate': '2023-07-08T12:30:00Z', # optional: Get history of links clicked after this date.
    'toClickDate': '2023-07-08T12:30:00Z', # optional: Get history of links clicked before this date.
})
```

### Additional Calls

- [Webhooks endpoints](https://www.ayrshare.com/docs/apis/webhooks/overview)
- [Webhooks endpoints](https://www.ayrshare.com/docs/apis/webhooks/overview)
- unregisterWebhook
- listWebhook
- setAutoSchedule
- deleteAutoSchedule
- listAutoSchedule

## Other Packages & Integrations

We have other package and integrations such as [Node NPM](https://www.ayrshare.com/docs/packages-guides/nodejs), [Bubble.io](https://www.ayrshare.com/docs/packages-guides/bubble), [Make](https://www.ayrshare.com/docs/packages-guides/make), and [Airtable](https://www.ayrshare.com/docs/packages-guides/airtable).

### Information and Support

Additional examples, responses, etc. can be found at:

[RESTful API Endpoint Docs](https://www.ayrshare.com/docs/apis/overview)
[RESTful API Endpoint Docs](https://www.ayrshare.com/docs/apis/overview)

[GitHub](https://github.com/ayrshare/social-post-api-python)

See our [changelog](https://www.ayrshare.com/docs/whatsnew/latest) for the latest and greatest.
See our [changelog](https://www.ayrshare.com/docs/whatsnew/latest) for the latest and greatest.

Please [contact us](mailto:support@ayrshare.com) with your questions, or just to give us shout-out 📢!
