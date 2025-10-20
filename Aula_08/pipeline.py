from etl import pipeline_calcular_kpi_de_vendas_consolidado


pasta_entrada = "data/raw/"
pasta_saida = "data/processed"
formato_saida = ["CSV", "parquet"]

pipeline_calcular_kpi_de_vendas_consolidado(
    pasta_entrada=pasta_entrada,
    pasta_saida=pasta_saida,
    formato_saida=formato_saida
)