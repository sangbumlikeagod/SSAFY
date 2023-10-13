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
    # 1. div 태그 중 g 클래스를 가진 모든 요소 선택
    g_list = soup.select("div.g")
    
    for result in g_list:
        # print(result.text)
        title = result.select_one(".LC20lb.MBeuO.DKV0Md")
        print(f'제목 = {title.text}')
get_google_date('칸예 웨스트')