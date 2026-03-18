import requests
from bs4 import BeautifulSoup as bs

header_backend = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36",
}

header_frontend = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36",
}

def get_data_backend():
    a = requests.get("https://skillbox.ru/media/code/bekendrazrabotchik-kto-eto-chem-on-zanimaetsya-i-kak-im-stat/#stk-1", headers=header_backend)
    soup = bs(a.text, 'html.parser')
    item = soup.find_all('p', class_="stk-reset")
    info = []
    for i in item:
        if i.text.startswith("Бэкенд-разработчик"):
            info.append(
                {"text": f"{i.text}",}
            )
    return info

def get_data_frontend():
    a = requests.get("https://ru.hexlet.io/blog/posts/chto-takoe-frontend-razrabotka#heading-2-2", headers=header_frontend)
    soup = bs(a.text, 'html.parser')
    item = soup.find_all("p")
    info = []
    for i in item:
        if i.text.startswith("Когда мы открываем"):
            info.append(
                {"text": f"{i.text}",}
            )
    return info

