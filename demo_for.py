for i in range(2,5,2):
    print(i)

dict1 = {
    "username":"huang",
    "password":"123456"
}
print(dict1.keys())
print(dict1.values())


# 通过zip方法合并两个list为dict
keys = ["a","b","c","d"]
values = ["1","2","3","4"]
for key,value in zip(keys,values):
    print(key,value)