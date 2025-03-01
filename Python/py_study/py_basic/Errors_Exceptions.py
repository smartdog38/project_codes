#错误（Error）
#语法错误（SyntaxError）



#异常（Exception）
#异常处理
# try:
#     # 可能会引发异常的代码
#     pass
# except Exception as e:
#     # 处理异常的代码
#     pass
# finally:
#     # 不管是否有异常发生都会执行的代码
#     pass

#可以有多个except语句，用于处理不同类型的异常
# import sys
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

#try...except...else...finally
# try:
#     # 可能会引发异常的代码
#     pass
# except Exception as e:
#     # 处理异常的代码
#     pass
# else:
#     # 没有异常发生时执行的代码
#     pass
# finally:
#     # 不管是否有异常发生都会执行的代码
#     pass

# raise 语句用于引发异常
# raise 语句可以不带任何参数，这种情况下，它会重新引发最近的异常
# raise 语句可以带有一个异常类型参数，这种情况下，它会引发指定类型的异常
# raise 语句可以带有一个异常类型和一个值参数，这种情况下，它会引发指定类型的异常，并把值参数传递给该异常.
# raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
#异常处理并不仅仅处理那些直接发生在 try 子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常

# rasie ecxeption from excetion instance #这是指是 ecxeption instance 里的异常

#自定义异常
# class MyError(Exception):#继承自Exception
#     pass
#
# def test():
#     raise MyError
#
# try:
#     test()
# except MyError:
#     print('MyError 被捕获')

#异常处理的优先级
# try:
#     # 可能会引发异常的代码
#     pass
# except Exception1 as e:
#     # 处理异常1的代码
#     pass
# except Exception2 as e:
#     # 处理异常2的代码
#     pass
# except Exception3 as e:
#     # 处理异常3的代码
#     pass
# 先1，再2，再3

# 可以收集多个异常然后一起处理
# excs = [OSError('error 1'), SystemError('error 2')]
# 将异常收集到一个列表中
# 引起异常组
# raise ExceptionGroup('there were problems', excs)

# except*  处理异常组里特定的异常，使其他的异常正常传播
# try:
#     # 代码抛出一个异常组
#     raise ExceptionGroup("多个异常", [
#         ValueError("发生了 ValueError"),
#         TypeError("发生了 TypeError"),
#         KeyError("发生了 KeyError"),
#     ])
# except* ValueError as e:
#     print(f"捕获到 ValueError: {e}")
# except* KeyError as e:
#     print(f"捕获到 KeyError: {e}")
# except Exception as e:
#     print(f"捕获到其他异常: {e}")

# 用 add_note 来给异常增加注释

# 断言assert
# 用于判断一个表达式，在表达式条件为 false 的时候触发异常
# 用法：assert expression

