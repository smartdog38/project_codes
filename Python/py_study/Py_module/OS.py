#################################################################################################
#################################################################################################
"""

OS 模块
os 模块是处理操作系统相关功能的核心库
涵盖了文件/目录操作、路径管理、环境变量、进程管理

"""
from site import abs_paths

#################################################################################################
"""

路径判断

"""
#################################################################################################

# 正确返回 True，错误返回 False
# os.path.exists(path) #判断文件是否存在
# os.path.isdir(path) #判断是否是目录
# os.path.isfile(path) #判断是否是文件
# os.path.islink(path) #判断是否是链接
# os.path.isabs(path) #判断是否是绝对路径
# os.path.ismount(path) #判断是否是挂载点
import os

print(os.path.exists(r"D:\code\Python\py_study\Py_module\OS.py"),
      os.path.isdir(r"D:\code\Python\py_study\Py_module\OS.py"),
      os.path.isfile(r"D:\code\Python\py_study\Py_module\OS.py"),
      os.path.islink(r"D:\code\Python\py_study\Py_module\OS.py"),
      os.path.isabs(r"D:\code\Python\py_study\Py_module\OS.py"),
      os.path.ismount(r"D:\code\Python\py_study\Py_module\OS.py"))
# True False True False True False

#################################################################################################
"""

操作路径

"""
#################################################################################################

# os.path.join(path1, path2) #连接路径
# os.path.split(path) #分离路径
# os.path.splitext(path) #分离文件名和扩展名
# os.path.splitdrive(path) #分离磁盘
# os.path.normpath(path) #规范化路径
import os


# 连接
print(os.path.join(r"C:\aa\bb",r"dd\ff")) # C:\aa\bb\dd\ff


# 分离，将最后一个字段与前面的分开构成元组
path_tuple  = os.path.split(r"C:\aa\bb\dd\ff")
print(type(path_tuple)) # <class 'tuple'>
print(path_tuple[0]) # C:\aa\bb\dd
print(path_tuple[1]) # ff


# 分离文件名与拓展名
path_tuple_2  = os.path.splitext(r"C:\aa\bb\dd\ff.img")
print(type(path_tuple_2)) # <class 'tuple'>
print(path_tuple_2[0]) # C:\aa\bb\dd\ff
print(path_tuple_2[1]) # img


# 分离磁盘即最开始的字段
path_tuple_3 = os.path.splitdrive(r"C:\aa\bb\dd\ff.img")
print(type(path_tuple_3)) # <class 'tuple'>
print(path_tuple_3[0]) # C:
print(path_tuple_3[1]) # \aa\bb\dd\ff.img

# 将路径规范化
# 将路径中的多余分隔符（如 // 或 \\）替换为单个分隔符
# 将路径中的 .（当前目录）和 ..（父目录）解析为实际路径
# 根据操作系统的默认路径分隔符，将路径中的分隔符统一(Linux 为 /, Windows 为 \)
path_normal = os.path.normpath(r"C://///aaa\\\\\b///c\\d.txt") # C:\aaa\b\c\d.txt
print(path_normal)

#################################################################################################
"""

获取路径信息

"""
#################################################################################################

# os.path.basename(path) #获取文件名
# os.path.dirname(path) #获取目录
# os.path.getsize(path) #获取文件大小
# os.path.getatime(path) #获取文件最后访问时间
# os.path.getmtime(path) #获取文件最后修改时间
# os.path.getctime(path) #获取文件创建时间
# os.path.abspath(path) #获取绝对路径
# os.path.expanduser(path) #获取用户路径
# os.path.expandvars(path) #获取环境变量
import os


#
basename = os.path.basename(r"D:\code\Python\py_study\Py_module\data\os_test.txt")
dirname = os.path.dirname(r"D:\code\Python\py_study\Py_module\data\os_test.txt")
file_size = os.path.getsize(r"D:\code\Python\py_study\Py_module\data\os_test.txt")
access_time = os.path.getatime(r"D:\code\Python\py_study\Py_module\data\os_test.txt")
modifeid_time = os.path.getmtime(r"D:\code\Python\py_study\Py_module\data\os_test.txt")
create_time = os.path.getctime(r"D:\code\Python\py_study\Py_module\data\os_test.txt")
abs_path = os.path.abspath(r"D:\code\Python\py_study\Py_module\data\os_test.txt")

print(basename, dirname, file_size, access_time, modifeid_time, create_time, abs_path)
# os_test.txt
# D:\code\Python\py_study\Py_module\data
# 0
# 1741430667.548577 1741430667.548577 1741430667.548577  这个是以 1970年1月1日来计算秒的
# D:\code\Python\py_study\Py_module\data\os_test.txt

#################################################################################################
"""

对目录的操作

"""
#################################################################################################

# os.mkdir(folder_path) # 创建文件夹，如果文件夹已存在，则报错
# os.makedirs(folder_path) # 递归创建文件夹
# os.rmdir(folder_path) # 删除空文件夹
# os.listdir(folder_path) # 获取文件夹下的文件，返回名称列表
# os.walk(folder_path) # 递归遍历所有子目录
# os.scandir(folder_path) # 快速遍历（非递归）
# os.rename("old_folder", "new_folder") # 重命名或移动目录


# os.mkdir(folder_path)
# 一般的创建文件夹的方式
if not os.path.exists(r"D:\code\Python\py_study\Py_module\data\os_folder"):
      os.mkdir(r"D:\code\Python\py_study\Py_module\data\os_folder")
# 可以看见已经创建了，在运行一遍虽然不报错，但是也不会生成另一个目录了


