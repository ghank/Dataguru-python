#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: aggregationDemo.py
@time: 2016/11/10 12:24
"""

from pymongo import MongoClient
import json
from time import clock

start = clock()
conn = MongoClient('localhost')
db = conn.test
# zips = db.app1.zips
# zips.remove(None)
# f = open('zips.json')
# for line in f:
#     x = json.loads(line)
#     zips.insert_one(x)
# f.close()

#sort
# cursor = zips.aggregate([
#     {'$sort':{'city':1, 'state':1}},
#     {'$project':{
#         '_id':0,
#         'state':1,
#         'city':1,
#         'pop':1
#     }}
# ])

# cursor = db.app1.zips.aggregate( [
#     { '$group': { '_id':"$state", 'totalPop': { '$sum': "$pop" } } },
#     { '$match': { 'totalPop': { '$gte': 10*1000*100 } } }
# ] )

cursor = db.app1.zips.aggregate( [
    { '$group': { '_id':{'state':'$state', 'city':'$city'}, 'pop':{'$sum':'$pop'} } },
    { '$group': {'_id':'$_id.state', 'avgCityPop':{'$avg':'$pop'}}},
    { '$sort':{'avgCityPop': -1}}
])

for doc in cursor:
    print doc

end = clock()
print 'running times is %s.'%(end-start)