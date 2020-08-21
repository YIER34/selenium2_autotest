# 读取txt文件
# read()  读取整个文件
# readline()  读取一行数据
# readlines()  读取所有行的数据

# 通过open()的方法以读("r")的形式打开数据文件
# 使用readlines()方法按行读取文件
user_file = open('user_info.txt','r')
lines = user_file.readlines()
user_file.close()

# 通过split()方法拆分数据
for line in lines:
    username = line.split(',')[0]
    password = line.split(',')[1]
    print(username,password)