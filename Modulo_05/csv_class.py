from pathlib import Path
from typing import Any
import pandas as pd


class CsvProcessor:
    def __init__(self, file_path: Path | str):
        self.file_path = file_path
        self.df = None
        
    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df
        
    def filtrar_por(self, coluna: str, atributo: Any) -> pd.DataFrame:
        self.df_filtrado = self.df[self.df[coluna]==atributo]
        return self.df_filtrado

    def sub_filtro(self, coluna, atributo):
        return self.df_filtrado[self.df[coluna] == atributo]


data_folder = Path(__file__).parent / "data"
exemplo_file = data_folder / "exemplo.csv"
coluna = "estado"
estado = "SP"

arquivo_csv = CsvProcessor(exemplo_file)
arquivo_csv.carregar_csv()
print(arquivo_csv.filtrar_por(coluna, estado))