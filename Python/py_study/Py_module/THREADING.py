#################################################################################################
#################################################################################################
"""

THREADING module
线程（Thread）：操作系统能够调度的最小执行单元，是进程中的一个独立执行流程

可以看为是一个程序的子程序
但是会有一定的限制

"""
#################################################################################################
"""

线程的创建
我们主要通过 threading 模块完成
threading.Thread 是创建线程的核心类，它提供了多种参数和方法来定制线程的行为

"""
#################################################################################################

import threading
import time



#通过 threading.Thread 类创建线程
# 核心参数
# target：指定线程要执行的函数（必填）
# args：传递给 target 函数的位置参数（元组形式）（可选）
# kwargs：传递给 target 函数的关键字参数（字典形式）（可选）
# name：线程名称，默认为 Thread-N（可选 ）
# daemon：是否为守护线程（True/False，默认为 False）（在下一节介绍）

# 定义目标函数
def mytarget(arg, kwarg = 14):
    # threading.current_thread().name 返回当前线程的名字，如果定义了的话
    print(f"线程{threading.current_thread().name}启动")
    print(f"arg: {arg}, kwarg = {kwarg}")
    time.sleep(1)
    print(f"线程{threading.current_thread().name}结束")

# 创建相关线程
thread_1 = threading.Thread(target=mytarget,
                            args=(11,),
                            kwargs={"kwarg":20},name="thread_1")
thread_2 = threading.Thread(target=mytarget,
                            args=(15,),
                            kwargs={"kwarg":26},name="thread_2")

# 创建了但需要显式启动
# 用 start()
thread_1.start()
thread_2.start()

# 等待结束
thread_1.join()
thread_2.join()
print("主程序结束\n-------------------------------------------")
# 线程thread_1启动
# arg: 11, kwarg = 20
# 线程thread_2启动
# arg: 15, kwarg = 26
# 线程thread_1结束
# 线程thread_2结束
# 主程序结束
# -------------------------------------------

#################################################################################################
"""

守护线程
守护线程（Daemon Thread） 是一种特殊类型的线程，其生命周期与主线程紧密绑定

核心特点
主线程退出时，守护线程会立即终止，无论是否完成任务
不会阻止程序退出：程序在所有非守护线程结束后终止，即使守护线程仍在运行
适用场景：后台支持任务（如日志记录、心跳检测、监控等非关键任务）

"""
#################################################################################################、

import threading
import time



# 有两种设置方式


# 守护目标函数
def daemon_target():
    while True:
        print("守护进程工作中...")
        time.sleep(1)

# 非守护目标函数
def non_daemon_target():
    print("非守护进程工作中")
    time.sleep(3)
    print("非守护进程结束")

# 创建守护线程
daemon_thread = threading.Thread(target=daemon_target,daemon=True)
# 创建非守护线程
non_daemon_thread = threading.Thread(target=non_daemon_target)

# 另一种方式就是在 start() 前对其赋值
daemon_thread.daemon = True

# 开启线程
daemon_thread.start()
non_daemon_thread.start()

# 等待得守护线程结束
non_daemon_thread.join()
print("主程序结束\n-------------------------------------------")

# 守护进程工作中...
# 非守护进程工作中
# 守护进程工作中...
# 守护进程工作中...
# 非守护进程结束
# 主程序结束
# -------------------------------------------


# 注意：守护线程可能被突然终止，不会执行 finally 代码块或释放资源
# 守护线程通常用于无限循环任务（如监听网络请求），但需确保主线程退出时能安全终止
# 守护线程的任务可能随时中断，不适合保存数据或提交事务等操作

#################################################################################################
"""

线程类

除了直接使用 threading.Thread 创建线程外，还可以通过继承 Thread 类来创建自定义线程
这种方式提供了更高的灵活性，允许将线程的行为封装到类中，从而实现更复杂的线程逻辑类
这种方式适合需要封装线程逻辑的复杂任务，代码更清晰且可复用

封装性：通过继承 Thread 类，可以将线程的逻辑封装到一个类中，使代码更加模块化和易于维护
扩展性：可以方便地添加额外的属性和方法，扩展线程的功能
代码复用：可以重用线程类的逻辑，创建多个线程实例

"""
#################################################################################################

