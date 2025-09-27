"""
Exercício 5: Detecção de Anomalias em Dados de Transações
Você está trabalhando em um sistema de detecção de fraude e precisa 
identificar transações suspeitas. Uma transação é considerada suspeita se 
o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial 
(antes das 9h ou depois das 18h). Dada uma transação como 
transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.
"""
transacao = {'valor': 12000, 'hora': 20}
# transacao = {'valor': 12000, 'hora': 10}
# transacao = {'valor': 5000, 'hora': 12}
# transacao = {'valor': 5000, 'hora': 7}
# transacao = {'valor': 5000, 'hora': 22}

valor_suspeito = transacao["valor"] > 10000
horario_suspeito = transacao["hora"] < 9 or transacao["hora"] > 18
if valor_suspeito or horario_suspeito:
    print(f"Transação suspeita: {transacao}")
else:
    print(f"Transição válida: {transacao}")