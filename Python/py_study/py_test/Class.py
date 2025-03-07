# 类（class）
# 一系列相关行为与数据的封装
#################################################################################################
#################################################################################################
"""

基本形式

 """
#################################################################################################

class MyClass:
    pass

#################################################################################################
"""

类的实例化

"""
#################################################################################################

# 类名()创建类的实例，即类的实例化
myclass = MyClass()

#################################################################################################
"""

属性
分为类属性与实例属性
也分为私有属性与公开属性

"""
#################################################################################################
# 类属性，所有类的实例与类本身都能访问与修改
# 直接在类的内部声明
class MyClass_1:
    name = "Tom"

# 通过类访问 class.attr
print(MyClass_1.name) # Tom

# 通过类修改
MyClass_1.name = "Amy"
print(MyClass_1.name) # Amy

# 通过实例访问 instance.attr
myclass_1 = MyClass_1()
print(myclass_1.name) # Amy

# 注意，这里是所有实例与类共享改属性，所以一个改，全都改
# 通过实例修改
myclass_1.name = "Tom"
print(myclass_1.name) # Tom

# 类属性的添加（最好不要这样做）
MyClass_1.age = 12
print(MyClass_1.age) # 12


# 实例属性，在类的内部声明，用 self 区别于类属性 self.attr
# 属于实例，修改只会更改该实例的值
# 可以在方法直接赋值，也可以在__init__()即类的初始化方法里赋值
class MyClass_2:
    school = "NUJUPT"
    def __init__(self,age): # 需要在实例化时给的参数
        self.name = "Tom" # 可以直接赋值
        self.age = age

myclass_2 = MyClass_2(22)
print(myclass_2.school,myclass_2.name,myclass_2.age) # NUJUPT Tom 22

# 实例属性的修改
myclass_2.name = "Amy"
print(myclass_2.name) # Amy

# 实例属性的添加（强烈不要）
myclass_2.ID = "Q230000"
print(myclass_2.ID) # Q230000


# 私有属性，虽然没有啥限制机制
# 但是可以让人知道该属性不能被外界访问
# 以 _ 和 __ 来申明
# _ 可以被直接访问，而 __ 会触发改写机制，需要通过 _class__attr 来访问
# 其实就是你写了 _class__attr 它就会去找 __ 开头的 attr
# 可以避免子类覆盖掉该属性
class MyClass_3:
    _school = "NJUPT"
    __age = 11
    def __init__(self):
        self._name = "Tom"
        self.__ID = "Q23"

myclass_3 = MyClass_3()

# 直接调用
print(MyClass_3._school)

# 通过 _class__attr 调用
print("MyClass_3:" + f"{MyClass_3._MyClass_3__age}")

# 直接调用
print(myclass_3._name)

# 实例私有属性也是用这个来调用
print(myclass_3._MyClass_3__ID)

#################################################################################################
"""

方法
即类里的函数，有一定区别
有类方法、实例方法、静态方法
也分为私有方法与共有方法

"""
#################################################################################################

# 类方法
# 用 @classmethod 修饰的方法
# 默认第一个参数为 cls，即类本身，可以改
# 可以调用类属性，不能调用实例属性
class Myclass_4:
    school = "NJUPT"
    @classmethod
    def sayhi(cls):
        print(f"Hello, I'm from {cls.school}")

# 调用类方法
Myclass_4.sayhi()

# 有参数的类方法
class Myclass_5:
    school = "NJUPT"
    @classmethod
    def sayhi(cls,name):
        print(f"Hello, I'm from {cls.school},I'm {name}")

Myclass_5.sayhi("Tom")


# 实例方法
# 默认第一个属性为self，即实例本身
# 可以调用实例属性（self）与类属性（class）
# 也能传参
class MyClass_6:
    school = "NJUPT"
    def __init__(self,name):
        self.name = name
    def sayhi(self,age):
        print(f"Hi,I'm from {MyClass_6.school}, I'm {self.name} ,I'm {age}")

# 创建实例后，调用实例方法
myclass_6 = MyClass_6("Tom")
myclass_6.sayhi(15)


