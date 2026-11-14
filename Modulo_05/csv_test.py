from pathlib import Path
import pandas as pd
from interface.classes.csv_class import CsvProcessor


data_folder = Path(__file__).parent / "data"
exemplo_file = data_folder / "exemplo.csv"
coluna = "estado"
estado = "SP"

arquivo_csv = CsvProcessor(exemplo_file)
arquivo_csv.carregar_csv()
# print(arquivo_csv.filtrar_por(coluna, estado))
print(arquivo_csv.filtrar_por(["estado", "preco"], ["sp", "10,50"]))