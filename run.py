from ibge.ibge import Ibge
from excel.create_excel import CreateExcel
from excel.treat_excel import TreatExcel
from ibge.utilities import Utilities

try:
    bot = Ibge()
    response_secao = bot.access_link()
    html_secao = bot.parse_table(response=response_secao)
    links_secao = bot.get_links(html_parsed=html_secao, element='a')
    links_secao = bot.delete_duplicates(links_secao)
    for indice in range(0,3):
        response_divisao = bot.access_link(url_filtered=links_secao[indice])
        html_divisao = bot.parse_table(response=response_divisao)
        code_secao, name_secao = bot.get_titles(html_divisao)
        links_divisao = bot.get_links(html_parsed=html_divisao, element='a')
        for divisao in links_divisao:
            response_grupo = bot.access_link(url_filtered=divisao)
            html_grupo = bot.parse_table(response=response_grupo)
            links_grupo = bot.get_links(html_parsed=html_grupo, element="td[class='codigo n1'] a")
            for grupo in links_grupo:
                response_classe = bot.access_link(url_filtered=grupo)
                html_classe = bot.parse_table(response=response_classe)
                links_classe = bot.get_links(html_parsed=html_classe, element="td[class='codigo n2'] a")
                for classe in links_classe:
                    response_subclasse = bot.access_link(url_filtered=classe)
                    html_subclasse = bot.parse_table(response=response_subclasse)
                    links_subclasse = bot.get_links(html_parsed=html_subclasse, element="td[class='codigo n3'] a")
                    for subclasse in links_subclasse:
                        response_subclasse = bot.access_link(url_filtered=subclasse)
                        html_subclasse = bot.parse_table(response=response_subclasse)
                        list_hierarquia = bot.get_hierarquia(html_parsed=html_subclasse)
                        bot.create_list(code=code_secao, name=name_secao, list_hierarquia=list_hierarquia)
    ibge_results = bot.get_infos_table()

    c_excel =  CreateExcel()
    c_excel.set_sheet_name()
    c_excel.set_headers()
    c_excel.write_lines(ibge_results)
    c_excel.save_excel()

    t_excel = TreatExcel()
    t_excel.lower_strings()
    t_excel.remove_accents()
    t_excel.remove_non_digits()
    t_excel.save_excel()
except BaseException as e:
    Utilities().register_log(e)