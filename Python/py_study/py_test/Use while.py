# while condition:
#     loop body
# while 后面的条件可以是任何表达式，只要为True就一直循环

# while True:  # 无限循环
#     print(1)

# condition 为变量
a = 10
while a:
    print(a)
    a -= 1

# condition 为表达式
x = 10
y = 10
while x > 10 and 10 > y:
    print("x > 10 and y < 10")

# break 跳出循环
while True:
    print(1)
    break

# continue 跳过本次循环
while True:
    print(1)
    continue

# else 语句，只有在循环正常结束时才会执行
while True:
    print(1)
    break
else:
    print("else work")

# 只要对象不为 None 或 False 或 0 ，就一直循环
# 避免陷入死循环，要有钥匙出去的方法