import threading
import time



# 自定义线程类的步骤
# 继承 threading.Thread 类
# 重写 __init__ 方法（可选，用于传递参数）
# 重写 run() 方法（定义线程执行的核心逻辑）
# 启动线程：调用 start() 方法（自动触发 run()）

class MyThread(threading.Thread):
    # 可以重写__init__ 方法
    def __init__(self, name, delay):
        # 必须调用父类的构造函数
        # 在这里可以将该线程设置为守护线程
        super().__init__(daemon=True)
        # 也可以在下面设置,效果一样
        self.daemon = True
        # 自定义属性
        self.name = name
        # 自定义参数
        self.delay = delay

    # important，线程实现逻辑，当调用 start() 是实现的逻辑
    def run(self):
        print(f"线程 {self.name} 启动")
        time.sleep(self.delay)
        print(f"线程 {self.name} 完成")

# 使用自定义线程类
thread1 = MyThread(name="Thread-A", delay=2)
thread2 = MyThread(name="Thread-B", delay=1)

# 启动线程
thread1.start()
thread2.start()

# 等待线程结束
thread1.join()
thread2.join()
print("主程序结束\n-------------------------------------------")
# 线程 Thread-A 启动
# 线程 Thread-B 启动
# 线程 Thread-B 完成
# 线程 Thread-A 完成
# 主程序结束
# -------------------------------------------


# 必须重写 run() 方法来定义线程的行为。run() 方法是线程的入口点
# 不能直接调用 run() 方法，必须通过 start() 方法启动线程

#################################################################################################
"""

线程的关闭

线程的关闭是一个需要谨慎处理的操作
由于 Python 的线程模型（基于 CPython 的全局解释器锁 GIL）并不直接支持强制终止线程
突然终止线程可能导致锁未释放、文件未关闭、数据未保存等问题
所以 Python 的 threading 模块未提供强制终止线程的 API（设计上避免潜在风险）
因此关闭线程需要通过一些间接的方式实现

"""
#################################################################################################

import threading
import time



# 主要有
# join()       等待线程自然结束（推荐方式）
# Event对象    进行线程间通信来决定结束（复杂时好用）
# Event 实现线程间通信，来控制线程的关闭（下节介绍）

# join()
# 阻塞当前线程：调用 join() 的线程（通常是主线程）
# 会等待目标线程执行完毕，再继续执行后续代码
# thread.join(timeout=None)
# timeout：可选参数，指定最大等待时间（秒）
# 超时后无论目标线程是否完成，当前线程继续执行，且父线程恢复执行
# 返回值：None（无论是否超时）

def my_task():
    print("Thread started.")
    time.sleep(3)  # 模拟耗时操作
    print("Thread finished.")

# 创建线程
thread = threading.Thread(target=my_task)
thread.start()

print("Waiting for thread to finish...")
# 等待线程结束
thread.join()
print("Thread has finished.")
# Thread started.
# Waiting for thread to finish...
# Thread finished.
# Thread has finished.

# 设置 timeout
def my_task():
    print("Thread started.")
    time.sleep(5)  # 模拟耗时操作
    print("Thread finished.")

# 创建线程
thread = threading.Thread(target=my_task)
thread.start()

print("Waiting for thread to finish...")
# 等待最多3秒
thread.join(timeout=3)
print("Thread join timeout reached.")
# Thread started.
# Waiting for thread to finish...
# Thread join timeout reached.
# Thread finished.

