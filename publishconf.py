#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'yinhang.blog'
RELATIVE_URLS = False
SOCIAL = (('Github', 'https://github.com/yinhang-e5b0b9e888aa/'), ('RSS', SITEURL + '/feeds/all.atom.xml'))

DELETE_OUTPUT_DIRECTORY = False
