from unidecode import unidecode
import pandas as pd
import re
import os

class TreatExcel:
    def __init__(self, excel_path=os.getcwd()+'\\files', excel_name='ExtractedIbge.xlsx'):
        self.excel_path = excel_path
        self.excel_name = excel_name
        self.df = pd.read_excel(self.excel_path+"\\"+self.excel_name)

    def lower_strings(self):
        self.df['Seção'] = self.df['Seção'].str.lower()
        self.df['Divisão'] = self.df['Divisão'].str.lower()
        self.df['Grupo'] = self.df['Grupo'].str.lower()
        self.df['Classe'] = self.df['Classe'].str.lower()
        self.df['Subclasse'] = self.df['Subclasse'].str.lower()

    def remove_accents(self):
        self.df['Seção'] = self.df['Seção'].apply(lambda x: unidecode(x))
        self.df['Divisão'] = self.df['Divisão'].apply(lambda x: unidecode(x))
        self.df['Grupo'] = self.df['Grupo'].apply(lambda x: unidecode(x))
        self.df['Classe'] = self.df['Classe'].apply(lambda x: unidecode(x))
        self.df['Subclasse'] = self.df['Subclasse'].apply(lambda x: unidecode(x))

    def remove_non_digits(self):
        self.df = self.df.astype({'Codigo Divisão': str, 'Codigo Grupo': str})
        self.df['Codigo Divisão'] = self.df['Codigo Divisão'].apply(lambda x: re.sub('\D', '', x))
        self.df['Codigo Grupo'] = self.df['Codigo Grupo'].apply(lambda x: re.sub('\D', '', x))
        self.df['Codigo Classe'] = self.df['Codigo Classe'].apply(lambda x: re.sub('\D', '', x))
        self.df['Codigo Subclasse'] = self.df['Codigo Subclasse'].apply(lambda x: re.sub('\D', '', x))

    def save_excel(self):
        self.df.to_excel(self.excel_path+"\\"+self.excel_name, index=False )

if __name__ == '__main__':

    obj = TreatExcel()
    obj.lower_strings()
    obj.remove_accents()
    obj.remove_non_digits()
    obj.save_excel()