#################################################################################################
"""

Event（事件）
threading.Event 是 Python 多线程编程中用于线程间通信的核心同步原语
它通过一个内部标志位实现线程的等待与唤醒机制，能够高效、安全地协调多个线程的执行顺序

Event 的核心机制
内部标志位：Event 对象内部维护一个布尔值（初始为 False），表示某个事件是否发生
线程安全操作：所有方法均为原子操作，无需额外加锁
阻塞唤醒：线程可主动等待标志位变为 True，避免忙等待（busy waiting）消耗 CPU

"""
#################################################################################################

import threading
import time



#Event 的三大方法
# set()	        将内部标志设为 True，唤醒所有等待的线程
# clear()	    将内部标志重置为 False
# wait(timeout)	阻塞当前线程，直到标志为 True 或超时（返回当前标志状态）
# 若在主线程中调用 event.wait()：主线程会卡在阻塞点，直到事件被触发（event.set()）或超时
# 若在子线程中调用 event.wait()：只有该子线程被阻塞，主线程可以继续执行其他代码

# is_set()：检查内部标志是否为 True


# 控制线程启动顺序
# 创建 Event 对象
start_event = threading.Event()

# 目标函数，不需要将 event 丢进去
def worker():
    print("子线程等待启动...")
    # 阻塞直到主线程触发事件
    start_event.wait()
    print("子线程开始工作")

# 创建线程
thread = threading.Thread(target=worker)
# 启动线程
thread.start()

time.sleep(2)
print("主线程触发启动")
# 唤醒子线程
start_event.set()

# 等待线程结束
thread.join()

# 子线程等待启动...
# 主线程触发启动
# 子线程开始工作


# 终止线程，即上面提到的关闭线程
stop_event = threading.Event()
def task():
    while not stop_event.is_set():
        print("线程运行中...")
        time.sleep(1)
    print("线程安全退出")

thread = threading.Thread(target=task)
thread.start()

time.sleep(3)
# 设置终止标志
stop_event.set()

thread.join()


# 多线程同步
# 所有子线程初始化完成后，主线程才继续执行
def worker(ready_event, id):
    print(f"子线程 {id} 初始化中...")
    time.sleep(1)
    ready_event.set()  # 标记当前线程已就绪
    print(f"子线程 {id} 开始工作")

# 创建多个线程的 Event 对象
events = [threading.Event() for _ in range(3)]
threads = [
    # 将 event 与其索引一起传给参数
    threading.Thread(target=worker, args=(event, i))
    for i, event in enumerate(events)
]

# 启动所有线程
for t in threads:
    t.start()

# 主线程等待所有子线程就绪
for event in events:
    # 阻塞直到每个子线程的 Event 被触发
    event.wait()

print("所有子线程已就绪，主线程继续执行")

#################################################################################################
"""

锁（Lock）
在多线程编程中，锁（Lock） 是保证线程安全的核心同步机制
它用于控制对共享资源的访问，防止多个线程同时修改数据导致竞态条件（Race Condition）

锁的核心作用
互斥访问：确保同一时刻只有一个线程能进入临界区（Critical Section），保护共享资源
线程安全：防止数据不一致或损坏（如多个线程同时修改同一变量）

"""
#################################################################################################

import threading
import time



# 锁的创建 Lock()
lock = threading.Lock()


# 获取锁 acquire()
# acquire(blocking=True, timeout=-1)
# blocking（布尔值）:
# True（默认）: 阻塞当前线程，直到获取锁
# False: 非阻塞模式，若锁已被占用，立即返回 False；否则获取锁并返回 True
# timeout（浮点数，单位：秒）:
# 设置最大等待时间。仅当 blocking=True 时有效
# 默认值 -1 表示无限等
# 若超时前未获取锁，返回 False；否则返回 True

# 释放锁 release
# 用完一定释放，不然死锁

if lock.acquire():
    try:
        print("Get Lock")
    finally:
        lock.release()
else:
    print("Lock is acquire")
# Get Lock
print("---------------------------------------------------")


# 进行多线程操作
# 定义锁
lock = threading.Lock()

