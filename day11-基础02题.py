f=open('movie.txt','r+',encoding='utf-8')
# 一次性全部读取
# str1=f.read()
# print(str1)
# 每次读取一行
str1=f.readline()
print(str1,end='')
str1=f.readline()
print(str1,end='')
str1=f.readline()
print(str1,end='')
