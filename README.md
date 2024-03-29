# Social Media APIs for Posting, Scheduling, and Analytics

<img src="https://www.ayrshare.com/wp-content/uploads/2020/08/ayr-logo-2156-reduced.png" width="400">

The Social Media API is a wrapper SDK for [Ayrshare's APIs](https://www.ayrshare.com).

Ayrshare is a powerful set of APIs that enable you to send social media posts, get analytics, and add comments to *Twitter*, *Instagram*, *Facebook*, *LinkedIn*, *YouTube*, *Google My Business*, *Pinterest*, *TikTok*, *Reddit*, and *Telegram* on behalf of your users or clients.

The Ayrshare Social API handles all the setup and maintenance for the social media networks. One API to rule them all (yeah, went there). See the full list of [full list of features](https://docs.ayrshare.com/rest-api/overview).

Get started with a [free plan](https://www.ayrshare.com/pricing), or if you have a platform or manage multiple users check out the [Business Plan](https://www.ayrshare.com/business-plan-for-multiple-users/).

For more information on setup, see our installation [video](https://youtu.be/G8M6DZdtcMc) or our [Quick Start Guide](https://docs.ayrshare.com/quick-start-guide).

## Installation

`pip install social-post-api`

## Setup

**1.** Create a free [Ayrshare account](https://app.ayrshare.com).

   ![alt Social Accounts Setup](https://www.ayrshare.com/wp-content/uploads/2021/07/ayrshare-login.jpg)

**2.** Enable your social media accounts such as Twitter, Facebook, LinkedIn, Reddit, Instagram, Google My Business, Telegram, TikTok, or YouTube in the Ayrshare dashboard.

   ![alt Social Accounts Setup](https://www.ayrshare.com/wp-content/uploads/social-api-linking.jpg)
  
**3.** Copy your API Key from the Ayrshare dashboard. Used for authentication.

   ![alt API Key](https://www.ayrshare.com/wp-content/uploads/social-api-key.jpg)

## Getting Started

### Initialize Social Media API

Create a new Social Post object with your API Key.

``` python
from ayrshare import SocialPost
social = SocialPost('8jKj782Aw8910dCN') # get an API Key at ayrshare.com
```

### History, Post, Delete Example

This simple example shows how to post, get history, and delete the post. This example assumes you have a free API key from [Ayrshare](https://www.ayrshare.com) and have enabled Twitter, Facebook, and LinkedIn. Note, Instagram, Telegram, YouTube, and Reddit also available.

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

Published a new post to the specified social networks either immediately or at scheduled future date with the Social API. Returns a promise that resolves to an object containing the post ID and post status (success, error). See the [post endpoint](https://docs.ayrshare.com/rest-api/endpoints/post) for the full capabilities.

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

Delete a post with a given post ID, obtained from the "post" response. Returns a promise with the delete status. Also, can bulk delete multiple IDs at once using the "bulk" key. See the [delete endpoint](https://docs.ayrshare.com/rest-api/endpoints/post#delete-a-post) for more details.

``` python
deleteResponse = social.delete({
    # Required
    'id': 'POST ID',                          # optional, but required if "bulk" not present
    'bulk': ['Post ID 1', 'Post ID 2', ...]   # optional, but required if "id" not present
  })
```

### History

Get a history of all posts and their current status in descending order. Returns a promise that resolves to an array of post objects. See the [history endpoint](https://docs.ayrshare.com/rest-api/endpoints/history) for more details.

``` python
historyResponse = social.history({
  'lastRecords': 10,    # optional: returns the last X number of history records
  'lastDays': 30,       # optional: returns the last X number of days of history records. Defaults to 30 if not present.
})
```

### Upload Media

Upload and store a new image. Returns a URL referencing the image. Can be used in "image_url" in "post". See the [media endpoint](https://docs.ayrshare.com/rest-api/endpoints/media) for more details.

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

Get all media URLS. Returns a promise that resolves to an array of URL objects. See the [media endpoint](https://docs.ayrshare.com/rest-api/endpoints/media) for more details.

``` python
mediaResponse = social.media()
```

### User

Get data about the logged in user, such as post quota, used quota, active social networks, and created date. See the [user endpoint](https://docs.ayrshare.com/rest-api/endpoints/user) for more details.

``` python
user = social.user()
```

### Shorten URL

Shorten a URL and return the shortened URL. See the [shorten endpoint](https://docs.ayrshare.com/rest-api/endpoints/shorten) for more details.

``` python
shortenResponse = social.shorten({
    # Required: URL to shorten
    'url': 'https://theURLtoShorten.com/whatmore',
  })
```

### Analytics

Get analytics on shortened links and shares, likes, shares, and impressions with for a post or at the accounts level. See the [analytics endpoint](https://docs.ayrshare.com/rest-api/endpoints/analytics) for more details.

``` python
analytics = social.analyticsLinks({
  # Optional range 1-7, default 1 day.
  'lastDays': 3
})
```

``` python
analytics = social.analyticsPost({
  'id': 'Post ID',
  'platforms': ['twitter', 'linkedin']
})
```

### Add an RSS or Substack Feed

Add a new RSS or Substack feed to auto post all new articles. Returns a promise that resolved to an object containing the feed ID. See [How to Automate Your Blog or Newsletter](https://www.ayrshare.com/how-to-automatically-post-your-blog-or-newsletter-to-social-media/) for more info.

``` python
feedResponse = social.feedAdd({
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
feedResponse = social.feedDelete({
  # Required: ID of the feed
  'id': 'Feed ID',
})
```

### Get Commnets

Get comments for a post. Currently only on Facebook and Instagram. See the [get comment endpoint](https://docs.ayrshare.com/rest-api/endpoints/comments#get-comments) for more details.

``` python
getCommentsResponse = social.getComments({
  # Required: ID of the Post
  'id': 'Post Id',
})
```

### Post a Comment

Add a comment to a post. Currently only on Facebook and Instagram. See the [create comment endpoint](https://docs.ayrshare.com/rest-api/endpoints/comments#post-a-comment) for more details.

``` python
postCommentResponse = social.postComment({
  # Required: ID of the Post
  'id': 'Post Id',
  'platforms': ['facebook', 'instagram'],
  'comment': 'The best comment ever!',
})
```

## Business Functions for Multiple Users - Business or Enterprise Plan Required

The [Business Plan](https://www.ayrshare.com/business-plan-for-multiple-users/) allows you to create, manage, and post on behalf of client profiles via the API or Dashboard GUI. You can [integrate](https://docs.ayrshare.com/multiple-client-accounts/overview) Ayrshare into your platform, product, or agency and give your clients social media capabilites. Please [contact us](mailto:contact@ayrshare.com) with any questions.

### Create Profile

Create a new account profile under the primary account. See the [create profile endpoint](https://docs.ayrshare.com/rest-api/endpoints/profiles#create-a-new-profile) for more details.

``` python
createProfileResponse = social.createProfile({
    # Required: title
    'title': 'New Profile Title',
})
```

### Delete Profile

Delete a profile owned by the primary account. See the [delete profile endpoint](https://docs.ayrshare.com/rest-api/endpoints/profiles#delete-a-profile) for more details.

``` python
deleteProfileResponse = social.deleteProfile({
    # Required: profileKey - the API Key of the profile to delete
    'profileKey': 'JI9s-kJII-9283-OMKM',
  })
```

### Generate a JWT URL

Generate a JWT Token and URL used for authorizing a user's access to the Social Account linking page. See the [generate JWT endpoint](https://docs.ayrshare.com/rest-api/endpoints/profiles#generate-a-jwt) for more details.

``` python
generateJWTResponse = social.generateJWT({
    'domain': 'mydomin',
    'privateKey': 'private key data...',
    'profileKey': 'JI9s-kJII-9283-OMKM',
  })
```

### Additional Calls

- [Webhooks endpoints](https://docs.ayrshare.com/rest-api/endpoints/webhooks)
- unregisterWebhook
- listWebhook
- setAutoSchedule
- deleteAutoSchedule
- listAutoSchedule

## Other Packages & Integrations

We have other package and integrations such as [Node NPM](https://docs.ayrshare.com/packages/node.js-npm-package), [Bubble.io](https://docs.ayrshare.com/packages/bubble.io), and [Airtable](https://docs.ayrshare.com/packages/airtable) + examples in C#, PHP, and Go.

### Information and Support

Additional examples, responses, etc. can be found at:

[RESTful API Endpoint Docs](https://docs.ayrshare.com/rest-api/endpoints)

[GitHub](https://github.com/ayrshare/social-post-api-python)

See our [changelog](https://docs.ayrshare.com/additional-info/whats-new) for the latest and greatest.

Please [contact us](mailto:support@ayrshare.com) with your questions, or just to give us shout-out 📢!