# 静态方法
# 用 @staticmethod 修饰
# 不调用类属性与实例属性
# 没有必要的参数 self 或 cls
# 当这个方法与类相关，但不会涉及其属性的时候可以使用
class MyClass_7:
    @staticmethod
    def sayhi(name):
        print(f"Hi! {name}")

# 直接用类名调用即可
MyClass_7.sayhi("Tom")


# 私有方法
# 与私有属性一样， _ 可以访问，但 __ 需要 _class__method() 来访问
# 可以防止子类覆盖该方法
class MyClass_8:
    def _sayhi(self):
        print("Hi!")
    def __saybye(self):
        print("Bye!")

myclass_8 = MyClass_8()
myclass_8._sayhi() # Hi!
myclass_8._MyClass_8__saybye() # Bye!

#################################################################################################
#################################################################################################
"""

继承（重要）
Python里类的最重要的特点
分为单继承与多继承


"""
#################################################################################################
"""

基本格式

"""
#################################################################################################

# object 类为所有对象的父类
# MyClass_a 继承 object 类
class MyClass_a(object):
    pass

#################################################################################################
"""

单继承
即只继承一个父类

"""
#################################################################################################
"""

属性继承
自动继承类属性
实例属性要初始化

"""
#################################################################################################

# 子类会自动继承父类的类属性
class Parent_A:
    name = "Tom"

class Parent_B(Parent_A):
    pass

print(Parent_B.name) # Tom


# 子类默认初始化父类的实例属性
# 因为会自动继承__init__()方法
# 但是如果要在子类也写自己的__init__()方法而又保留父类的实例属性
# 一般需要在 __init__() 方法里调用 super().__init__()
# 也可以调用 parent.__init__(self) 来显式指定继承父类的初始化方法
# 来进行父类的实例属性的初始化
class Animal:
    def __init__(self, name):
        self.name = name  # 实例属性

class Dog(Animal):
    def __init__(self, name, breed):
        # 调用父类的 __init__ 方法
        super().__init__(name)
        # 同样，但是可以直接用父类名指定，但是要传入子类的 self 进去
        Animal.__init__(self,name)
        self.breed = breed

# 创建子类对象
dog = Dog("Buddy", "Golden Retriever")
print(dog.name)   #  Buddy（继承自父类）
print(dog.breed)  #  Golden Retriever（子类新增属性）


# 私有属性的继承
class Parent:
    def __init__(self):
        self._protected_attr = "受保护的属性"
        self.__protected_attr2 = "受保护的属性"
class Child(Parent):
    pass

child = Child()
print(child._protected_attr) # 受保护的属性
# 这里是父类的类名
print(child._Parent__protected_attr2) # 受保护的属性

#################################################################################################
"""

方法继承
子类会自动继承父类的所有方法，包括实例方法、类方法和静态方法
如果子类没有同名的方法就会直接调用父类的方法
就是去父类找函数然后调用
但如果有属性，就要处理好当中的关系

"""
#################################################################################################

# 继承实例方法
class Animal:
    def speak(self):
        return "Unknown sound"

class Dog(Animal):
    pass

# 创建子类对象
dog = Dog()
print(dog.speak())  # Unknown sound（继承自父类）


# 继承类方法
class Animal:
    @classmethod
    def info(cls):
        return f"This is {cls.__name__}"

class Dog(Animal):
    pass

# 调用类方法
print(Dog.info())  # This is Dog


# 继承静态方法
class Animal:
    @staticmethod
    def is_animal():
        return True

class Dog(Animal):
    pass

# 调用静态方法
print(Dog.is_animal())  # 输出: True


# 继承魔术方法
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal(name={self.name})"

class Dog(Animal):
    pass

# 创建子类对象
dog = Dog("Buddy")
print(dog)  # 输出: Animal(name=Buddy)


# 继承私有方法
class Parent:
    def _protected_method(self):
        return "父类的受保护方法"

    def __protected_method(self):
        return "父类的受保护方法"

class Child(Parent):
    pass

