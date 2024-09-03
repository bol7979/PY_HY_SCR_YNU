from bs4 import BeautifulSoup
import requests



keyword = input("검색할 제품을 입력하세요 : ")

url = "https://search.shopping.naver.com/search/all?query={keyword}"

user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"

headers = {'User-Agent': user_agent}

req = requests.get(url, headers=headers)

html = req.text
# print(html[:1000]) 확인용
soup = BeautifulSoup(html, "html.parser")

base_divs = soup.select("[class^=product_item]")   # product_item 로 클래스 이름이 시작되는 클래스 

# print(base_divs)
print(len(base_divs))

for base_div in base_divs:
  title = base_div.select_one("[class^=product_link]")
  
  print(title.text)