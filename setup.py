import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '1.1.1'
PACKAGE_NAME = 'social-post-api'
AUTHOR = 'Ayrshare'
AUTHOR_EMAIL = 'support@ayrshare.com'
URL = 'https://www.ayrshare.com'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Social Media API: Schedule posts, get analytics, add comments for Instagram, Twitter, Facebook, YouTube, LinkedIn, Google My Business, Pinterest, Telegram, TikTok, and Reddit.'
KEYWORDS = "Ayrshare, Social Media API, Social Networks, Social Media Management, Social API, Social Posting, Social Analytics, Social Automation, Agency Social, Multiple User Posting, Instagram, YouTube API, Twitter API, Facebook API, LinkedIn API, Reddit API, Telegram API, Pinterest API, Google My Business API, TikTok API"
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
PROJECT_URLS={
    'Documentation': 'https://docs.ayrshare.com',
    'Source': 'https://github.com/ayrshare/social-post-api-python'
},

INSTALL_REQUIRES = [
    'requests'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      keywords=KEYWORDS,
      project_urls=PROJECT_URLS,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
