# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

def dbHandle():
    conn = pymysql.connect(
        host = 'localhost',
        db = 'STOCK',
        user = 'root',
        passwd = '111111',
        charset = 'utf8',
        use_unicode = True        
    )
    return conn
    
class AllfundPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()

        sql = 'insert into STOCK.Dfcf_allfund(id,name,1m,3m,6m,1y,3y,fs)\
                values(%s,%s,%s,%s,%s,%s,%s,%s)'
        lis = (item['fund_id'],item['fund_name'],item['one_month'],item['three_month'],item['six_month'],item['one_year'],item['three_year'],item['from_start'])
        try:
            cursor.execute(sql,lis)
            dbObject.commit()
            print(item['fund_name'],'writen sucessed')
        
        except Exception as e:
            print('DB writer failllllll',e)
            dbObject.rollback()
        else:
            #print('DB writer success')
            dbObject.close()

        return item