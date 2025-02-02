# Git

## 一、初始化

### 1.数字签名

在想要进行Git管理的文件夹里，右键点开 `open git bash here` ，进入到Git的命令行界面，输入 `git global user.name aaa` 与 `git global user.email bbb@` 来进行数字签名

### 2.初始化

打开命令行

在所要进行git管理的目录里，进行 `git init`，就会将当前目录加入到git的管理下，当然，如果非空，最好设计一个git忽略文件 `.ignore` 放在用户的家目录下，来对不想进行管理的文件进行忽略

### 3.add 与 rm --cached

