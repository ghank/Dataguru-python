#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: mongoDemo.py
@time: 2016/11/9 19:46
"""
# import pymongo
# from pymongo import MongoClient
#
# conn = MongoClient('localhost')
# db = conn.dataguru
# users = db.app1.users
#
# u1 = {
#     'name':'zhang',
#     'mails':['abc@def', 'bcd@efg']
# }
#
# x = users.insert_one(u1)
# print type(x), x.inserted_id
#
# props = ['name', 'mails']
# us = [ ['zhao', ['abc@def', 'bcd@efg']],
#        ['qian', ['abc@def', 'bcd@efg']],
#        ['sun', ['abc@def', 'bcd@efg']],
#        ['li', ['abc@def', 'bcd@efg']],
# ]

# ul = [dict(zip(props, u)) for u in us]
# print ul
# users.insert_many(ul, ordered=False)

# import json
# from bson import json_util
# cursor = users.find()
# cursor = users.find({'name':'zhang'})
# cursor = users.find({'name':{'$in':['zhang', 'li']}})
#年龄大于25岁
# cursor = users.find({'age':{'$gt':25}})
# cursor = users.find({'name':{'$in':['zhang', 'li']},
#                      'mails':{'$size':2}
#                      }
#                     )

# or
# cursor = users.find({'$or':[ {'name':{'$in':['zhang', 'li']}},
#                              {'mails': {'$size':2}}
#                            ]
#                      }
#                     )

#3 更新
# users.update_many(
#     {},
#     {'$set':{'age':23}},
#     # {'$unset':{'age':''}}
# )

#年龄字段增加2
# users.update_many(
#     {},
#     {'$inc':{'age':2}}
# )

#min
# users.update_many(
#     {'name':
#          {'$in':['zhang', 'li']}
#     },
#     {'$min':
#          {'age':20}
#     }
# )

#日期 时间戳
# users.update_many(
#     {'name':
#          {'$in':['zhang', 'li']}
#     },
#     {'$currentDate':
#          {'create_time':True,#日期的格式
#           'mod_time':{'$type':'timestamp'}
#          }
#     }
# )

# for user in cursor:
#     print json.dumps(user, indent=4, default=json_util.default)

from pymongo import MongoClient

client = MongoClient()
db = client.test

from datetime import datetime
result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)


