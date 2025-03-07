# 类
# 类本身也是对象

# 类的定义
# class MyClass:
#     pass

# 类里的语句里大部分为函数的定义，称为方法


# 类属性与实例属性
# 类最好不要用列表等可变数据作为类属性，而是用列表等可变数据作为实例属性
# class MyClass:
#     a = 1 # 类属性
#     def __init__(self, b): # 构造函数,输入的参数在这里定义为实例属性
#         self.b = b # 实例属性
# print(MyClass.a) # 1
# MyClass1 = MyClass(2)
# print(MyClass1.b) # 2
# 类属性更改后，所有实例都会受到影响
# 实例属性更改，只有该实例会收到影响
# 如果类的类属性与实例属性重复，则会找到实例属性（最好避免）
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# rect = Rectangle(5, 10)
# rect.color = "blue"  # 这个是用户添加的属性，最好与实例的属性名不同


# 类方法与实例方法
# class MyClass:
#     @classmethod # 类方法必须要加的修饰器
#     def Class_method(cls): # cls 代表类本身
#         print("This is a class method")
#     def Instance_method(self): # self 代表实例本身
#         print("This is a instance method")
#
# MyClass.Class_method() # This is a class method
# MyClass1 =  MyClass() #生成一个MyClass的实例
# MyClass1.Instance_method() # This is a instance method
#
# 方法可以可以定义在类外面
# def f1(self, x, y):
#     return min(x, x+y)
# class C:
#     f = f1 # 赋值给类里的属性，最好别这么写
#
# 最重要的两个方法：
# 构造方法：__init__() # 初始化方法
# 析构方法：__del__() # 程序最后将对象销毁前做的清理工作
#
# 类里的方法互相调用时用self
# class MyClass:
#     def f1(self, x, y):
#         return min(x, x+y)
#     def f2(self, x, y):
#         return self.f1(x, y) # 调用 f1
#
# 继承
# class BaseClassName: # 基类
    # pass
# class DerivedClassName(BaseClassName): # 继承基类的派生类
#     pass
# 这个也能继承其他模块里的类
# class  DerivedClassName(module.BaseClassName):
#
# 类的重写
# 如果派生类里有与基类同名的方法，那么就会重写基类的方法
# 如果想要调用基类的方法，可以用super()，也可以用 BaseClassName.methodname(self, arguments)
# 继承的类会继承来自基类的方法，如果没有改写，那么就会延用方法，可以递归
# 查询类的方法是从派生类一直往上找到对顶层的基类的方法
#
# 两个检测方法
# isinstance( obj, Class) # 检测obj是否是Class类型
# issubclass( Class1, Class2) # 检测Class1是否是Class2的子类
#
# 多继承
# class Base1:
#     pass
# class Base2:
#     pass
# class Base3:
#     pass
# class DerivedClassName(Base1, Base2, Base3): # 继承 Base1, Base2, Base3
#     pass
# 多继承采用深度搜索，从左到右搜索，不重复查找相同类
# 即先找 Base1 及其父类，找到完了再找 Base2 及其父类，找到完了再找 Base3 及其父类
# 如果是砖石类，会有共同的父类，父类也只会找一次
# 一个类被继承并且有新的父类加入，那么这个新的父类加入不会改变已存在父类的优先顺序
#
# 带有__的为私有方法与属性，避免与子类的方法与属性重名
#
#
# 数据类
# from dataclasses import dataclass
# @dataclass
# class DataClass:
#     name: str
#     age: int
# p = DataClass(name="Alice", age=30) # 数据类的实例化
#
# 在 Python 中，代码往往并不依赖于传递特定的类或类型，而是关注对象是否实现了所需的行为。
# 这种灵活性使得可以将实现了所需方法的任何对象传递给函数或方法，
#
# 实现类的迭代
# class Reverse:
#     """Iterator for looping over a sequence backwards."""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]

# 多态
# 1. 方法重写实现多态
# class Animal:
#     def speak(self):
#         pass  # 基类不实现具体行为
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# animals = [Dog(), Cat()]
#
# for animal in animals:
#     print(animal.speak())  # 输出 "Woof!" 和 "Meow!"
#
# 2.  通过函数实现多态
# class Bird:
#     def fly(self):
#         return "I can fly high!"
#
# class Penguin:
#     def fly(self):
#         return "I cannot fly."
#
# def make_it_fly(animal):
#     print(animal.fly())
#
# bird = Bird()
# penguin = Penguin()
#
# make_it_fly(bird)    # "I can fly high!"
# make_it_fly(penguin) # "I cannot fly."
# 这就是鸭子类型（Duck Typing），即不关注对象的类型，只关注它是否具有某个方法
#
# 3. 抽象类和接口实现多态
# from abc import ABC, abstractmethod
#
# class Animal(ABC):  # 继承 ABC 变成抽象类
#     @abstractmethod
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# # animal = Animal()  #报错，不能实例化抽象类
# dog = Dog()
# cat = Cat()
#
# print(dog.speak())  # Woof!
# print(cat.speak())  # Meow!
# Animal 是一个抽象类，不能被直接实例化
# Dog 和 Cat 必须 实现 speak() 方法，否则报错
#
# 4. 运算符重载（特殊方法）
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):  # 重载 +
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __str__(self):  # 重载 str() 方法
#         return f"Vector({self.x}, {self.y})"
#
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# print(v1 + v2)  # 输出 Vector(4, 6)