def mytask():
    print(f"{threading.current_thread().name} 启动")
    if lock.acquire(timeout=1, blocking=True):  # 尝试获取锁，超时时间为3秒
        try:
            print(f"{threading.current_thread().name} 获取锁")
            time.sleep(1)  # 模拟耗时操作
        finally:
            print(f"{threading.current_thread().name} 释放锁")
            lock.release()
    else:
        print(f"{threading.current_thread().name} 超时，继续执行")

# 定义线程名称
names = ["thread_1", "thread_2", "thread_3"]

# 创建线程
threads = [threading.Thread(target=mytask, name=name) for name in names]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("所有线程执行完毕")
# thread_1 启动
# thread_1 获取锁
# thread_2 启动
# thread_3 启动
# thread_1 释放锁
# thread_2 获取锁
# thread_3 超时，继续执行
# thread_2 释放锁
# 所有线程执行完毕
print("---------------------------------------------------")


# 使用 with 来自动管理释放锁
# 但是要设置超时的话
# 还是需要 acquire 来设置
lock_1 = threading.Lock()

def with_target():
    print(f"{threading.current_thread().name} start")
    with lock_1:
        print(f"{threading.current_thread().name} Get Lock")
        time.sleep(1)
    print(f"{threading.current_thread().name} release Lock")

threads = [
    threading.Thread(target=with_target,name = f"thread_{i}")
    for i in range(3)
]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Done")
# thread_0 start
# thread_0 Get Lock
# thread_1 start
# thread_2 start
# thread_0 release Lock
# thread_1 Get Lock
# thread_1 release Lock
# thread_2 Get Lock
# thread_2 release Lock
# Done
print("---------------------------------------------------")

# 另外还有一个函数 locked()
# 检查锁是否被占用
# 占用返回 True，否则返回 False

lock = threading.Lock()

def task():
    if lock.locked():
        print("Lock is already acquired.")
    else:
        print("Lock is available.")

thread = threading.Thread(target=task)
thread.start()
thread.join()
print("---------------------------------------------------")

#################################################################################################
"""

RLock（可重入锁）
允许同一线程多次获取锁的同步机制，适用于需要嵌套或递归加锁的场景

核心特性
可重入性：同一线程可多次调用 acquire() 获取锁，不会导致死锁
计数器机制：内部维护计数器，记录锁被获取的次数
每次 acquire() 计数器加1，release() 计数器减1，归零时锁才真正释放
线程绑定：锁必须由获取它的线程释放，跨线程释放会抛出 RuntimeError
必须确保 acquire() 和 release() 次数匹配，否则可能导致锁无法释放或异常

"""
#################################################################################################

import threading
import time

# create RLock
rlock = threading.RLock()

def nested_task():
    rlock.acquire(timeout=3)
    try:
        print("第一次获取锁")
        # 同一线程再次获取锁（计数器+1）
        rlock.acquire(timeout=3)
        try:
            print("第二次获取锁")
        finally:
            # 计数器-1（未完全释放）
            rlock.release()
    finally:
        # 计数器归零，锁完全释放
        rlock.release()

thread = threading.Thread(target=nested_task)
thread.start()
thread.join()
# 第一次获取锁
# 第二次获取锁

# 使用 with 语句
def safe_operation():
    with rlock:  # 自动获取锁
        print("外层锁")
        with rlock:  # 同一线程再次获取锁
            print("内层锁")
    # 退出时自动释放两次

thread = threading.Thread(target=safe_operation)
thread.start()
thread.join()
# 外层锁
# 内层锁
print("---------------------------------------------------")

#################################################################################################
"""

Condition
threading.Condition 是 Python 多线程编程中用于线程间协调通信的核心同步原语

它结合了锁（Lock 或 RLock）和条件变量机制
允许线程在特定条件下等待或被唤醒，从而高效实现复杂的同步逻辑（如生产者-消费者模型、任务调度等）。

Condition 的核心机制
锁的集成：每个 Condition 对象内部绑定一个锁（默认是 RLock），所有操作需先获取锁
等待队列：调用 wait() 的线程会被放入等待队列，直到被 notify() 或 notify_all() 唤醒
条件检查：必须在循环中检查条件，防止虚假唤醒（Spurious Wakeup）

"""
#################################################################################################

