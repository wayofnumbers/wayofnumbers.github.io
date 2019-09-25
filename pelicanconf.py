# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
IGNORE_FILES = ['.ipynb_checkpoints']


# AUTHOR = 'Michael Li'
SITENAME = 'Way of Numbers'
SITEURL = 'https://wayofnumbers.github.io'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
STATIC_PATHS = ['images', 'extras/logo.svg']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

AUTHORS = {
    'Michael Li': '/author.html',
    'Xiao Xu': 'http://mary.info',
}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/lymenlee'),
          ('Medium', 'https://medium.com/@lymenlee'),
          ('GitHub', 'https://github.com/wayofnumbers'),
          ('LinkedIn', 'www.linkedin.com/in/michael-li-dfw'),
          )

TWITTER_USERNAME = 'lymenlee'


DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

MARKUP = ('md', 'ipynb')
# STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg']
MENUITEMS = [('Homepage', '/'), ('Categories', '/categories.html'),
             ('About', './pages/about.html')]
PLUGIN_PATHS = ['./pelican-plugins', './plugins']
PLUGINS = ['ipynb.markup', 'sitemap', 'extract_toc',
           'neighbors', 'tipue_search', 'readtime']

TYPOGRIFY = True

'''
MENUITEMS = [
    ('Home', '/'),
    ('Archives', [
        ('Tags', '/tags.html'),
        ('Categories', '/categories.html'),
        ('Chronological', '/archives.html'),
        ]),
    ('Find Us', [
        ('Email', 'mailto: lemuel.li@gmail.com'),
        ('Github', 'https://github.com/wayofnumbers/wayofnumbers.github.io'),
        ('Twitter', 'https://twitter.com/lymenlee'),
        ]),
    ('About', './pages/about.html'),
    ]
'''


# Configuration for the "sitemap" plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'monthly'
    }
}

DISQUS_SITENAME = "way-of-numbers"


# elegant
THEME = "./pelican-themes/elegant"
# MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc(anchorlink=true)']
DIRECT_TEMPLATES = (('index', 'tags', 'categories',
                     'archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
# added only for elegent theme, which does not process the favicon with this.
USE_SHORTCUT_ICONS = True
LANDING_PAGE_ABOUT = {'title': "Data science for the rest of us.",
                      'details': "We are a small team of researchers, designers, developers that likes to explore. Data science don't have to be boring, and we are here to help."}
SITESUBTITLE = "Data science for the rest of us."

PROJECTS = [{
    'name': 'Mucraft.net',
    'url': 'http://mucraft.net',
    'description': 'Thoughts about design and UI/UX'},
    {
    'name': 'Pelican Read Time Plugin',
    'url': 'https://github.com/wayofnumbers/pelican-readtime',
    'description': 'A Pelican plugin that can display estimated read time on the website'},
]

# Mail Chimp
MAILCHIMP_FORM_ACTION = "https://github.us17.list-manage.com/subscribe/post?u=c212184cc0965bdf1658f69f0&amp;id=5677a7b75e"
EMAIL_SUBSCRIPTION_LABEL = "Get Monthly Updates"
SUBSCRIBE_BUTTON_TITLE = "Send me Free Updates"

# comments
COMMENTS_INTRO = "So what do you think? Did I miss anything? Is any part unclear? Leave your comments below."

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'permalink': 'true'},

    },
    'output_format': 'html5',
}
