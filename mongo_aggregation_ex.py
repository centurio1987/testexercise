from pymongo import MongoClient
import json

client = MongoClient()
db = client.aggr_ex

result = db.zips.aggregate([
    {'$group':{'_id': '$state', 'total_pop':{'$sum':'$pop'}}},
    {'$match':{'total_pop':{'$gt':'10'}}}
])

for elem in result:
    print(elem)