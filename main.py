#!/usr/bin/python
# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
#广度优先
execute('scrapy crawl mm131_breadth'.split())
#深度优先
#execute('scrapy crawl mm131_depth'.split())
