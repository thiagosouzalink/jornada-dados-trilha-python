from copy import deepcopy
import utils


arquivo_csv = "arquivos/vendas.csv"
lista_dados = utils.ler_csv(arquivo_csv)
dict_processado = utils.processar_dados(lista_dados)
total_vendas_categoria = utils.calcular_vendas_por_categoria(dict_processado)