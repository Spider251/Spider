import pymongo

# 创建数据库连接对象
conn = pymongo.MongoClient("localhost",'27017')

# 创建库对象
db = conn.spiderdb
# 创建集合对象
myset = db.t1

# 在t1集合中插入1条文档
myset.insert_one({"name":"Tom"})

print("OK!")


'''
show dbs
use spiderdb
show collections
db.t1.find().pretty()
db.t1.count()
删除库 db.dropDatabase()
'''