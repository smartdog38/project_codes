# assignment operation
x = 1
x += 1 # x = x + 1
print(x) # 2
x -= 1 # x = x - 1
x *= 2 # x = x * 2
x /= 2 # x = x / 2
x %= 2 # x = x % 2
x **= 2 # x = x ** 2
x //= 2 # x = x // 2
x = 1 # &| ^ 的优先级比赋值运算符低，且不能在 float 与 int 之间进行运算
x &= 2 # x = x & 2 , 按位与
x |= 2 # x = x | 2 ， 按位或
x ^= 2 # x = x ^ 2 ，按位异或
x = -x # x = -x

# logic operation
# 优先级：not > and > or
x = 1
y = 0
print(x and y) # 1，全真返回最后一个真值，假返回第一个假值
print(x or y) # 2，返回第一个真值，或最后一个假值
print(not x) # 0，返回布尔值的反值

# comapre operation
x = 1
y = 2
print(x == y) # False
print(x != y) # True
print(x > y) # False
print(x < y) # True
print(x >= y) # False