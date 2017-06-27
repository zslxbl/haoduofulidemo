# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HaoduofuliDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field()  # 类型
    title = scrapy.Field()  # 标题
    imgurl = scrapy.Field()  # 图片的地址
    yunlink = scrapy.Field()  # 百度云盘的连接
    password = scrapy.Field()  # 百度云盘的密码
    url = scrapy.Field()  # 页面的地址
