# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import requests
import os
import pymysql




class DoubanmoviePipeline(object):
    # 首次运行工程就打开文件
#    def open_spider(self, spider):
#        self.fp = open('movies.json', 'w', encoding='utf-8')

    # 退出就关闭
#    def close_spider(self, spider):
#        self.fp.close()

    # 此处的item参数就是从film.py中的parse方法返回的
    # 每返回一个item，这里就调用一次
#    def process_item(self, item, spider):
        # print(item)
#        string = json.dumps(item, ensure_ascii=False, indent=4)
#        self.fp.write(string + '\n')

    def process_item(self, item, spider):
         file = open("movies.txt", "a+", encoding='utf-8')
         file.write('电影名：' + item['name'] + '\n上映时间：' + item['release_time'] + '\n导演：' + item['director'] + \
                    '\n时长：' + item['length'] + '\n电影链接：' + item['imdb_link'] + \
                    '\n评分：' + item['mark'] + '\n简介：' + item['summary'] + '\n封面地址:' + item['cover_link'] + '\n\n')
         file.close()
         r = requests.get(item['cover_link'])
         file_name = os.path.join("D:\pic", item['name'] + '.jpg')
         with open(file_name, 'wb') as fp:
             fp.write(r.content)
         print(file_name + '====================================================')
         return item

# 用于数据库存储
class DoubanmovieDBPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            db='gradesign',
            user='root',
            passwd='123456',
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        # 查重处理
        self.cursor.execute(
            """select * from movies where name = %s""",
           item['name'])
        #是否有重复数据
        repetition = self.cursor.fetchone()
        #重复
        if repetition:
            pass
        else:

            self.cursor.execute(
            """insert into movies(name,release_time,director,length,imdb_link,mark,summary,cover_link)
            value (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (item['name'],
             item['release_time'],
             item['director'],
             item['length'],
             item['imdb_link'],
             item['mark'],
             item['summary'],
             item['cover_link']))
        # 提交sql语句
        self.connect.commit()
        return item
