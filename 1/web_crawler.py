import requests
from bs4 import BeautifulSoup
import os


MAIN_LINK = 'https://lyrsense.com/hitparad'
COUNT_PAGES = 100
INFO_FILE = 'index.txt'


def get_links(url):
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, features="lxml")
    links = []
    print(soup)
    for item in soup.select("a.songTitle.gotha.blackLink"):
        links.append(item['href'])
    return links


def remove_tags(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script', 'noscript', 'link']):
        data.decompose()
    return str(soup)


def crawl(url):
    page = requests.get(url)
    data = page.text
    return remove_tags(data)


if __name__ == '__main__':
    links_all = []
    i = 1
    info_string = ""
    print("start")

    links = get_links(MAIN_LINK)
    links_all += links
    print(i, len(links_all), MAIN_LINK)
    for i, link in enumerate(links_all):
        html_text = crawl("https://lyrsense.com" + link)
        print(i, link)
        filename = f'00{i}' if i < 10 else f'0{i}'
        info_string += f"{filename}\t{link}\n"
        path_result = f"Выкачка/{filename}.txt"
        os.makedirs(os.path.dirname(path_result), exist_ok=True)
        with open(path_result, "w", encoding="utf-8") as file_result:
            file_result.write(html_text)
    with open(INFO_FILE, "w", encoding="utf-8") as f:
        f.write(info_string)
