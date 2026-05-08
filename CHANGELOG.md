# Changelog

## [1.3.0] 2026-05-08

- Added `set_twitter_byo(api_key, api_secret)` and `clear_twitter_byo()` for X/Twitter Bring-Your-Own-Keys support. When set, every outbound request includes `X-Twitter-OAuth1-Api-Key` and `X-Twitter-OAuth1-Api-Secret` headers — required for X/Twitter operations now that Ayrshare's BYO requirement is enforced (as of March 31, 2026).
- README: removed duplicated paragraphs, fixed typos (e.g. capabilities, Google Business Profile), corrected links (update post, generate alt text), tightened intro copy.

## [1.2.5] 2026-01-20
- Updates missing endpoint base url reference from app.ayrshare.com to api.ayrshare.com

## [1.2.4] 2024-12-13

- Updated `setProfileKey` method to set the profile key for the SocialPost object.

## [1.2.3] 2024-12-13

- Updated README with new docs.

## [1.2.1] 2024-09-20

- Added new endpoints with examples including resize, verify, generate, webhooks, and more. Please see README for details.
- Added new test cases.
- Switch endpoint calls from app.ayrshare.com to api.ayrshare.com.
- Updated packages.

## [1.1.1] 2022-11-17

- Updated code examples and docs.

No breaking changes.
