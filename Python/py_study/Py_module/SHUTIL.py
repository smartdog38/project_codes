#################################################################################################
"""

SHUTIL module
用于高级文件操作的模块
提供了对文件和目录的复制、移动、删除、压缩等操作的便捷接口

"""
#################################################################################################
"""

复制、移动、删除

"""
#################################################################################################

import shutil



# 文件的复制
# shutil.copy(src, dst)
# 将文件从 src 复制到 dst（可以是目录或新路径），可以重复复制
# 保留文件权限，但不保留元数据
# 将其复制到 os_folder2
shutil.copy(r"D:\code\Python\py_study\Py_module\data\shutil_test.txt",
            r"D:\code\Python\py_study\Py_module\data\os_folder_2\shutil_test.txt")


# shutil.copy2(src, dst)
# 类似 copy，但保留文件的元数据（如修改时间、权限等）
# 将其复制到 os_folder3
shutil.copy2(r"D:\code\Python\py_study\Py_module\data\shutil_test.txt",
            r"D:\code\Python\py_study\Py_module\data\os_folder_3\shutil_test.txt")


# 复制目录
# shutil.copytree(src, dst, symlinks=False, ignore=None, dirs_exist_ok=False)
# dirs_exist_ok=True（Python 3.8+）允许目标目录已存在
# ignore 可指定忽略的文件（如 shutil.ignore_patterns('*.tmp')）
# 将 os_folder_3, 复制到 os_folder_4 里
shutil.copytree(r"D:\code\Python\py_study\Py_module\data\os_folder_3",
                r"D:\code\Python\py_study\Py_module\data\os_folder_4",
                dirs_exist_ok=True)


# 文件与目录的移动
# 递归移动文件或目录（类似 mv 命令）
# 若 dst 存在且是目录，文件会被移动到该目录下。
# shutil.move(src, dst)
# 将 shutil_test_2.txt 文件移动到 os_folder_2 下
# shutil.move(r"D:\code\Python\py_study\Py_module\data\shutil_test_2",
#             r"D:\code\Python\py_study\Py_module\data\os_folder_2")

# 将 os_folder_3 移动到 os_folder_2 下
# shutil.move(r"D:\code\Python\py_study\Py_module\data\os_folder_3",
#             r"D:\code\Python\py_study\Py_module\data\os_folder_2")


# 删除目录
# shutil.rmtree(path, ignore_errors=False, onerror=None)
# shutil.rmtree(r"D:\code\Python\py_study\Py_module\data\os_folder_4")

#################################################################################################
#################################################################################################