child = Child()
print(child._protected_method()) # "父类的受保护方法"
# 这里也是父类名
print(child._Parent__protected_method()) # "父类的受保护方法"

#################################################################################################
"""

方法重写（方法覆盖）
在子类写了与父类同名的方法，那么就会执行子类定义的方法
而不会调用父类的方法
注意与 C++ 不同
只要同名就会重写，不管参数

"""
#################################################################################################

# 重写类方法
class Animal:
    @classmethod
    def info(cls):
        return f"This is {cls.__name__}"

class Dog(Animal):
    @classmethod
    def info(cls):
        return f"This is a {cls.__name__} and it barks"

# 调用类方法
print(Dog.info())  # 输出: This is a Dog and it barks


# 重写实例方法
class Animal:
    def speak(self):
        return "Unknown sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# 创建子类对象
dog = Dog()
print(dog.speak())  # 输出: Woof!


# 重写静态方法
class Animal:
    @staticmethod
    def is_animal():
        return True

class Dog(Animal):
    @staticmethod
    def is_animal():
        return "Yes, it's a dog"

# 调用静态方法
print(Dog.is_animal())  # 输出: Yes, it's a dog


# 重写静态方法
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal(name={self.name})"

class Dog(Animal):
    def __str__(self):
        return f"Dog(name={self.name})"

# 创建子类对象
dog = Dog("Buddy")
print(dog)  # 输出: Dog(name=Buddy)


# 重写私有方法
class Parent:
    def _protected_method(self):
        return "父类的受保护方法"
    def __private_method(self):
        return "父类的私有方法"

class Child(Parent):
    def _protected_method(self):
        return "子类重写的受保护方法"
    def __private_method(self):
        return "子类重写的私有方法"

# 创建子类对象
child = Child()
print(child._protected_method())  # 子类重写的受保护方法
# 注意这里为子类名
print(child._Child__private_method()) # 子类重写的私有方法

#################################################################################################
"""

多继承
即继承多个父类

"""
#################################################################################################
"""

MRO(Method Resolution Order)
Python 中用于确定多继承中属性和方法调用顺序的规则

"""
#################################################################################################

"""
当多个父类有同名方法时，MRO 决定了子类调用哪个父类的方
MRO 通过 C3 线性化算法，确保方法的调用顺序是唯一且合理

MRO 遵循以下规则:
子类的方法优先于父类的方法
在多继承中，父类的顺序是从左到右
如果一个类在 MRO 中出现在另一个类之前，那么它的所有父类也会在该类之前出现
即先找完一个类及其父类再找下一个
如果出现了之前找过的父类直接换到下一个父类，确保一个父类只出现一次

如果类的继承关系导致 MRO 无法满足单调性，Python 会抛出 TypeError
"""


# class.mro() 查看当前类的 MRO 顺序
class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

#################################################################################################
"""

继承属性
与单继承一样

"""
#################################################################################################

# 继承实例属性
class A:
    def __init__(self):
        self.a = "A 的实例属性"

class B:
    def __init__(self):
        self.b = "B 的实例属性"

class C(A, B):
    def __init__(self):
        A.__init__(self)  # 调用 A 的 __init__ 方法
        B.__init__(self)  # 调用 B 的 __init__ 方法

# 创建子类对象
obj = C()
print(obj.a)  # 输出: A 的实例属性
print(obj.b)  # 输出: B 的实例属性


# 继承类属性
class A:
    class_attr_a = "A 的类属性"

class B:
    class_attr_b = "B 的类属性"

class C(A, B):
    pass

# 访问类属性
print(C.class_attr_a)  # A 的类属性
print(C.class_attr_b)  # B 的类属性


# 继承受保护属性
class A:
    def __init__(self):
        self._protected_attr_a = "A 的受保护属性"

class B:
    def __init__(self):
        self._protected_attr_b = "B 的受保护属性"

class C(A, B):
    def __init__(self):
        A.__init__(self)  # 调用 A 的 __init__ 方法
        B.__init__(self)  # 调用 B 的 __init__ 方法

