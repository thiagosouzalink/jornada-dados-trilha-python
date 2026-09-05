"""
Exercício 4 — Menu do Álbum

Desenvolva um programa que simule um álbum de figurinhas.

Utilize uma lista para armazenar as figurinhas e exiba o seguinte menu:

1 - Adicionar figurinha
2 - Remover figurinha
3 - Buscar figurinha
4 - Mostrar álbum
5 - Encerrar

O menu deve permanecer sendo exibido até que o usuário escolha a opção 5.

Regras:

Ao adicionar, a figurinha deve ser inserida no final da lista.
Ao remover, informe caso a figurinha não exista.
Na busca, informe se a figurinha está ou não no álbum.
Ao mostrar o álbum, exiba todas as figurinhas utilizando um for.

Desafio: utilize if, elif, else e while.
"""

figurinhas: list[str] = []
continuar: bool = True

mensagem_menu = """ ########## MENU ##########
1 - Adicionar figurinha
2 - Remover figurinha
3 - Buscar figurinha
4 - Mostrar álbum
5 - Encerrar

Informe a opção: """
while continuar:
    try:
        opcao = int(input(mensagem_menu))
        match opcao:
            case 1:
                figurinha = input("Digite a figurinha: ").strip().title()
                figurinhas.append(figurinha)
                print(f"Figurinha {figurinha} adicionada ao álbum.\n")

            case 2:
                figurinha = input("Digite a figurinha: ").strip().title()
                if figurinha not in figurinhas:
                    print(f"Figurinha {figurinha} não está presente no álbum.\n")
                else:
                    while figurinha in figurinhas:
                        figurinhas.remove(figurinha)
                    print(f"Figurinha {figurinha} removida do álbum.\n")
            case 3:
                figurinha = input("Digite a figurinha: ").strip().title()
                if figurinha in figurinhas:
                    print(f"Figurinha {figurinha} está presente no álbum.\n")
                else:
                    print(f"Figurinha {figurinha} não está presente no álbum.\n")
            case 4:
                if len(figurinhas) == 0:
                    print("Álbum está vazio.\n")
                else:
                    print("Figurinhas do álbum:")
                    for i in range(len(figurinhas)):
                        print(f"{i+1} - {figurinhas[i]}")
                    print()
            case 5:
                continuar = False
            case _:
                print("ERRO: Opção inválida.\n")
    except ValueError: 
        print("ERRO: Digite um número inteiro\n")