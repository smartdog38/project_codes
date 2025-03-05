# if 后面只要不是 None 或 False 或 0 ，就执行该语句块
# 变量
a = 1
if a:
    print(a)
# 一行语句的话可以写成单行
if a: print(a)

# if 后面的条件可以是任何表达式，只要为True就执行该语句块
a = 1
if a > 1:
    print(a)

# elif 后面的条件可以是任何表达式，只要为True就执行该语句块
# if 与 elif 的条件要不一样，先从上往下判断，正确了就执行，不再往下判断
# 不正确就继续往下判断
a = 1
if a > 1:
    print(a)
elif a < 1:
    print(a)
elif a == 1:
    print(a)

# else 语句，只有在 if 和 elif 都不满足时才会执行
a = 1
if a > 1:
    print(a)
elif a < 1:
    print(a)
else:
    print(a)


# 多条件判断
# not and or
# is is not

