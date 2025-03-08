#对路径的操作
# os.path.exists(path) #判断文件是否存在
# os.path.isdir(path) #判断是否是目录
# os.path.isfile(path) #判断是否是文件
# os.path.islink(path) #判断是否是链接
# os.path.isabs(path) #判断是否是绝对路径
# os.path.ismount(path) #判断是否是挂载点


# os.path.join(path1, path2) #连接路径
# os.path.split(path) #分离路径
# os.path.splitext(path) #分离文件名和扩展名
# os.path.splitdrive(path) #分离磁盘
# os.path.normpath(path) #规范化路径


# os.path.basename(path) #获取文件名
# os.path.dirname(path) #获取目录
# os.path.getsize(path) #获取文件大小
# os.path.getatime(path) #获取文件最后访问时间
# os.path.getmtime(path) #获取文件最后修改时间
# os.path.getctime(path) #获取文件创建时间
# os.path.abspath(path) #获取绝对路径
# os.path.realpath(path) #获取绝对路径
# os.path.expanduser(path) #获取用户路径
# os.path.expandvars(path) #获取环境变量



# #对文件夹的操作
# os.mkdir(path) #创建文件夹，如果文件夹已存在，则报错
# os.rmdir(path) #删除文件夹，如果文件夹不为空，则报错
# os.listdir(path) #获取文件夹下的文件
# os.removedirs(path) #删除文件夹
# os.walk(path) #遍历文件夹

# #对文件的操作
# os.utime(path, times) #修改文件时间
# os.remove(path) #删除文件
# os.rename(old, new) #重命名文件,不会创造中间目录
# os.truncate(path, size) #截断文件
# os.replace(src, dst) #替换文件
# os.stat(path) #获取文件信息

# os.chdir(path) #改变当前路径
# os.getcwd() #获取当前路径
# os.chmod(path, mode) #修改文件权限
# os.chown(path, uid, gid) #修改文件所有者


# import os
# print(help(os))
# print(dir(os))