import threading
import time



# Condition 的核心方法
# acquire()	            获取底层锁（与 Lock 或 RLock 相同）。
# release()	            释放底层锁。
# wait(timeout=None)	释放锁并阻塞，直到被唤醒或超时，返回 True 表示因通知唤醒，False 表示超时。
# notify(n=1)	        唤醒等待(wait)队列中的至多 n 个线程
# notify_all()	        唤醒所有等待线程。


# 生产者与消费者模型
import random



# 缓冲区最大容量
MAX_ITEMS = 5
buffer = []
# create condition
condition = threading.Condition()

MAX_ITEMS = 5
buffer = []
condition = threading.Condition()

def producer():
    for i in range(20):
        with condition:
            while len(buffer) >= MAX_ITEMS:
                print("缓冲区已满，生产者等待...")
                condition.wait()
            buffer.append(i)
            print(f"生产: {i}, 缓冲区大小: {len(buffer)}")
            condition.notify_all()
            print("生产者通知消费者")
        time.sleep(0.1)

def consumer():
    for _ in range(20):
        with condition:
            while not buffer:
                print("缓冲区为空，消费者等待...")
                condition.wait()
            item = buffer.pop(0)
            print(f"消费: {item}, 缓冲区大小: {len(buffer)}")
            condition.notify_all()
            print("消费者通知生产者")
        time.sleep(0.2)

# 启动线程
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("所有线程执行完毕\n--------------------------------------------")

#################################################################################################
"""

Semaphore
信号量（Semaphore）是多线程编程中用于控制资源访问和线程同步的重要工具

计数器机制：信号量维护一个整数值，表示可用资源数量
两种核心操作：
P操作（Wait/Acquire）：申请资源，计数器减1；若计数器为0则阻塞
V操作（Signal/Release）：释放资源，计数器加1，唤醒等待线程

"""
#################################################################################################

import threading



# Python 的 threading.Semaphore 类提供以下核心方法：
# acquire(blocking=True, timeout=None)
# P操作：获取信号量，计数器减1
# 若计数器为0：
# blocking=True：线程阻塞，直到其他线程调用 release() 或超时
# blocking=False：直接返回 False（非阻塞模式）
# timeout：设置阻塞等待的最长时间（秒）
# release()
# V操作：释放信号量，计数器加1
# 若计数器超过初始值，抛出 ValueError（但需注意线程安全问题）


# 初始化信号量，允许最多3个线程同时访问
sem = threading.Semaphore(3)

def worker(thread_id):
    sem.acquire()  # 获取信号量
    try:
        print(f"线程 {thread_id} 开始工作")
        time.sleep(1)
    finally:
        print(f"线程 {thread_id} 释放信号量")
        sem.release()  # 释放信号量（确保异常时也能释放）

# 启动5个线程
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print()
# 线程 0 开始工作
# 线程 1 开始工作
# 线程 2 开始工作
# 线程 0 释放信号量
# 线程 1 释放信号量
# 线程 3 开始工作
# 线程 2 释放信号量
# 线程 4 开始工作
# 线程 4 释放信号量
# 线程 3 释放信号量
print("---------------------------------------------------")

#################################################################################################
"""

线程池
Python中的线程池通过concurrent.futures模块的ThreadPoolExecutor实现
适用于I/O密集型任务

"""
#################################################################################################

import threading
from concurrent.futures import ThreadPoolExecutor



# 用 with 来管理线程池，max_workers指定最大线程数
with ThreadPoolExecutor(max_workers=4) as executor:
    # 提交任务，# 计算2^3
    future = executor.submit(pow, 2, 3)
    # 获取结果（阻塞直到任务完成）
    print(future.result())  # 8

