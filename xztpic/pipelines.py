# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

import requests


class XztpicPipeline(object):
    def process_item(self, item, spider):
        header = {
            'USER-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'referer': item['referer']
        }
        # 所有图片放在一个文件夹下
        dir_path = 'D:\\PyCharm\\xztpic\\pic\\mm131\\{}'.format(item['title'])
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        for src,alt in zip(item['src'], item['alt']):
            with open('{}//{}.jpg'.format(dir_path, alt), 'wb') as f:
                req = requests.get(src, headers=header)
                f.write(req.content)
        return item