# os.makedirs(folder_path)
if not os.path.exists(r"D:\code\Python\py_study\Py_module\data\os_folder_2\os_subfolder"):
      os.makedirs(r"D:\code\Python\py_study\Py_module\data\os_folder_2\os_subfolder")
# 可以看见生成了一个父目录与一个子目录


# os.rmdir(folder_path
# 每次对文件夹进行操作前进行检查
if os.path.exists(r"D:\code\Python\py_study\Py_module\data\os_folder"):
      os.rmdir(r"D:\code\Python\py_study\Py_module\data\os_folder")
# 发现文件夹没了


# os.listdir(folder_path)
if os.path.exists(r"D:\code\Python\py_study\Py_module"):
      py_modulde_list = os.listdir(r"D:\code\Python\py_study\Py_module")
      # 将里面所有的文件与文件夹打印出来，注意子目录不会扫描
      for file in py_modulde_list:
            print(file)


# os.walk(folder_path) (递归)
for root, dirs, files in os.walk(r"D:\code\Python\py_study\Py_module"):
    print(f"当前目录: {root}")
    print(f"子目录列表: {dirs}")
    print(f"文件列表: {files}")
    print("------")
# 每一个目录都会记录一次
# 当前目录: D:\code\Python\py_study\Py_module
# 子目录列表: ['data']
# 文件列表: ['AIOHTTP.py', 'AIOMYSQL.py', 'ASYNCIO.py', 'BEAUTIFULSOUP.py', 'CSV.py', 'DATETIME.py', 'DJANGO.py', 'FAKE-USERAGENT.py', 'FASTAPI.py', 'FLASK.py', 'HTTPX.py', 'JSON.py', 'LXML.py', 'MATPLOTLIB.py', 'MYSQL-CONNECTOR-PYTHON.py', 'MYSQLCLIENT.py', 'NUMPY.py', 'OPENYXL.py', 'OS.py', 'PANDAS.py', 'PROXYPOOL.py', 'PYMYSQL.py', 'RE.py', 'REQUESTS-HTML.py', 'REQUESTS.py', 'SCRAPY.py', 'SEABORN.py', 'SELENIUM.py', 'SHUTIL.py', 'SOCKET.py', 'SQLALCHEMY.py', 'SYS.py', 'THREADING.py', 'TQDM.py', 'XLWINGS.py']
# ------
# 当前目录: D:\code\Python\py_study\Py_module\data
# 子目录列表: ['os_folder_2']
# 文件列表: ['os_test.txt']
# ------
# 当前目录: D:\code\Python\py_study\Py_module\data\os_folder_2
# 子目录列表: ['os_subfolder']
# 文件列表: []
# ------
# 当前目录: D:\code\Python\py_study\Py_module\data\os_folder_2\os_subfolder
# 子目录列表: []
# 文件列表: []
# ------


# os.scandir(folder_path)
with os.scandir(r"D:\code\Python\py_study\Py_module") as entries:
    for entry in entries:
        if entry.is_dir():
            print(f"目录: {entry.name}")
        elif entry.is_file():
            print(f"文件: {entry.name}")
# 只会查看第一层的文件内容，不会递归
# 但使用 os.scandir 性能更高，返回对象


# os.rename("old_folder", "new_folder")
if os.path.exists(r"D:\code\Python\py_study\Py_module\data\os_folder_2"):
    if not os.path.exists(r"D:\code\Python\py_study\Py_module\data\os_folder_3"):
        os.rename(r"D:\code\Python\py_study\Py_module\data\os_folder_2",
                  r"D:\code\Python\py_study\Py_module\data\os_folder_3")
# 可以看到变为了os_folder_3

#################################################################################################
"""

对文件的操作

"""
#################################################################################################

# os.remove(path) #删除文件
# os.rename(old, new) #重命名文件,不会创造中间目录
# os.truncate(path, size) #截断文件
# os.stat(path) #获取文件信息
import os


# 文件的创建
# 没有特有的方法
# 但是当我们可以通过 open() 函数以写入模式打开文件来创建文件
if not os.path.exists(r"D:\code\Python\py_study\Py_module\data\os_newfile.txt"):
    with open(r"D:\code\Python\py_study\Py_module\data\os_newfile.txt", "w") as file:
        print("新文件已创建")


# os.stat(path)
if os.path.exists(r"D:\code\Python\py_study\Py_module\data\os_newfile.txt"):
    print(os.stat(r"D:\code\Python\py_study\Py_module\data\os_newfile.txt"))
    # os.stat_result(st_mode=33206, st_ino=22517998136878415, st_dev=17334588300867143118,
    # st_nlink=1, st_uid=0, st_gid=0,
    # st_size=0, st_atime=1741457513, st_mtime=1741457513, st_ctime=1741457513)


# os.rename(old, new)
if os.path.exists(r"D:\code\Python\py_study\Py_module\data\os_newfile.txt"):
    if not os.path.exists(r"D:\code\Python\py_study\Py_module\data\os_newfile2.txt"):
        os.rename(r"D:\code\Python\py_study\Py_module\data\os_newfile.txt",
                  r"D:\code\Python\py_study\Py_module\data\os_newfile2.txt")


# os.truncate(payh, size)
if os.path.exists(r"D:\code\Python\py_study\Py_module\data\os_newfile2.txt"):
    os.truncate(r"D:\code\Python\py_study\Py_module\data\os_newfile2.txt", 60)

# os.remove(path)
if os.path.exists(r"D:\code\Python\py_study\Py_module\data\os_newfile.txt"):
    os.remove(r"D:\code\Python\py_study\Py_module\data\os_newfile.txt")
    print("文件已删除")

#################################################################################################
#################################################################################################