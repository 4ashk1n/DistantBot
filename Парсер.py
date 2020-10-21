import requests
from bs4 import BeautifulSoup
import lxml
import datetime


def get_html(url):
    r=requests.get(url)
    return r.text


def get_data(html):
    soup=BeautifulSoup(html, 'lxml')
##    people=soup.find('div', class_="sc-25l6fi-5")
    return soup

session = requests.Session()
headers = {'Referer': 'https://www.mos.ru/pgu/ru/application/dogm/journal/'}
auth_url = "https://login.mos.ru/sps/login/methods/password"
#471bc3aac0635c7a6a5a3dbcd8eb2e99
auth_req = session.get(auth_url, headers=headers, params={"login": "+79175965927", "password": "471bc3aac0635c7a6a5a3dbcd8eb2e99"}, allow_redirects=False)
print(1)
main_req = session.get("https://dnevnik.mos.ru/diary/diary/lessons")
print(BeautifulSoup(main_req.text,'lxml').find("div",id='root').next)