"""
14. Tentativas de Conexão
Objetivo: Simular tentativas de reconexão a um serviço com um limite 
máximo de tentativas.
"""
tentativa = 1
maximo_tentativas = 3
while tentativa <= maximo_tentativas:
    print(f"Tentativa {tentativa} de {maximo_tentativas} tentativas")
print("Tentativas esgotadas.")