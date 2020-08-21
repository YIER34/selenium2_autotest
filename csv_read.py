import csv
# 读取本地CSV文件
data = csv.reader(open('info.csv','r'))

# 循环输出每一行信息,通过下标获取所要数据
for user in data:
    print(user)