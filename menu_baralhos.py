from banco_da_dados import adicionar_card, criar_baralho, listar_baralhos, listar_tabelas


def menu_baralhos():
    print("*------------------------*")
    listar_baralhos()
    while True:
        print("*-------------OPÇÃO------------*")
        print("1. Criar baralho")
        print("2. adicionar card")
        print("0. Retornar ao menu")
        res = int(input("Digite sua opção: "))

        if res == 1:
            criar_baralho()
        elif res == 2:
            tabela = listar_tabelas()
            adicionar_card(tabela)
        elif res == 0:
            break
        else:
            print("Opção inválida. Digite novamente.")
