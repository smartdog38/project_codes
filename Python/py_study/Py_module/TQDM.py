#################################################################################################
#################################################################################################
"""

TQDM module
Python的tqdm库是一个高效、灵活的工具，用于在循环和长时间运行的任务中显示进度条
实时显示进度条，支持迭代次数、剩余时间、速度等信息

"""

#################################################################################################
"""

基本用法

"""
#################################################################################################

from tqdm import tqdm
import time



# 基本格式
# for i in tqdm(iterable, total(tqdm 自己判断))
#   函数逻辑


# 对于列表、元组、集合等已知长度的可迭代对象
# 即用 len() 获得的数
data = [1,2,3,4,5]
print(len(data)) # 5
for item in tqdm(data, desc="处理列表"):
    time.sleep(0.2)


# 对于生成器或其他未知长度的可迭代对象
# 如果可迭代对象没有__len__方法（如生成器），需手动指定total
def generate_data(n):
    for i in range(n):
        yield i

n = 10
generator = generate_data(n)
for item in tqdm(generator, total=n, desc="处理生成器"):
    time.sleep(0.1)


# 如果不想以 1 来增加进度
# 可以自己手动控制
with tqdm(total=100) as pbar:
    # 每十个进行一次操作
    for i in range(10):
        time.sleep(0.1)
        # 使用 update() 手动更新进度
        pbar.update(10)

#################################################################################################
"""

处理文件与流式数据

"""
#################################################################################################

from tqdm import tqdm



# 逐行读取文件
file_path = r"D:\code\Python\py_study\Py_module\data\json_test.json"
with open(file_path, "r") as f:
    # 获取总行数（可选）
    total_lines = sum(1 for _ in f)
    f.seek(0)  # 重置文件指针
    for line in tqdm(f, total=total_lines, desc="读取文件"):
        time.sleep(0.1)


# 手动更新未知长度的迭代
# 比如流式数据
# with tqdm(desc="流式处理", unit="item") as pbar:
#     while True:
#         data = get_stream_data()  # 假设每次获取一个数据块
#         if not data:
#             break
#         process(data)
#         pbar.update(1)  # 手动更新进度

#################################################################################################
"""

处理嵌套循环与复杂迭代

"""
#################################################################################################

from tqdm import tqdm


# 处理嵌套循环
outer_loop = range(3)
inner_loop = range(100)

for i in tqdm(outer_loop, desc="外层循环"):
    # leave=False内层完成后不保留
    for j in tqdm(inner_loop, desc="内层循环", leave=False):
        time.sleep(0.01)

#################################################################################################
"""

相关参数与设置

"""
#################################################################################################

# bar_format             完全自定义进度条格式
# desc                   左侧描述文本
# colour                 颜色设置
# ncols                  进度条宽度
# unit 和 unit_scale     单位与自动缩放
# postfix：              右侧动态信息

from tqdm import tqdm



# bar_format
# 占位符：
# {l_bar}       左侧信息（描述+进度条）
# {bar}         进度条本身
# {r_bar}       右侧信息（百分比、时间等）
# {n_fmt}       当前进度值（如 10/100）
# {percentage}  百分比（如 10%）
# {elapsed}     已用时间（如 0:00:05）
# {remaining}   预计剩余时间
# {rate}        速率（如 5.0 it/s）
# {desc}        描述文本
for i in tqdm(
    range(10),
    bar_format="{desc}: {percentage:.0f}%|{bar:40}{r_bar}",
    desc="处理进度"
):
    time.sleep(0.1)
# 处理进度: 100%|████████████████████████████████████████| 100/100 [00:10<00:00,  9.94it/s]


# desc
# 动态更新描述
pbar = tqdm(range(10), desc="初始描述")
for i in pbar:
    pbar.set_description(f"正在处理第 {i} 项")
    time.sleep(0.1)
# 正在处理第 9 项: 100%|██████████| 100/100 [00:10<00:00,  9.93it/s]


# colour
# 支持的颜色：
# 预定义颜色：'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
# HEX颜色：'#00ff00'（需终端支持）
from colorama import init
init()  # 启用ANSI颜色支持


pbar = tqdm(range(10), desc="初始描述", colour="green")
for i in pbar:
    pbar.set_description(f"正在处理第 {i} 项")
    time.sleep(0.1)
# 正在处理第 9 项: 100%|██████████| 10/10 [00:01<00:00,  9.93it/s]


# ncols
# 一般是自适应
# 更改为 80
pbar = tqdm(range(10), desc="初始描述", colour="green", ncols=80)
for i in pbar:
    pbar.set_description(f"正在处理第 {i} 项")
    time.sleep(0.1)


# unit 和 unit_scale
# unit：设置单位（默认为 it，即 "iterations"）
# unit_scale：自动缩放单位（如 1000 → 1k）
pbar = tqdm(range(10), desc="初始描述", colour="green",
            ncols=80, unit="文件", unit_scale=True)
for i in pbar:
    pbar.set_description(f"正在处理第 {i} 项")
    time.sleep(0.1)
# 正在处理第 9 项: 100%|█████████████████████| 10.0/10.0 [00:01<00:00, 9.89文件/s]


# postfix
# 显示额外指标,用字典形式表示，但这个 key 只能为字符串
pbar = tqdm(range(100), postfix={"准确率": 0.0})
for i in pbar:
    # 用 set_postfix 更新右侧信息，注意不用加 ""
    pbar.set_postfix(准确率=i * 0.01)
    time.sleep(0.1)
# 100%|██████████| 100/100 [00:10<00:00,  9.92it/s, 准确率=0.99]


#################################################################################################
#################################################################################################