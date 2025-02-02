import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)
    try:
        driver.get('https://www.ctta.cn/')
        # 等待 'focus' div 可见
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'focus'))
        )
        focus_div = driver.find_element(By.ID, 'focus')
        # 在该 <div> 内找到所有的 <a> 标签
        links = focus_div.find_elements(By.TAG_NAME, 'a')
        articles_dict = {}  # 用于存储所有文章信息的字典，以URL为键
        for link in links:
            href = link.get_attribute('href')  # 获取 href 属性值
            if href:  # 确保 href 不为空
                # 找标题和图片信息
                img_tag = link.find_element(By.TAG_NAME, 'img') if link.find_elements(By.TAG_NAME, 'img') else None
                title_value = img_tag.get_attribute('title') if img_tag else "无标题"
                src_value = img_tag.get_attribute('src') if img_tag else "无图片"
                # 如果 URL 未在字典中，添加它
                if href not in articles_dict:
                    articles_dict[href] = {
                        'url': href,
                        'image_src': src_value,
                        'title': title_value,
                        'content': []  # 初始化内容列表
                    }
        # 打印所有唯一链接并抓取内容
        for article in articles_dict.values():
            # print(f"Fetching content from: {article['url']}")
            content = fetch_content(driver, article['url'])
            if content:
                article['content'] = content
        # 将字典转换为列表以保存为 JSON
        articles_list = list(articles_dict.values())
        # 保存为 JSON 文件
        switch_to_json(articles_list)
    finally:
        # 关闭浏览器
        driver.quit()

def fetch_content(driver, href):
    driver.get(href)
    # 等待页面中的 <p> 标签可见
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'p'))
    )
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    content = []
    for p in paragraphs:
        text = p.text
        if text:  # 只打印非空文本
            content.append(text)  # 将非空文本添加到内容列表中
    return content if content else None

def switch_to_json(articles):
    with open('focus.json', 'w', encoding='utf-8') as json_file:
        json.dump(articles, json_file, ensure_ascii=False, indent=4)
        print("Articles saved to focus.json")



