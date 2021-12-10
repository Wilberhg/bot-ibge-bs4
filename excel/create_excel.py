from xlsxwriter import Workbook
import os

class CreateExcel:
    def __init__(self, excel_path=os.getcwd()+'\\files', excel_name='ExtractedIbge.xlsx'):
        self.excel_path = excel_path
        self.excel_name = excel_name
        os.makedirs(self.excel_path, exist_ok=True)
        self.wb = Workbook(self.excel_path+"\\"+self.excel_name)

    def set_sheet_name(self):
        self.ws = self.wb.add_worksheet('Ibge')

    def set_headers(self):
        bold = self.wb.add_format({'bold': 1})
        self.ws.write_string('A1', 'Codigo Seção', bold)
        self.ws.write_string('B1', 'Seção', bold)
        self.ws.write_string('C1', 'Codigo Divisão', bold)
        self.ws.write_string('D1', 'Divisão', bold)
        self.ws.write_string('E1', 'Codigo Grupo', bold)
        self.ws.write_string('F1', 'Grupo', bold)
        self.ws.write_string('G1', 'Codigo Classe', bold)
        self.ws.write_string('H1', 'Classe', bold)
        self.ws.write_string('I1', 'Codigo Subclasse', bold)
        self.ws.write_string('J1', 'Subclasse', bold)

    def write_lines(self, table_datas):
        row = 1
        col = 0

        for cod_secao, secao, cod_divisao, divisao, cod_grupo, grupo, cod_classe, classe, cod_subclasse, subclasse in table_datas:
            self.ws.write_string(row, col, cod_secao)
            self.ws.write_string(row, col+1, secao)
            self.ws.write_string(row, col+2, cod_divisao)
            self.ws.write_string(row, col+3, divisao)
            self.ws.write_string(row, col+4, cod_grupo)
            self.ws.write_string(row, col+5, grupo)
            self.ws.write_string(row, col+6, cod_classe)
            self.ws.write_string(row, col+7, classe)
            self.ws.write_string(row, col+8, cod_subclasse)
            self.ws.write_string(row, col+9, subclasse)
            row += 1

    def save_excel(self):
        self.wb.close()
            
if __name__ == '__main__':
    list_datas = [
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.54-7', 'Criação de suínos', '0154-7/00', 'Criação de suínos'],
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.55-5', 'Criação de aves', '0155-5/01', 'Criação de frangos para corte'],
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.55-5', 'Criação de aves', '0155-5/02', 'Produção de pintos de um dia'],
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.55-5', 'Criação de aves', '0155-5/03', 'Criação de outros ga...para corte'],
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.55-5', 'Criação de aves', '0155-5/04', 'Criação de aves, exc...galináceos'],
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.55-5', 'Criação de aves', '0155-5/05', 'Produção de ovos']
        ]

    obj =  CreateExcel()
    obj.set_sheet_name()
    obj.set_headers()
    obj.write_lines(list_datas)
    obj.save_excel()
    ...