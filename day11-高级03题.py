# 创建一个新项目中新创建一个名字py文件夹
# 进入py文件夹中创建5个文件，
# 文件名分别为python基础班-1.txt，
# python基础班-2.txt，
# python基础班-3.txt，
# python基础班-4.txt，
# python基础班-5.txt
# 然后将py文件夹中的所有文件都改名为
# [黑马]python基础班-1.txt，
# [黑马]python基础班-2.txt，
# [黑马]python基础班-3.txt，
# [黑马]python基础班-4.txt，
# [黑马]python基础班-5.txt

import os, time

print(os.getcwd())
if os.path.exists('py'):
    print('文件夹已经存在，无需重新创建')
else:
    os.mkdir('py')
os.chdir('py')
# print(os.getcwd())
for i in range(1, 6):
    f = open(f'python基础班-{i}.txt', 'w', encoding='utf-8')
f.close()
for i in range(1, 6):
    os.rename(f'python基础班-{i}.txt', f'[黑马]python基础班-{i}.txt')

# import shutil,os
# print(os.getcwd())
# shutil.rmtree('py')