# 创建子类对象
obj = C()
print(obj._protected_attr_a)  # 输出: A 的受保护属性
print(obj._protected_attr_b)  # 输出: B 的受保护属性


# 继承私有属性
class A:
    def __init__(self):
        self.__private_attr_a = "A 的私有属性"

class B:
    def __init__(self):
        self.__private_attr_b = "B 的私有属性"

class C(A, B):
    def __init__(self):
        A.__init__(self)  # 调用 A 的 __init__ 方法
        B.__init__(self)  # 调用 B 的 __init__ 方法

obj = C()
# 通过改写后的名称访问
print(obj._A__private_attr_a)  # 输出: A 的私有属性
print(obj._B__private_attr_b)  # 输出: B 的私有属性


# 属性冲突时按照 MRO 来继承
class A:
    attr = "A 的属性"

class B:
    attr = "B 的属性"

class C(A, B):
    pass

# 访问属性
print(C.attr)  # A 的属性（遵循 MRO）

#################################################################################################
"""

方法继承
也与单继承一样
如果多个父类有同名类方法，子类会继承 MRO 中第一个父类的类方法
就不写了

"""
#################################################################################################
"""

方法重写
与单继承类似
直接重写就行

"""
#################################################################################################
"""

抽象类（ABC）
用作基类，即不实例化
作为其他类的模板
ABC 为所有抽象类的基类
需要模块 abc
继承的子类需要实现所有抽象方法才能实例化
如果子类还有抽象方法，那么子类也是抽象类
与接口类似
不过接口不含实现，但是抽象类能含实现的函数体

"""
#################################################################################################

# 分别修饰抽象实例方法，抽象属性，抽象类方法，抽象静态方法

from abc import ABC, abstractmethod,abstractproperty,abstractclassmethod,abstractstaticmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("Sleeping...")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog()
cat = Cat()
dog.make_sound()  # Woof!
cat.make_sound()  # Meow!
dog.sleep()  # Sleeping...
cat.sleep()  # Sleeping...
print(dir(Cat))

#################################################################################################
"""

类的多态
对于一个函数，不同的类的实现不一样
只要给函数传入父类
并调用父类的方法
那么所有子类传入后，就会调用子类重写的相应方法

"""

#################################################################################################

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# 多态的使用
def animal_sound(animal):
    print(animal.speak())

# 创建不同的动物对象
dog = Dog()
cat = Cat()
duck = Duck()

# 调用同一个函数，传入不同的对象
animal_sound(dog)  # 输出: Woof!
animal_sound(cat)  # 输出: Meow!
animal_sound(duck)  # 输出: Quack!

#################################################################################################
"""

类修饰器
与函数修饰器类似，但是作用与类
有很大的不同

"""
#################################################################################################

# 定义修饰器，传入类
def log_class(cls):
    # 一个类来定义修饰的行为
    class Wrapper:
        def __init__(self, *args, **kwargs):
            # 定义初始化的逻辑
            self.wrapped = cls(*args, **kwargs)

        # 定义参数的逻辑
        def __getattr__(self, name):
            print(f"Accessing attribute: {name}")
            return getattr(self.wrapped, name)

    return Wrapper

@log_class
class MyClass:
    def __init__(self, value):
        self.value = value

    # 简单的逻辑
    def display(self):
        print(f"Value: {self.value}")


obj = MyClass(10)
obj.display() # Accessing attribute: display \n Value: 10

#################################################################################################
"""

属性装饰器
使用 @property 来修饰
属性装饰器用于将方法转换为属性，从而控制属性的访问
还可以定义对应的 setter 和 deleter 方法

"""
#################################################################################################

# 实现只读，即当你有想保护的属性时，又不想用函数来调用，就可以进行这个操作
class MyClass:
    def __init__(self, value):
        self._value = value

    # 将方法变为属性，一定要有返回值
    @property
    def value(self):
        return self._value


obj = MyClass(10)
print(obj.value)  # 输出: 10
# obj.value = 20  # 抛出 AttributeError (因为 value 是只读属性)


# 通过 @属性名.setter 可以为属性定义赋值逻辑
# 即在为 属性（被修饰的方法） 赋值时调用验证
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

