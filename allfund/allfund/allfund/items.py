# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AllfundItem(scrapy.Item):
    # define the fields for your item here like:
    fund_id = scrapy.Field()
    fund_name = scrapy.Field()
    one_month = scrapy.Field()
    three_month = scrapy.Field()
    six_month = scrapy.Field()
    one_year = scrapy.Field()
    three_year = scrapy.Field()
    from_start = scrapy.Field()