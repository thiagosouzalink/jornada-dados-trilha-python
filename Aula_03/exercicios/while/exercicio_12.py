"""
13. Consumo de API Simulado
Objetivo: Simular o consumo de uma API paginada, onde cada "página" de 
dados é processada em loop até que não haja mais páginas.
"""
pagina_atual = 1
paginas_totais = 10

while pagina_atual <= paginas_totais:
    print(f"Página {pagina_atual} de {paginas_totais}")
    pagina_atual += 1

print("Todas as páginas foram processadas.")