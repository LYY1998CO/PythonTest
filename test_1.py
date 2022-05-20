import json
str = '[1,2,3,4]'
print(type(str))
print(str)
# 通过 json.loads(data) 方法把josn数据转化为了 python数据
str = json.loads(str)
print(str)
print(type(str))
# 通过 json.dumps(data) 方法把python数据转化为了 json数据
str = json.dumps(str)
print(type(str))
print(str)

