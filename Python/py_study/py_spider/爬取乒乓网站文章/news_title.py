import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = ori_driver()
    article_dict = {}
    articles_url = []
    try:
        articles_url = fetch_articles_url(driver)
        create_articles_dict(driver,articles_url,article_dict)
        article_list = list(article_dict.values())
        switch_to_json(article_list)
    finally:
        driver.close()

def ori_driver():
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)  # Keep the browser open after execution
    driver = webdriver.Edge(options=options)
    return driver

def fetch_articles_url(driver):
    urls = []
    driver.get('https://www.ctta.cn/')
    main_link_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='news title']"))
    )
    links = main_link_element.find_elements(By.TAG_NAME,'a')
    for link in links:
        url = link.get_attribute('href')
        if url not in urls:
            urls.append(url)
    return urls

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
    with open('news_title.json', 'w', encoding='utf-8') as json_file:
        json.dump(articles, json_file, ensure_ascii=False, indent=4)
        print("Articles saved to news_title.json")

