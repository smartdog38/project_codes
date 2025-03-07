# 实例模块
__all__ = ["greet","MyClass"]

def greet(name):
    print(f"Hello, {name}")

class MyClass:
    def __init__(self,value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")


def secret_function():
    return "This is a secret."