circle = Circle(5)
print(circle.radius)  # 输出: 5
circle.radius = 10
print(circle.radius)  # 输出: 10
# circle.radius = -5  # 抛出 ValueError: Radius must be positive.

# 当你要在内部计算某些值并实时分给属性时很好用，也可以缓存数据
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rectangle = Rectangle(4, 5)
print(rectangle.area)  # 20
rectangle = Rectangle(4, 6)
print(rectangle.area)  # 24




# 通过 @属性名.deleter，可以为属性定义删除逻辑
# 即当你运行 del attr 时调用的逻辑函数
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Deleting radius")
        del self._radius


circle = Circle(5)
print(circle.radius)  # 输出: 5
del circle.radius  # 输出: Deleting radius
# print(circle.radius)  # 抛出 AttributeError: 'Circle' object has no attribute '_radius'

#################################################################################################
"""

一些特殊的方法

"""
#################################################################################################

# __getattr__ 与 __setattr__

# __getattr__ 在访问一个不存在的属性时被调用
# 如果属性存在，Python 会直接返回该属性的值
# 如果属性不存在，Python 会调用 __getattr__ 方法
class DynamicAttributes:
    def __getattr__(self, name):
        if name == "age":
            return 25
        raise AttributeError(f"'DynamicAttributes' object has no attribute '{name}'")

obj = DynamicAttributes()
print(obj.age)  # 25
# print(obj.name)  # 抛出 AttributeError: 'DynamicAttributes' object has no attribute 'name'


# __setattr__ 方法在设置属性时被调用，无论是已存在的属性还是新属性
class RestrictedAttributes:
    def __init__(self):
        self._internal_data = {}

    # name 为属性名，value 为设置的值
    def __setattr__(self, name, value):
        if name.startswith("_"):
            # 注意在 __setattr__ 中设置属性时
            # 必须使用 super().__setattr__ 不然会有递归调用
            super().__setattr__(name, value)  # 允许设置私有属性
        else:
            self._internal_data[name] = value  # 将属性存储到字典中

    # name为
    def __getattr__(self, name):
        if name in self._internal_data:
            return self._internal_data[name]
        raise AttributeError(f"'RestrictedAttributes' object has no attribute '{name}'")


obj = RestrictedAttributes()
obj.name = "Alice"
obj.age = 25
print(obj.name)  # Alice
print(obj.age)  # 25
print(obj._internal_data)  # {'name': 'Alice', 'age': 25}


# __getattribute__ 方法与 __getattr__ 类似，但它会在访问任何属性时被调用，无论属性是否存在

#################################################################################################

# __get__、__set__ 与 __delete__
# 是Python的描述符
# 描述符是一种对象属性访问的底层机制，用于控制属性的获取、设置和删除行为
# 通过实现这些方法，可以创建自定义的描述符类，从而实现属性的精细控制
# 描述符是一个实现了 __get__、__set__ 或 __delete__ 方法的对象
# 描述符通常用于类属性，而不是实例属性

# __get__(self, instance, owner)：在访问属性时调用
# instance：访问属性的实例
# owner：属性所属的类
class Square:
    # 在这里实现要访问的属性的逻辑
    def __get__(self, instance, owner):
        return instance.side ** 2

class Shape:
    # 对想要控制的属性加描述符
    area = Square() # 描述符，类属性

    def __init__(self, side):
        self.side = side

shape = Shape(5)
# 当访问 area 这个类属性时调用描述符
# 到 get 找到 shape.side 来返回
print(shape.area)  # 25


# __set__(self, instance, value)：在设置属性时调用
# instance：设置属性的实例。
# value：要设置的值
class PositiveNumber:
    # 实现设置对应的属性的逻辑
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Value must be positive.")
        # 使用 _ 防止递归，因为instance里有value，无限循环set
        instance._value = value

    # 这里对应的要控制访问的属性
    # 即当你访问 value 实际返回的是 _value
    def __get__(self, instance, owner):
        return instance._value


