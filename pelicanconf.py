#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'yinhang'
SITENAME = u"银行的冒菜馆"
SITEURL = '/'

# Regional Settings
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {'zh': '%Y-%m-%d'}
DEFAULT_LANG = u'zh'

# Plugins and extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {
            'permalink': 'true'
        },
        'markdown.extensions.meta': {},
        'markdown.extensions.admonition': {},
    }
}

PLUGIN_PATHS = ['plugins/']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img',
           'neighbors', 'render_math', 'related_posts', 'assets', 'share_post',
           'series']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
THEME = 'themes/elegant'
TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

# Social
SOCIAL = (('Github', 'https://github.com/yinhang-e5b0b9e888aa/'), ('RSS', SITEURL + '/feeds/all.atom.xml'))

# TODO
# CLAIM_GOOGLE = "Bk4Z5ucHLyPXqlZlj5LzANpYBBSvxqBW4E8i-Kwf-bQ"
# CLAIM_BING = "8FF1B025212A47B5B27CC47163A042F0"

# Elegant theme
STATIC_PATHS = ['theme/images', 'images', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}
}
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'与我联系'
RELATED_POSTS_LABEL = '相关文章'
SHARE_POST_INTRO = '分享到：'
COMMENTS_INTRO = u'评论'

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = u'邮件订阅'
EMAIL_FIELD_PLACEHOLDER = u'您的邮箱。。。'
SUBSCRIBE_BUTTON_TITLE = u'确认订阅'
# TODO
MAILCHIMP_FORM_ACTION = u'empty'

# SMO
TWITTER_USERNAME = u''
# TODO
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

# Legal
SITE_LICENSE = """对于本人发布的原创内容，如果没有特殊注明，默认采用<a rel="license" 
    href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>协议"""

# SEO
SITE_DESCRIPTION = u'个人技术博客，记录工作和学习中踩过的坑以及可能需要查阅的知识'

# Landing Page
PROJECTS = [
    {
        'name': '数据科学教程',
        'url': 'https://github.com/yinhang-e5b0b9e888aa/tutorials',
        'description': '做数据科学技术分享时用过的演讲资料，文件格式为jupyter notebook，不是PPT'
    },
    {
        'name': '杂乱无章的技术笔记', 'url': 'https://github.com/yinhang-e5b0b9e888aa/notes',
        'description': '通过Emacs Deft管理的原始技术笔记，其中部分内容已经格式化发布在博客上'
    }
]

LANDING_PAGE_ABOUT = {
    'title': '',
    'details': """<p>该博客记录了我在工作和学习中踩过的坑以及可能需要查阅的知识</p>
    <p>最大的作用，可能就是在遇到同样问题的时候，可以很快地在博客中找到解决办法</p>"""
}
