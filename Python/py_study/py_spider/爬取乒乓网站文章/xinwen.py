import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = ori_driver()
    article_dict = {}
    pages_url = []
    articles_url = []
    try:
        # 获取主页面 URL
        url = fetch_main_url(driver)
        # 获取分页 URL
        pages_url = fetch_pages_url(driver, url, pages_url)
        # 在每个分页链接中查找文章链接
        articles_url = search_page_for_urls(driver, pages_url)
        # 获取每篇文章的标题和内容
        article_dict = create_articles_dict(driver, articles_url, article_dict)
        # 将文章数据保存到 JSON 文件
        article_list = list(article_dict.values())
        switch_to_json(article_list)
    finally:
        driver.quit()  # 确保结束时关闭浏览器

def ori_driver():
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)  # 保持浏览器打开
    driver = webdriver.Edge(options=options)
    return driver

def fetch_main_url(driver):
    driver.get('https://www.ctta.cn/')
    try:
        main_link_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[text()='乒乓新闻']"))
        )
        url = main_link_element.get_attribute('href')
        driver.get(url)
        return url
    except Exception as e:
        print(f"Error fetching main URL: {e}")
        return None

def fetch_pages_url(driver, url, pages_url):
    try:
        driver.get(url)
        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'sldd'))
        )
        option_elements = select_element.find_elements(By.TAG_NAME, 'option')
        values = [option.get_attribute('value') for option in option_elements]
        for value in values[:3]:  # 获取前三个分页链接
            page_url = url + value
            pages_url.append(page_url)
        return pages_url
    except Exception as e:
        print(f"Error fetching pages URL: {e}")
        return pages_url

def search_page_for_urls(driver, pages_url):
    url_list = []
    for page_url in pages_url:
        driver.get(page_url)
        try:
            page_div = driver.find_element(By.CLASS_NAME, 'c_body')
            links = page_div.find_elements(By.TAG_NAME, 'a')
            for link in links:
                url = link.get_attribute('href')
                if url:
                    url_list.append(url)
        except Exception as e:
            print(f"Error fetching links on page {page_url}: {e}")
    return url_list

def fetch_content(driver, href):
    try:
        driver.get(href)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'p'))
        )
        paragraphs = driver.find_elements(By.TAG_NAME, 'p')
        content = [p.text for p in paragraphs if p.text]
        return content if content else None
    except Exception as e:
        return None

def fetch_title(driver, href):
    try:
        driver.get(href)
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'c_title'))
        )
        title = driver.find_element(By.CLASS_NAME, 'c_title').text
        return title
    except Exception as e:
        print(f"Error fetching title for {href}: {e}")
        return None

def create_articles_dict(driver, articles_url, article_dict):
    for article_url in articles_url:
        title = fetch_title(driver, article_url)
        content = fetch_content(driver, article_url)
        if title and content:
            article_dict[title] = {
                'url': article_url,
                'title': title,
                'content': content
            }
    return article_dict

def switch_to_json(articles):
    with open('xinwen.json', 'w', encoding='utf-8') as json_file:
        json.dump(articles, json_file, ensure_ascii=False, indent=4)
        print("Articles saved to xinwen.json")