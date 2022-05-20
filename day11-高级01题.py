# - 使用os模块创建一个名为“黑马”的文件夹
# - 获取黑马文件夹当前所在目录
# - 获取当前的目录列表
# - 改变文件的操作路径
# - 将黑马文件夹删除
import os,shutil
print(os.getcwd())
# 创建黑马的文件夹
if os.path.exists('黑马'):
    print('文件夹已存在')
else:
    os.mkdir('黑马')
# 获取黑马文件夹当前所在目录
os.chdir('黑马')
print(os.getcwd())
# 读取当前目录的列表
list1=os.listdir()
print(list1)
# 改变文件的操作路径
os.chdir('../')
print(os.getcwd())
# 执行删除文件夹的操作
os.rmdir('黑马')  #只能删除空文件夹
shutil.rmtree('黑马') # 删除文件夹，（非空）