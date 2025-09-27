"""
Exercício 4: Validação de Dados de Entrada
Antes de processar os dados de usuários em um sistema de recomendação, 
você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e 
tenha fornecido um email válido. Escreva um programa que valide essas 
condições e imprima "Dados de usuário válidos" ou o erro específico 
encontrado.
"""
try:
    idade = int(input("Idade: "))
    email = input("Email: ").strip()

    if 18 <= idade <= 65:
        if "@" not in email:
            print("Email deve ter um caracter '@'")
        else:
            email_lista = email.split("@")
            if not len(email_lista) == 2:
                print("Email deve ter apenas 1 simbolo '@'")
            elif not email_lista[0]:
                print("Email deve ter um username")
            elif not email_lista[1]:
                print("Email deve ter provedor e dominio")
            else:
                provedor_dominio = email_lista[1].split(".")
                if len(provedor_dominio) == 1:
                    print("Email deve ter provedor e dominio")
                elif not provedor_dominio[0] or not provedor_dominio[1]:
                    print("Email deve ter provedor e dominio")
                else:
                    print("Dados de usuário válidos")
    else:
        print("Idade inválida.")
except ValueError:
    print("Erro na entrada de valores.")
    
        