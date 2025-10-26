from interface.classes.csv_class import CsvProcessor


arquivo_csv = "data/exemplo.csv"

csv1 = CsvProcessor(arquivo_csv)
csv1.carregar_csv()
print(csv1.filtrar_por(["estado", "preco"], ["SP", "10,50"]))

