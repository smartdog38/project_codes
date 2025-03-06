# 基本函数
def helloworld():
    print("HelloWorld")
# 调用
helloworld() # HelloWorld

# 带参数的函数
def greet(name):
    print("Hello, "+ name )
greet('Amy') # Hello, Amy
greet('Tom') # Hello, Tom

# 带返回值的函数
def add(a, b):
    return a + b
sum_ab = add(1, 2)
print(sum_ab)


# 参数的类型：位置参数-关健词参数
# 位置参数不用指明参数名，但要严格按照位置进行赋值
# 关键词参数指明参数名，要严格按照位置进行赋值
def diff(a,b):
    return a-b
diff_ab = diff(4,1)
print(diff_ab) # 3
diff_ab = diff(b = 1, a =4)
print(diff_ab) # 3

# 默认参数，可以不要赋值。在函数定义时赋值,可以改
def power(a,b = 4):
    return a*b
print(power(3)) # 12
print(power(2,3)) # 6
print(power(a = 2, b = 3)) # 6

# 可变位置参数
def pp(*args): # 可以是 *a 等等，但最好规范为args。接受不定数量的位置参数
    for arg in args: # args 是一个元组
        print(arg)
pp('a','b','c')

# 可变关键词参数
def print_kwargs(**kwargs): # 接受不定数量的关键词参数
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="Alice", age=25)  #  name: Alice, age: 25
# 可以看到关键词参数与默认参数有点像，但不是一个概念
# 默认参数在函数定义时定义参数，而关键词参数则是在函数调用时赋值参数

# 混合参数
def func(a, b, *args, c=10, **kwargs):
    # 可以看到，默认参数放在可变位置参数后，可变关键词参数前
    # 因为如果有可变位置参数，要修改默认参数就要用关键词来赋值
    print(f"a: {a}, b: {b}, args: {args}, c: {c}, kwargs: {kwargs}")
func(1, 2, 3, 4, c=20, name="Alice", age=25)
# a: 1, b: 2, args: (3, 4), c: 20, kwargs: {'name': 'Alice', 'age': 25}

# / 限制前面都为 位置参数
def func(a, b, /, c, d):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
func(1, 2, 3, 4)      # 正确，a 和 b 不能是关键字参数

# * 限制后面都为关键词参数
def func(a, b, *, c, d):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
func(1, 2, c=3, d=4)  # 正确，c 和 d 必须是关键字参数

# 函数的解包，字典的 ** 会将其解到值 {a} 为 kwargs["a"]
def func(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")
args = (1, 2, 3)
func(*args)  # a: 1, b: 2, c: 3
kwargs = {"a": 1, "b": 2, "c": 3}
func(**kwargs)  # 输出: a: 1, b: 2, c: 3

# 参数顺序 位置参数-仅限位置参数-默认参数-仅限关键字参数-可变关键字参数
def func(a, b, /, c=10, *, d, **kwargs):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}, kwargs: {kwargs}")

func(1, 2, c=20, d=30, name="Alice")  # 输出: a: 1, b: 2, c: 20, d: 30, kwargs: {'name': 'Alice'}


# 匿名函数 lambda 函数（少用）
add = lambda a, b: a + b # a, b为参数
print(add(3, 5))  # 输出: 8


# 函数的作用域
# 嵌套作用域
def outer():
    x = 10  # 外层函数的局部变量
    def inner():
        print("内层函数 x:", x)  # 内层函数可以访问外层函数的变量
    inner()
outer() # 内层函数 x: 10
# 使用 nonlocal 可以在嵌套函数中修改外层函数的变量
def outer():
    x = 10  # 外层函数的局部变量
    def inner():
        nonlocal x
        x = 20  # 修改外层函数的变量
        print("内层函数 x:", x)
    inner()
    print("外层函数 x:", x)
outer()
# 内层函数 x: 20
# 外层函数 x: 20

# 全局变量
x = 10  # 全局变量
def func():
    print("函数内部 x:", x)  # 函数可以访问全局变量
func()
# 函数内部 x: 10
# 使用 global 可以在函数里修改全局变量
x = 10  # 全局变量
def func():
    global x
    x = 20  # 修改全局变量
    print("函数内部 x:", x)
func()
print("函数外部 x:", x)
# 内层函数 x: 20
# 外层函数 x: 20
# 尽量减少全局变量的使用，以避免命名冲突和性能问题


# 函数递归
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # 输出: 120


# 函数作为返回值与参数
def apply(func, x, y): # 不能直接 fun(x,y)，如果要参数，将参数一起传进
    return func(x, y)
def add(a, b):
    return a + b
result = apply(add, 3, 5)
print(result)  # 输出: 8


# 闭包，函数内定义函数
# 并且内层函数保留了外层函数的变量，修饰器的基础结构
def outer():
    x = 10  # 外层函数的局部变量
    def inner():
        print(x)  # 内层函数引用了外层函数的变量
    return inner
closure = outer()  # 调用 outer 函数，返回 inner 函数
closure()  # 输出: 10


# Last，注释文档"""六个双引号"""
def aa():
    """
    function describe:

    require modules:

    parameters:

    returns:

    """
    pass