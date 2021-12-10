# import ibge.constants as const
# import ibge.constants as const
import requests
import time
from bs4 import BeautifulSoup

FILTER_URL = "https://cnae.ibge.gov.br/?option=com_cnae&view=estrutura&Itemid=6160&ti%20po=cnae&versao_classe=7.0.0&versao_subclasse="
BASE_URL = "https://cnae.ibge.gov.br"

# r = requests.get(const.FILTER_URL)
r = requests.get(FILTER_URL)
html_main = BeautifulSoup(r.text, 'html.parser')
secao_links = html_main.table.find_all('a')
secao_links = [a.get('href') for a in secao_links]
secao_links = list(set(secao_links))
secao_links.sort()

def acess_site(site):
    for i in range(3):
        try:
            return requests.get(site)
        except:
            time.sleep(3)

# for link in secao_links:
#     requests.get(const.BASE_URL+link)
infos_table = []

for indice in range(0,3):
    # r = requests.get(const.BASE_URL+secao_links[indice])
    r = acess_site(BASE_URL+secao_links[indice])
    html_divisao = BeautifulSoup(r.text, 'html.parser')
    code_secao, name_secao = html_divisao.table.find_all(class_='destaque')
    code_secao, name_secao = code_secao.text.strip(), name_secao.text.strip()
    html_divisao_links = html_divisao.table.find_all('a')
    html_divisao_links = [a.get('href') for a in html_divisao_links]
    for divisao in html_divisao_links:
        # r = requests.get(const.BASE_URL+divisao)
        r = acess_site(BASE_URL+divisao)
        html_grupo = BeautifulSoup(r.text, 'html.parser')
        code_divisao, name_divisao = html_grupo.table.find(class_='destaque').text.split(' ',1)
        html_grupo_links = html_grupo.table.select("td[class='codigo n1'] a")
        html_grupo_links = [a.get('href') for a in html_grupo_links]
        for grupo in html_grupo_links:
            # r = requests.get(const.BASE_URL+divisao)
            r = acess_site(BASE_URL+grupo)
            html_classe = BeautifulSoup(r.text, 'html.parser')
            code_grupo, name_grupo = html_classe.table.find(class_='destaque').text.split(' ',1)
            html_classe_links = html_classe.table.select("td[class='codigo n2'] a")
            html_classe_links = [a.get('href') for a in html_classe_links]
            for classe in html_classe_links:
                # r = requests.get(const.BASE_URL+divisao)
                r = acess_site(BASE_URL+classe)
                html_subclasse = BeautifulSoup(r.text, 'html.parser')
                code_classe, name_classe = html_subclasse.table.find(class_='destaque').text.split(' ',1)
                html_subclasse_links = html_subclasse.table.select("td[class='codigo n3']")
                for subclasse in html_subclasse_links:
                    code_subclasse, name_subclasse = subclasse.text.strip().split(' ', 1)
                    infos_table.append([code_secao, name_secao, code_divisao, name_divisao, code_grupo, name_grupo, code_classe, name_classe, code_subclasse, name_subclasse])
                ...
            ...
        ...
    ...
...