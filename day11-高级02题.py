# 编写一段代码以完成两份文件之间的相互备份
# - 提示用户输入文件名。例：gailun.txt
# - 创建已用户输入的名字的文件
# - 打开文件写入如下信息
#       功夫，周星驰
#       一出好戏，黄渤
#       我不是药神，徐峥
# - 将输入的数据输出到终端上
# - 在文件夹中创建gailun副本.txt文件
# - 将gailun.txt文件中的数据写入gailun副本.txt文件中
# - 打开文件，查看文件中内容

# 文件的创建以及文件的写入操作
filename = input('请用户输入文件名：')
f = open(filename, 'a+', encoding='utf-8')
f.write('\t功夫，周星驰')
f.write('\n\t一出好戏，黄渤')
f.write('\n\t我不是药神，徐峥')
# 文件的输出和打印操作
f.seek(0)
str1 = f.read()
print(str1)
# 找到文件的文件名和文件后缀
oldname = filename
index = oldname.rfind('.')
file = oldname[:index]
suffix = oldname[index:]
# 拼接成新的文件名称
newname = file + '副本' + suffix
# 进行文件的拷贝操作
old_f = open(oldname, 'r+', encoding='utf-8')
new_f = open(newname, 'w+', encoding='utf-8')
while True:
    content = old_f.readline()
    if not content:
        break
    new_f.write(content)
new_f.close()
old_f.close()
