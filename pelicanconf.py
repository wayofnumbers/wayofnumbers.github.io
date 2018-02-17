#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# AUTHOR = u'Michael Li'
SITENAME = u'Way of Numbers'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'
STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

AUTHORS = {
    u'Michael Li': '/author.html',
    u'Xiao Xu': 'http://mary.info',
}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/lymenlee'),)

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS= ['./plugins']
PLUGINS = ['ipynb.markup','sitemap']

# TYPOGRIFY = True
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

# Pelican Chameleon
# THEME = "/home/lisper/pelican-themes/pelican-chameleon"
THEME = "/home/lisper/pelican-themes/bulrush"


# THEME = "notmyidea"

# BS3_THEME = 'http://maxcdn.bootstrapcdn.com/bootswatch/3.3.1/flatly/bootstrap.min.css'
# BS3_JS = '/home/lisper/Downloads/jupyter-blog/3rdparty/bootstrap/3.0.0/js/bootstrap.min.js'
# BS3_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css'
# BS3_JS  = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js'
# JQUERY_JS = '/home/lisper/Downloads/jupyter-blog/3rdparty/jquery/jquery-1.10.1.min.js'
# JQUERY_MIGRATE_JS = '/home/lisper/Downloads/jupyter-blog/3rdparty/jquery/jquery-migrate-1.2.1.min.js'




