#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hans Fangohr'
SITENAME = 'Introduction to Python for Computational Science and Engineering'
SITESUBTITLE = 'Hans Fangohr'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-octopress-theme"
#THEME_STATIC_DIR = "/home/pelican/pelican-octopress-theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# switches from original pelicanconf.py:
#MENUITEMS = [('About', 'about.html'),
#             ('Archive', 'archives.html'),
#             ('Tags', 'tags.html'), ]


# Must have tag-pages at the same level as / for paths to images to work
#TAG_URL = 'tag-{slug}.html'
#TAG_SAVE_AS = 'tag-{slug}.html'

#CATEGORY_URL = 'category-{slug}.html'
#CATEGORY_SAVE_AS = 'category-{slug}.html'
#CATEGORY_SAVE_AS = False  ## Pelican 3.3 warns about this, so remove for now.

#AUTHOR_URL = 'author-{slug}.html'
#AUTHOR_SAVE_AS = 'author-{slug}.html'

# Blogroll
LINKS = (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'))
          #('Jinja2', 'http://jinja.pocoo.org'),
          #('You can modify those links in your config file', '#'),)

LINKS =  ( ('Hans Fangohr home page', 'http://www.southampton.ac.uk/~fangohr'),)
    #('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          #('Python.org', 'http://python.org'),
          #('Computational Modelling Group Southampton', 'http://cmg.soton.ac.uk'),
          #('CDT Next Generation Computational Modelling', 'http://www.ngcm.soton.ac.uk'),
          #('Institute for Complex Systems Simulations', 'http://www.icss.soton.ac.uk'),
          #('Hans Fangohr home page', 'http://www.southampton.ac.uk/~fangohr'),)





# Social widget
SOCIAL = (('ProfCompMod', 'https://twitter.com/ProfCompMod'),)
          #('NGCM_Soton', 'https://twitter.com/NGCM_Soton'),
         #)

    #,
    #      ('Another social link', '#'),)

DEFAULT_PAGINATION = 15

FEED_DOMAIN = SITEURL
# FEED_ATOM = 'feeds/all.atom.xml'


DISQUS_SITENAME = 'hansfangohr'

TWITTER_USERNAME= "ProfCompMod"
TWITTER_USER = 'ProfCompMod'

GOOGLE_ANALYTICS = "UA-45946250-1"

NEWEST_FIRST_ARCHIVES = True

#STATIC_PATHS = ['images', 'images/research', 'code', 'notebooks', 'favicon.png']

DISPLAY_PAGES_ON_MENU = True

TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'
