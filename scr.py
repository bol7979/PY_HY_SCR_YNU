#pip install requests
#pip install bs4

import requests
from bs4 import BeautifulSoup

kw = "간호사"
response = requests.get(f"https://search.incruit.com/list/search.asp?col=job&kw={kw}&startno=0")

# print(response) #정상: 200

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

lis = soup.find_all("li", class_ = "c_col") #모두 찾기
# print(lis)
# print(len(lis))

jobs = []

for li in lis:
    # cpname = li.find("a", class_ = "cpname") #첫 하나 찾기
    cpname = li.find("a", class_ = "cpname").text #text: 내용 가져오기
    # print(cpname)
    context = li.find("div", class_ = "cell_mid").find("a").text
    # print(context)
    # location = li.find("div", class_ = "cl_md").find_all("span")
    # print(location)
    location = li.find("div", class_ = "cl_md").find_all("span")[2].text
    # print(location)
    # link = li.find("div", class_ = "cell_mid").find("a")
    # print(link)
    link = li.find("div", class_ = "cell_mid").find("a").get("href")
    print(link)

    job_data = {
        "tilte": context,
        "company": cpname,
        "location": location,
        "link": link
    }

    jobs.append(job_data)

print(jobs)