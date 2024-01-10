# 调式scrapy 爬虫框架脚本
from scrapy.cmdline import execute

import sys
import os
"""
D:/python_workspace/ArticleSpider/main.py
D:/python_workspace/ArticleSpider
D:\python_workspace\ArticleSpider
"""
# print(__file__)
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    execute(["scrapy", "crawl", "jobbole"])