# ThreadPoolExecutor 提供了两种主要的任务提交方式：submit() 和 map()
# submit() 方法用于提交单个任务，并返回一个 Future 对象
# Future 对象代表了异步执行的操作，可以通过它来获取任务的结果
def task(arg1, arg2):
    return arg1 + arg2

with ThreadPoolExecutor(max_workers=4) as executor:
    # 提交任务
    future = executor.submit(task, "arg1", "arg2")

    # 获取任务结果
result = future.result()
print(result)  # arg1arg2
# executor.submit()：提交任务，返回 Future 对象。
# future.result()：获取任务的结果（即 return 返回的值）
# 如果任务尚未完成，调用 result() 会阻塞，直到任务完成
print("---------------------------------------------------")

# map() 方法用于批量提交任务，并按顺序返回结果
# 它类似于内置的 map() 函数，但任务会在线程池中并行执行
arg1_list = ["a", "b", "c"]
arg2_list = ["1", "2", "3"]

def task(arg1, arg2):
    return arg1 + arg2

# 批量提交任务
with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(task, arg1_list, arg2_list)
    # 遍历结果
for result in results:
    print(result)
# a1
# b2
# c3
# executor.map()：批量提交任务，返回一个迭代器（里面为函数的结果）
# 结果顺序：结果的顺序与输入参数的顺序一致，即使任务的执行时间不同
# 异常处理：如果某个任务抛出异常，map() 会在迭代结果时抛出异常
print("---------------------------------------------------")


# Future 对象的主要作用是：
# 表示异步任务：Future 表示一个尚未完成的任务，可以用来跟踪任务的状态
# 获取任务结果：任务完成后，可以通过 Future 获取任务的返回值或异常
# 取消任务：如果任务尚未开始执行，可以通过 Future 取消任务
# 回调机制：可以为 Future 添加回调函数，任务完成后自动调用这些回调

# Future 对象的一些常用方法和属性：
# result(timeout=None)
# timeout：可选的超时时间（以秒为单位）
# 如果任务在超时时间内未完成，会抛出 TimeoutError
# 返回值：任务的返回值
# 异常：如果任务抛出异常，调用 result() 时会重新抛出该异常
# done()
# 返回值：如果任务已完成（成功或失败），返回 True；否则返回 False
# cancelled()
# 返回值：如果任务被取消，返回 True；否则返回 False
# cancel()
# 返回值：如果任务成功取消，返回 True；如果任务已经开始执行或已经完成，返回 False
# add_done_callback(callback)
# 为 Future 添加一个回调函数，任务完成后自动调用
# callback：一个可调用对象，接受一个 Future 对象作为参数

#################################################################################################
"""

进程的检测

"""
#################################################################################################

import threading



# is_alive()
# 返回线程是否正在运行（True/False）
# threading.enumerate()
# 返回当前所有活跃线程对象的列表（包括主线程）
# threading.active_count()
# 返回当前活跃线程的数量
# threading.current_thread()
# 返回当前正在执行的线程对象
# threading.main_thread()
# 返回主线程对象（Python 3.4+ 支持）

def mytask():
    print(f"线程 {threading.current_thread().name} 开启\n"
          f"活跃线程：{threading.enumerate()}\n"
          f"活跃线程数：{threading.active_count()}\n"
          f"主线程：{threading.main_thread()}\n"
          f"当前线程是否活跃：{threading.current_thread().is_alive()}\n")

thread_1 = threading.Thread(target=mytask,name="thread_1")
thread_1.start()
thread.join()
# 线程 thread_1 开启
# 活跃线程：[<_MainThread(MainThread, started 5360)>, <Thread(thread_1, started 13068)>]
# 活跃线程数：2
# 主线程：<_MainThread(MainThread, started 5360)>
# 当前线程是否活跃：True

print("---------------------------------------------------")

#################################################################################################
#################################################################################################