class MyClass:
    # 为控制的属性申明描述符
    value = PositiveNumber()

    def __init__(self, value):
        # 这里的调用了 value ，进而调用 __set__()
        self.value = value

obj = MyClass(10)
print(obj.value)  # 输出: 10
# obj.value = -5  # 抛出 ValueError: Value must be positive.


# __delete__(self, instance)：在删除属性时调用
# instance：删除属性的实例
class ProtectedAttribute:
    def __set__(self, instance, value):
        instance._value = value

    def __get__(self, instance, owner):
        return instance._value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete this attribute.")

class MyClass:
    value = ProtectedAttribute()  # value 是一个描述符

    def __init__(self, value):
        self.value = value


obj = MyClass(10)
print(obj.value)  # 10
# del obj.value  # AttributeError: Cannot delete this attribute.

#################################################################################################
"""

属性修饰符与描述符都可以对类的属性进行一定的限制
但是两者的使用范围不一样
当类很少时，或有特定的要求时使用属性修饰符
而当有多个类都要进行限制时，使用描述符会更好

"""
#################################################################################################

# __enter__ 和 __exit_
# __enter__ 和 __exit__ 是 Python 中用于实现上下文管理的特殊方法
# 通过实现这两个方法，可以让对象支持 with 语句，从而简化资源管理

# __enter__ 方法在进入 with 代码块时调用，通常用于资源的初始化
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    # 返回文件对象
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# 使用 with 语句
with FileManager("example.txt", "w") as f:
    f.write("Hello, World!")


# __exit__ 方法在退出 with 代码块时调用，无论代码块是否发生异常。它接收三个参数
# exc_type：异常类型（如果没有异常，值为 None）
# exc_value：异常实例（如果没有异常，值为 None）
# traceback：异常的堆栈信息（如果没有异常，值为 None）
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if exc_type is not None:
            # exc_value 就是引起异常时所带的信息
            print(f"An exception occurred: {exc_value}")
        return True  # 返回 True 抑制异常

# 使用 with 语句
with FileManager("example.txt", "w") as f:
    f.write("Hello, World!")
    raise ValueError("Oops! An error occurred.")

#################################################################################################

# __slot__
# __slots__ 是 Python 中用于优化类属性存储的特殊属性
# 通过定义 __slots__，可以显式声明类实例允许的属性
# 从而避免使用默认的 __dict__ 字典来存储属性
# 这种方式可以节省内存并提高属性访问速度。
class Person:
    __slots__ = ["name", "age"]  # 只允许 name 和 age 属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(person.name)  # 输出: Alice
print(person.age)   # 输出: 25

# 尝试动态添加属性
# person.address = "123 Street"  # AttributeError: 'Person' object has no attribute 'address'


# __slots__ 在继承时的行为需要注意：
# 如果子类没有定义 __slots__，它会继承父类的 __slots__，但仍然会拥有 __dict__
# 如果子类定义了 __slots__，它会合并父类和子类的 __slots__
class Parent:
    __slots__ = ["name"]

class Child(Parent):
    __slots__ = ["age"]

child = Child()
child.name = "Alice"
child.age = 25
# child.address = "123 Street"  # 抛出 AttributeError

print(child.name)  # 输出: Alice
print(child.age)   # 输出: 25

#################################################################################################

# __call__()
# __call__ 方法允许将类的实例像函数一样调用
class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x

add_five = Adder(5)
# instance()来调用__call__()
print(add_five(10))  # 输出: 15

#################################################################################################

# __new__ ()
# 用于控制实例的创建过程，通常用于单例模式或不可变对象
class Singleton:
    _instance = None
    # 设置只能存在一个实例
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # 输出: True

#################################################################################################

# __del__()
# 在对象被销毁时调用，通常用于资源清理
class Resource:
    def __del__(self):
        print("Resource is being deleted.")

resource = Resource()
del resource  # 输出: Resource is being deleted.

#################################################################################################
#################################################################################################


#################################################################################################
"""

想查看类的方法与属性可以使用dir()

"""
#################################################################################################
#################################################################################################
#################################################################################################