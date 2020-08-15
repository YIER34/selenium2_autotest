class A():
    def add(self,a,b):
        return a + b
count = A()
print(count.add(3,5))

# 初始化方法
class A():
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def add(self):
        return self.a + self.b

count = A("4",5)
print(count.add())


# 类的继承
class A():
    def add(self,a,b):
        return a + b

class B(A):
    def sub(self,a,b):
        return a - b
print(B().add(5,6))
