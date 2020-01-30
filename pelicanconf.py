#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

AUTHOR = "Michael Li"
SITENAME = "Way of Numbers"
SITESUBTITLE = "Data science for the rest of us."
SITEURL = ""

PATH = "content"

# Regional Settings
TIMEZONE = "America/Chicago"
DATE_FORMATS = {"en": "%b %d, %Y"}

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": " "},
    }
}

PLUGIN_PATHS = ['./pelican-plugins', './plugins']
PLUGINS = ['ipynb.markup', 
	    'sitemap', 
	    'extract_toc',
	    'neighbors', 
            'tipue_search', 
            'readtime',
        ]
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Appearance
THEME = "./pelican-themes/elegant"
TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

# Social
SOCIAL = (('Twitter', 'https://twitter.com/lymenlee', 'My Twitter'),
          ('Medium', 'https://medium.com/@lymenlee', 'Medium Page'),
          ('GitHub', 'https://github.com/wayofnumbers', 'GitHub'),
          ('LinkedIn', 'www.linkedin.com/in/michael-li-dfw', 'LinkedIn'),
          )

# Elegant theme
STATIC_PATHS = ["theme/images", "images", "extra/_redirects", 'extras/logo.svg']

EXTRA_PATH_METADATA = {"extra/_redirects": {"path": "_redirects"}}

if os.environ.get("CONTEXT") == "production":
    STATIC_PATHS.append("extra/robots.txt")
    EXTRA_PATH_METADATA["extra/robots.txt"] = {"path": "robots.txt"}
else:
    STATIC_PATHS.append("extra/robots_deny.txt")
    EXTRA_PATH_METADATA["extra/robots_deny.txt"] = {"path": "robots.txt"}

DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search", "404"]
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Like this post? Share on:"
COMMENTS_INTRO = "So what do you think? Did I miss something? Is any part unclear? Leave your comments below."

# Email Subscriptions
EMAIL_SUBSCRIPTION_LABEL = "Get New Release Alert"
EMAIL_FIELD_PLACEHOLDER = "Enter your email..."
SUBSCRIBE_BUTTON_TITLE = "Notify me"

FREELISTS_NAME = "oracle-l"
FREELISTS_FILTER = True

# SMO
TWITTER_USERNAME = ""
FEATURED_IMAGE = SITEURL + "/theme/images/apple-touch-icon-152x152.png"

# Legal
SITE_LICENSE = """Content licensed under <a rel="license nofollow noopener noreferrer"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Attribution 4.0 International License</a>."""
HOSTED_ON = {"name": "Netlify", "url": "https://www.netlify.com/"}

# SEO
SITE_DESCRIPTION = (
    "Michael Li's blog, talks about data science, design and code."
)

# Landing Page
PROJECTS_TITLE = "Related Projects"
PROJECTS = [{
    'name': 'Mucraft.net',
    'url': 'http://mucraft.net',
    'description': 'Thoughts about design and UI/UX'},
    {
    'name': 'Pelican Read Time Plugin',
    'url': 'https://github.com/wayofnumbers/pelican-readtime',
    'description': 'A Pelican plugin that can display estimated read time on the website'},
]

LANDING_PAGE_TITLE = "Data Science for the Rest of Us."

AUTHORS = {
    "Michael Li": {
        "url": "https://medium.com/@lymenlee",
        "blurb": "is the creator and lead developer of this site.",
        "avatar": "/images/michael.png",
    },
    
}
DISQUS_FILTER = True
UTTERANCES_FILTER = True


# Mail Chimp
MAILCHIMP_FORM_ACTION = "https://github.us17.list-manage.com/subscribe/post?u=c212184cc0965bdf1658f69f0&amp;id=5677a7b75e"
EMAIL_SUBSCRIPTION_LABEL = "Get Monthly Updates"
SUBSCRIBE_BUTTON_TITLE = "Send me Free Updates"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

MARKUP = ('md', 'ipynb')

DISQUS_SITENAME = "wayofnumbers"
DISQUS_SECRET_KEY = u'emdNyAftwShoAixVUdjO9C0buzpX2myI4UwvfytW1d5Yg0Jb5WzaAEimNhpZTvsR'
DISQUS_PUBLIC_KEY = u'7phihyH3j4px5cCgD5epLyzPsNyC11T3e0hwy9QwB1EjhFbfH4rCBf3AVPGaUzgV'
