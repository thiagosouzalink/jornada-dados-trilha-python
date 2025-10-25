import pandas as pd


class ProcessadorCSV:
    def __init__(self, arquivo_csv: str):
        self.arquivo_csv = arquivo_csv
        self.df = None
    
    def carregar_csv(self):
        self.df = pd.read_csv(self.arquivo_csv)
    
    def remover_celulas_vazias(self):
        self.df = self.df.dropna()
    
    def filtrar_por_estado(self, estado: str):
        self.df = self.df[self.df["estado"] == estado]
    
    def processar(self, estado: str) -> pd.DataFrame:
        self.carregar_csv()
        self.remover_celulas_vazias()
        self.filtrar_por_estado(estado)
        
        return self.df


arquivo_csv = "01-basico/datas/exemplo.csv"  
estado_filtrado = "SP"

processador = ProcessadorCSV(arquivo_csv)
df_filtrado = processador.processar(estado_filtrado)

print(df_filtrado)