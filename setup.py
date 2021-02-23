import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.7'
PACKAGE_NAME = 'social-post-api'
AUTHOR = 'Ayrshare'
AUTHOR_EMAIL = 'contact@ayrshare.com'
URL = 'https://github.com/ayrshare/social-post-api-python'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Automate social media posts via Ayrshare\'s API for your company or users. Post to Instagram, Twitter, Facebook, YouTube, LinkedIn, Telegram, and Reddit.'
KEYWORDS = "Ayrshare Social Media API Posting Networks Automation Agency Multiple Users Instagram YouTube Twitter Facebook LinkedIn Reddit Telegram"
HOMEPAGE = "https://www.ayrshare.com"
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'requests'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      keywords=KEYWORDS,
      home_page=HOMEPAGE,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
