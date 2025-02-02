import time
import focus
import news_title
import xinwen
import gonggao
import dongtai

#主程序
def main():
    print("欢迎来到爬取系统！！！")
    while True:
        print("请选择你要爬取的内容：\n1. 焦点\n2. 最新消息 \n3. 协会公告 \n4. 乒乓新闻 \n5. 协会动态")
        option=input()
        if option.lower() =="exit":
            break
        action(option)

def action(option):
    if option == "1":
        focus.main()
    elif option == "2":
        news_title.main()
    elif option == "3":
        gonggao.main()
    elif option == "4":
        xinwen.main()
    elif option == "5":
        dongtai.main()
    else:
        print("请重新输入正确的号码")

if __name__ == '__main__':
    main()