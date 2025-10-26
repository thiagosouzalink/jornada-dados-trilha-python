import pandas as pd


arquivo_csv = "data/exemplo.csv"
df = pd.read_csv(arquivo_csv)
df_filtrado = df[df["estado"] == "SP"]
print(df_filtrado)