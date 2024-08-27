#pip install requests
#pip install bs4

import requests
from bs4 import BeautifulSoup

def search_incruit(kw, pg = 1):
    jobs = []
    for i in range(pg):
        pg = i * 30
        response = requests.get(f"https://search.incruit.com/list/search.asp?col=job&kw={kw}&startno={pg}")

        # print(response) #정상: 200

        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup)

        lis = soup.find_all("li", class_ = "c_col") #모두 찾기 #리스트 형태
        # print(lis)
        # print(len(lis))

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
            # print(link)

            job_data = {
                "title": context,
                "company": cpname,
                "location": location,
                "link": link
            }

            jobs.append(job_data)
        print(f"{i + 1}페이지 완료")

    return jobs


def search_jobkorea(kw, pg = 1):
    jobs = []
    for i in range(pg):

        pg = i + 1

        response = requests.get(f"https://www.jobkorea.co.kr/Search/?stext={kw}&tabType=recruit&Page_No={pg}")
        soup = BeautifulSoup(response.text, "html.parser")

        lis = soup.find_all("article", class_ = "list-item")

        for li in lis:
            try:
                title = li.find("div", class_ = "information-title").find("a").text.strip()
                company = li.find("div", class_ = "list-section-corp").find("a").text.strip()
                location = li.find_all("li", class_ = "chip-information-item")[3].text
                if location[0] == "D":
                    location = li.find_all("li", class_ = "chip-information-item")[2].text
                link = li.find("div", class_ = "information-title").find("a").get("href")

                job_data = {
                    "title": title,
                    "company": company,
                    "location": location,
                    "link": f"https://www.jobkorea.co.kr{link}"
                }

                jobs.append(job_data)
            except:
                pass
        print(f"{i + 1}페이지 완료")
    return jobs

# result = search_jobkorea("파이썬")
# print(result)

# result = search_incruit("파이썬", 10)
# print(result)
# print(len(result))

# result = search_jobkorea("회계", 10)
# print(result)
# print(len(result))

