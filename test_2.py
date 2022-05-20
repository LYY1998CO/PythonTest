tuple1=('a','b','c','d','e')
print(tuple1)
print(type(tuple1))
print('-'.join(tuple1))

# 元组中的每个元素是数值类型的情况下，join方法不能适用，见下案例：
# tuple2=(1,2,3,4,5)
# print(tuple2)
# print(type(tuple2))
# print('-'.join(tuple2))