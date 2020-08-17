import sys
sys.path.append("project/model") # 将model目录添加到系统环境变量path下
from model import new_count

test = new_count.B()

print(test.add(2,5))