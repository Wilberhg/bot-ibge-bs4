import ibge.constants as const
from bs4 import BeautifulSoup
import requests
import time

class Ibge:
    def __init__(self):
        self._infos_table = []

    def get_infos_table(self):
        return self._infos_table

    def delete_duplicates(self, html_links):
        html_links = list(set(html_links))
        html_links = sorted(html_links)
        return html_links

    def access_link(self, url_filtered=const.FILTER_URL):
        for _ in range(3):
            try:
                return requests.get(const.BASE_URL+url_filtered)
            except:
                time.sleep(5)

    def parse_table(self, response):
        html_parsed = BeautifulSoup(response.text, 'html.parser')
        return html_parsed

    def get_titles(self, html_parsed, element=True):
        if element:
            html_titles = html_parsed.table.find_all(class_='destaque')
        else:
            html_titles = html_parsed
        if len(html_titles) == 2:
            code, name = [title.text.strip() for title in html_titles]
        else:
            code, name = html_titles[0].text.strip().split(' ',1)
        return code, name

    def get_links(self, html_parsed, element):
        html_links = html_parsed.table.select(element)
        if element.endswith('a'):
            html_links = [a.get('href') for a in html_links]
        return html_links

    def get_hierarquia(self, html_parsed):
        list_hierarquia = html_parsed.table.select('td[class*="codigo"]')
        list_hierarquia = [td.text.split(' ', 1) for td in list_hierarquia]
        list_hierarquia = sum(list_hierarquia, [])
        return list_hierarquia

    def create_list(self, code, name, list_hierarquia):
        list_hierarquia.insert(0, name)
        list_hierarquia.insert(0, code)
        self._infos_table.append(list_hierarquia)