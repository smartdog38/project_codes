# 生成器
# 使用 yield 来生成序列

# 简单的生成器函数
def simple_generator():
    print("yield 1")
    yield 1
    print("yield 2")
    yield 2
    print("yield 3")
    yield 3

gen = simple_generator() # 返回一个生成器对象，不会执行函数
print(next(gen))  # yield 1 1，用next()来运行生成器到yield结束并返回值
print(next(gen))  # yield 2 2
print(next(gen))  # yield 3 3
for i in simple_generator(): # 用 for 也能运行生成器
    print(i)


# 用 send 向生成器发送值并恢复其运行
def generator_with_send():
    x = yield "开始"
    yield f"接收到: {x}"
gen = generator_with_send()
print(next(gen))  # 开始
print(gen.send(42))  #  接收到: 42


# 用 throw 向生成器抛出异常
def generator_with_throw():
    try:
        yield "开始"
    except ValueError as e:
        yield f"捕获异常: {e}"
gen = generator_with_throw()
print(next(gen))  # 开始
print(gen.throw(ValueError("错误")))  # 捕获异常: 错误


# 用 close 关闭生成器
def generator_with_close():
    try:
        yield "开始"
    except GeneratorExit:
        print("生成器已关闭")

gen = generator_with_close()
print(next(gen))  # 输出: 开始
gen.close()  # 输出: 生成器已关闭
