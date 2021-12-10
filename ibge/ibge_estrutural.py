from selenium import webdriver
import time

def separate_words(list_texts):
    #['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA']
    #'A AGRICULTURA'
    if type(list_texts) == list:
        splitted_words = [element.text.strip() for element in list_texts]
        if len(splitted_words) == 1:
            splitted_words = splitted_words[0].split(' ', 1)
    else:
        splitted_words = list_texts
        splitted_words = list_texts.split(' ', 1)
    stripped_words = [word.strip() for word in splitted_words]
    return stripped_words

def code_value():
    return separate_words()[0]

def description_value():
    return separate_words()[-1]

def check_and_refresh(lista):
    ...

infos_table = list()

driver = webdriver.Chrome(r'C:\SeleniumDrivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://cnae.ibge.gov.br/?option=com_cnae&view=estrutura&Itemid=6160&ti%20po=cnae&versao_classe=7.0.0&versao_subclasse=')

# secao_elements = driver.find_elements_by_css_selector('table[id="tbEstrutura"] tr')
secao_elements = driver.find_elements_by_xpath('//a[contains(text(), "..")]')
secao_elements = [element.text.strip() for element in secao_elements]
for secao in range(0, 3):
    link_text = secao_elements[secao]
    driver.find_element_by_partial_link_text(link_text).click()
    driver.get(driver.current_url)
    secao_infos = driver.find_elements_by_css_selector('span[class="destaque"]')
    codigo_secao, nome_secao = separate_words(secao_infos)

    time.sleep(3)
    divisao_elements = driver.find_elements_by_css_selector('td[class="codigo"] a')
    divisao_elements = [element.text.strip() for element in divisao_elements]
    for divisao in divisao_elements:
        driver.find_element_by_xpath(f'//a[text()="{divisao}"]').click()
        driver.get(driver.current_url)
        divisao_infos = driver.find_elements_by_css_selector('span[class="destaque"]')
        codigo_divisao, nome_divisao = separate_words(divisao_infos)

        time.sleep(3)
        grupo_elements = driver.find_elements_by_css_selector('td[class="codigo n1"] a')
        grupo_elements = [element.text.strip() for element in grupo_elements]
        for grupo in grupo_elements:
            driver.find_element_by_xpath(f'//a[text()="{grupo}"]').click()
            driver.get(driver.current_url)
            grupo_infos = driver.find_elements_by_css_selector('span[class="destaque"]')
            codigo_grupo, nome_grupo = separate_words(grupo_infos)

            time.sleep(3)
            classe_elements = driver.find_elements_by_css_selector('td[class="codigo n2"] a')
            classe_elements = [element.text.strip() for element in classe_elements]
            for classe in classe_elements:
                driver.find_element_by_xpath(f'//a[text()="{classe}"]').click()
                driver.get(driver.current_url)
                classe_infos = driver.find_elements_by_css_selector('span[class="destaque"]')
                codigo_classe, nome_classe = separate_words(classe_infos)

                subclasse_elements = driver.find_elements_by_css_selector('td[class="codigo n3"]')
                # subclasse_elements = [element.text.strip() for element in subclasse_elements]
                for subclasse in subclasse_elements:
                    nome_subclasse = subclasse.text.split(' ', 1)
                    codigo_subclasse, nome_subclasse = [frase.strip() for frase in nome_subclasse]
                    infos_table.append([codigo_secao, nome_secao, codigo_divisao, nome_divisao, codigo_grupo, nome_grupo, codigo_classe, nome_classe, codigo_subclasse, nome_subclasse])

                driver.find_element_by_css_selector('td[class="codigo n1"] a').click()
                time.sleep(3)
            driver.find_element_by_css_selector('td[class="codigo"] a').click()
            time.sleep(3)
        driver.find_element_by_css_selector('table[class="tabela-hierarquia"] a').click()
        time.sleep(3)
    driver.get('https://cnae.ibge.gov.br/?option=com_cnae&view=estrutura&Itemid=6160&ti%20po=cnae&versao_classe=7.0.0&versao_subclasse=')
    ...