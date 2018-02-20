#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# AUTHOR = u'Michael Li'
SITENAME = u'Way of Numbers'
SITEURL = 'https://wayofnumbers.github.io/'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'
STATIC_PATHS = ['images', 'extras/logo.svg']

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
SOCIAL = (('Twitter', 'https://twitter.com/lymenlee'),
	  ('GitHub', 'https://github.com/wayofnumbers'),
	  ('LinkedIn', 'www.linkedin.com/in/michael-li-dfw'),
)

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

MARKUP = ('md', 'ipynb')
# STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg']
MENUITEMS = [('Homepage', '/'),('Categories','/categories.html'), ('About', './pages/about.html')]
PLUGIN_PATHS= ['./plugins']
PLUGINS = ['ipynb.markup','sitemap', 'extract_toc']

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

# Pelican Chameleon
# THEME = "/home/lisper/pelican-themes/pelican-chameleon"

'''
#Theme nest configuration
THEME = "/home/lisper/pelican-themes/nest"
SITESUBTITLE = u'A Data Science Blog For The Rest of Us'
# Minified CSS
NEST_CSS_MINIFY = True
# Add items to top menu before pages
MENUITEMS = [('Homepage', '/'),('Categories','/categories.html'), ('About', './pages/about.html')]
# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = 'test.jpg'
NEST_HEADER_LOGO = '/images/logo.png'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Archives', '/archives.html'),('Tags','/tags.html'), ('Authors','/authors.html')]
NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Links'
NEST_COPYRIGHT = u'&copy; Way of Numbers 2018'
# Footer optional
NEST_FOOTER_HTML = ''
# index.html
NEST_INDEX_HEAD_TITLE = u'Home'
NEST_INDEX_HEADER_TITLE = u'Way of Numbers'
NEST_INDEX_HEADER_SUBTITLE = u'A Data Science Blog For The Rest of Us'
NEST_INDEX_CONTENT_TITLE = u'Latest Posts'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts Archives'
NEST_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archives for all posts'
NEST_ARCHIVES_CONTENT_TITLE = u'Archives'
# article.html
NEST_ARTICLE_HEADER_BY = u'By'
NEST_ARTICLE_HEADER_MODIFIED = u'modified'
NEST_ARTICLE_HEADER_IN = u'in category'
# author.html
NEST_AUTHOR_HEAD_TITLE = u'Posts by'
NEST_AUTHOR_HEAD_DESCRIPTION = u'Posts by'
NEST_AUTHOR_HEADER_SUBTITLE = u'Posts archives'
NEST_AUTHOR_CONTENT_TITLE = u'Posts'
# authors.html
NEST_AUTHORS_HEAD_TITLE = u'Author list'
NEST_AUTHORS_HEAD_DESCRIPTION = u'Author list'
NEST_AUTHORS_HEADER_TITLE = u'Author list'
NEST_AUTHORS_HEADER_SUBTITLE = u'Archives listed by author'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categories'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archives listed by category'
NEST_CATEGORIES_HEADER_TITLE = u'Categories'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archives listed by category'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Category Archive'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Category Archive'
NEST_CATEGORY_HEADER_TITLE = u'Category'
NEST_CATEGORY_HEADER_SUBTITLE = u'Category Archive'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Tag archives'
NEST_TAG_HEAD_DESCRIPTION = u'Tag archives'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Tag archives'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tags List'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Tags List'
NEST_TAGS_CONTENT_TITLE = u'Tags List'
NEST_TAGS_CONTENT_LIST = u'tagged'
# Static files
#STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg']
EXTRA_PATH_METADATA = {
#	'extra/robots.txt': {'path': 'robots.txt'},
#	'extra/favicon.ico': {'path': 'favicon.ico'},
	'extra/logo.svg': {'path': 'logo.svg'}
}
''' # end of nest

#elegant
THEME = "/home/lisper/pelican-themes/elegant"
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
LANDING_PAGE_ABOUT = {'title': "Welcome!", 
		      'details' : "We are a small team of researchers, designers, developers that likes to explore. Data science don't have to be boring, and we are here to help."
			}
PROJECTS = [{
    'name': 'Mucraft.net',
    'url': 'http://mucraft.net',
    'description': 'Thoughts about design and UI/UX'},
    ]

#Mail Chimp
MAILCHIMP_FORM_ACTION = "https://github.us17.list-manage.com/subscribe/post?u=c212184cc0965bdf1658f69f0&amp;id=5677a7b75e"
EMAIL_SUBSCRIPTION_LABEL = "Get Monthly Updates"
SUBSCRIBE_BUTTON_TITLE = "Send me Free Updates"	

#comments
COMMENTS_INTRO = "So what do you think? Did I miss anything? Is any part unclear? Leave your comments below."

# THEME = "notmyidea"

# BS3_THEME = 'http://maxcdn.bootstrapcdn.com/bootswatch/3.3.1/flatly/bootstrap.min.css'
# BS3_JS = '/home/lisper/Downloads/jupyter-blog/3rdparty/bootstrap/3.0.0/js/bootstrap.min.js'
# BS3_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css'
# BS3_JS  = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js'
# JQUERY_JS = '/home/lisper/Downloads/jupyter-blog/3rdparty/jquery/jquery-1.10.1.min.js'
# JQUERY_MIGRATE_JS = '/home/lisper/Downloads/jupyter-blog/3rdparty/jquery/jquery-migrate-1.2.1.min.js'




