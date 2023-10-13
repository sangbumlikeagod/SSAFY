import requests
from bs4 import BeautifulSoup

def crawling_basic():
    url = 'https://quotes.toscrape.com/tag/humor/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())
    # with open('soup.txt', 'w', encoding='utf-8') as file:
    #     file.write(soup.prettify())
    return soup
soup = crawling_basic()


title = soup.find('a')
print(f'제목 : {title.text}')
a_tags = soup.find_all('a')
# print(f'a 태그들 = {a_tags}')
for a_tag in a_tags:
    print(f'링크 : {a_tag}')
word = soup.select_one('.text')
print(f'첫 번째 글 = {word.text}')

words = soup.select('.text')

for w in words:
    print(f'글 : {w.text}')