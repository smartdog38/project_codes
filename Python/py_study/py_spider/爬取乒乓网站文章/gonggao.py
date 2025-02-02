import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    #初始化driver
    driver=ori_driver()
    article_dict = {}
    plates_pages_url = {}
    plates_articles_url = {}
    plates_title = []
    plates_url = []
    try:
        #得到公告的更多的网址
        more_url = find_more_url(driver)
        #获取六个板块的初始网址
        plates_url = find_plates_url(driver,plates_url)
        #获取其板块名
        plates_title = find_plates_title(driver,plates_url)
        #找到每个板块每一页的网址
        plates_pages_url = find_plate_page_url(driver,plates_url,plates_title)
        #找到每个板块的文章的网址
        plates_articles_url = find_plates_article_url(driver,plates_pages_url)
        for plate in plates_articles_url.keys():
            for article_url in plates_articles_url[plate]:
                title = fetch_title(driver,article_url)
                content = fetch_content(driver,article_url)
                if title and content:
                    article_dict = create_dict_form(article_dict,plate,article_url,title,content)
        article_list=list(article_dict.values())
        switch_to_json(article_list)
    finally:
        driver.quit()


def switch_to_json(articles):
    with open('gonggao.json', 'w', encoding='utf-8') as json_file:
        json.dump(articles, json_file, ensure_ascii=False, indent=4)
        print("Articles saved to gonggao.json")

def fetch_title(driver,href):
    driver.get(href)
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'c_title'))
    )
    title = driver.find_element(By.CLASS_NAME,'c_title').text
    return title

def search_page_for_urls(driver, href):
    url_list=[]
    # 打开指定的网页
    driver.get(href)
    # 查找包含链接的 div（类名为 'c_body'）
    page_div = driver.find_element(By.CLASS_NAME, 'c_body')
    # 找到所有 <a> 标签
    links = page_div.find_elements(By.TAG_NAME, 'a')
    # 遍历每个链接
    for link in links:
        # 获取链接的 href 属性
        url = link.get_attribute('href')
        if url:
            url_list.append(url)
            # print(url)  # 打印链接
    return url_list

def fetch_content(driver, href):
    try:
        driver.get(href)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'p'))
        )
        paragraphs = driver.find_elements(By.TAG_NAME, 'p')
        content = []
        for p in paragraphs:
            text = p.text
            if text:  # Only add non-empty text
                content.append(text)
        return content if content else None
    except Exception as e:
        return None
#所有功能函数
def ori_driver():
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)  # Keep the browser open after execution
    driver = webdriver.Edge(options=options)
    return driver

def find_more_url(driver):
    driver.get('https://www.ctta.cn/')
    more_link_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@class="main_03_02"]/dl[@class="dbox"]/dt/span[@class="more"]/a'))
    )
    url = more_link_element.get_attribute('href')
    driver.get(url)
    return url

def find_plates_url(driver,more_url):
    plates_url = []
    for i in range(1, 7):
        second_dl_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'(//dl[@class="hbox"])[{i}]/dt/span[@class="more"]/a'))
        )
        href = second_dl_element.get_attribute('href')
        plates_url.append(href)
    return plates_url

def find_plates_title(driver,plates_url):
    plates_title = []
    for plate_url in plates_url:
        driver.get(plate_url)
        content_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="content"]/div[@class="c_nav"]'))
        )
        # 找到板块名
        plates_title.append(content_element.text.split('>')[2])
    # print(plates_title)
    return plates_title

def find_plate_page_url(driver,plates_url,plates_title):
    plate_pages_url = {}
    for plate_title in plates_title:
        plate_pages_url[plate_title] = []
    count = 0
    for plate_url in plates_url:
        driver.get(plate_url)
        if count == 4:
            plate_pages_url[plates_title[count]].append(plate_url)
            count = count+1
        else:
            select_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'sldd'))
            )
            option_elements = select_element.find_elements(By.TAG_NAME, 'option')
            values = [option.get_attribute('value') for option in option_elements]
            for value in values[:3]:
                page_url = plate_url+value
                plate_pages_url[plates_title[count]].append(page_url)
            count = count+1
    return plate_pages_url
    # print(plate_pages_url)

def find_plates_article_url(driver,plates_pages_url):
    plates_artcles_url = {}
    for plate in plates_pages_url.keys():
        plates_artcles_url[plate] = []
        # print(plate,plates_pages_url[plate])
        page_article_urls = []
        for page_url in plates_pages_url[plate]:
            page_article_urls = search_page_for_urls(driver,page_url)
            for url in page_article_urls:
                if url not in plates_artcles_url[plate]:
                    plates_artcles_url[plate].append(url)
    # print(plates_artcles_url)
    return plates_artcles_url


def create_dict_form(article_dict, plate, article_url, title, content):
    # 确保 plate 对应的列表存在
    if plate not in article_dict:
        article_dict[plate] = []
    # 将新的文章添加到对应 plate 的列表中
    article_dict[plate].append({
        'article_url': article_url,
        'title': title,
        'content': content
    })
    return article_dict
