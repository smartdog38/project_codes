import random

print(random.random()) # 0-1之间的随机数
print(random.randint(1,10))  # 1-10之间的随机数,包括1和10的整数
print(random.uniform(1,10)) # 1-10之间的随机数,包括1和10的浮点数

print(random.choice([1,3,5])) # 1、3、5之间的随机数
print(random.sample([1,2,3,4,5],3)) # 1-5之间的随机数,随机选取3个不重复的数


list_a = [1,2,3,4,5]
random.shuffle(list_a)
print(list_a) # list_a,随机打乱顺序

print(random.gauss(0,0.5)) # 随机数,均值为0,方差为0.5


# 设置一个种子，让每次随机的为同一个值
random.seed(10) # 设置常数