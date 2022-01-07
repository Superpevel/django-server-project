from os import link
from bs4 import BeautifulSoup
import requests
import random
from core.models import Film

user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]


def get_film():
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    
    x = 1

    url = "http://ac-online.lordfilms-s.art/filmy/"
    
    source = "http://ac-online.lordfilms-s.art/"

    while True:
        i = 0
        page = BeautifulSoup(requests.get(url,headers=headers).text, "lxml")


        name_list = []
        god_list = []
        link1_list = []
        opisanie_list = []


        for name in page.find_all("div", class_="th-title"):
            name_text = name.text
            print(name_text)
            name_list.append(name_text)

        for god in page.find_all("div", class_="th-year"):
            god_text = god.text
            print(god_text)
            god_list.append(god_text)

        for film in page.find_all("div", class_="th-item"):
            Link_STR = film.find("a", class_="th-in with-mask").get('href')
            print(Link_STR)
            link1_list.append(Link_STR)


        for link0 in link1_list:

            page2 = BeautifulSoup(requests.get(link0,headers=headers).text, "lxml")

            opisanie = page2.find("div", class_="fdesc clearfix slice-this").text


            b_split_list = opisanie.split("						")
            b1 = b_split_list[-1]
            print(b1)


            opisanie_list.append(b1)


        while i < len(opisanie_list):
            name1 = name_list[i]
            god1 = god_list[i]
            opisanie1 = opisanie_list[i]
            link2 = link1_list[i]
            print(f'{name1} {god1} {link2} ')
            film = Film.objects.get_or_create(name=name1,sourse=source,link=link2,desciption=opisanie1,year=god1)

            i = i + 1

        x = x + 1

        url = "http://ac-online.lordfilms-s.art/filmy/page/" + str(x) + "/"

        if x == 3:
            print('hello')
            return (0)

