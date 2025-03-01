#定义函数
#def function_name(parameter):
#    return value #return 语句返回函数的返回值，可以省略，即默认返回 None
#可以加上注释文档
#def function_name(parameter):
#    """
#    function_name(parameter)
#    """
#    return value

#调用函数
#function_name(parameter)

#函数的参数
#1.必选参数
#def add(a,b):
#    return a+b
#print(add(1,2))

#2.默认参数
#def add(a,b=1):
#    return a+b
#print(add(1))

#3.可变参数
#def add(*args):#args 是一个tuple
#    return sum(args)
#print(add(1,2,3,4,5))

#4.关键字参数
#def add(**kwargs):#kwargs 是一个dict
#    return sum(kwargs.values())
#print(add(a=1,b=2,c=3,d=4,e=5))

#5.命名关键字参数
# def greet(name, *, age, city):
#     print(f"Hello, {name}. You are {age} years old and live in {city}.")
# greet("Bob", age=20, city="New York")
#*号是为了区分位置参数和关键字参数

#6.参数组合
#def add(a,b,c=0,*args,**kwargs):
#    return a+b+c+sum(args)+sum(kwargs.values())
#print(add(1,2,3,4,5,a=1,b=2,c=3,d=4,e=5))

#参数的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数、关键字参数！！！

#函数的作用域
#函数内部的变量称为局部变量，函数外部的变量称为全局变量
#局部变量只能在函数内部访问，全局变量可以在函数内部和外部都可以访问
#在函数内部创建的变量，如果不使用global关键字，那么这个变量就是局部变量；
# 如果使用global关键字，那么这个变量就是全局变量
#如果在函数外有了全局变量，那么在函数内设立了同名的全局变量，也会对外部设立的全局变量进行修改

#特殊参数/,*
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
# 用*与**不仅区别了位置参数和关键字参数，还能对列表与字典进行解包
# *person_info 将列表 ["Alice", 30] 解包为位置参数 "Alice" 和 30
# **person_info 将字典中的键值对 {"name": "Charlie", "age": 35} 解包，并将键作为参数名，值作为对应的参数值传递给 greet() 函数