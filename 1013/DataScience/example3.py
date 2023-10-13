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

    # with open('soup.txt', 'w', encoding='utf-8') as file:
    #     file.write(soup.prettify())

    result_stats = soup.select_one("div#result-stats")
    print(result_stats, type(result_stats))
    results = soup.select("div.LC20lb")

    for result in results:
        print(result.text)
    # 그냥으로는 html객체를 그대로 가져온다, .text를 사용해야함 
get_google_date('칸예 웨스트')