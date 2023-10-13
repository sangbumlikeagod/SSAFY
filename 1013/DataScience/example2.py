import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_google_date(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    # 브라우저가 열릴 때 동적인 내용들이 모두 채워진다고?
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source

    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html, 'html.parser')

    with open('soup.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

get_google_date('칸예 웨스트')