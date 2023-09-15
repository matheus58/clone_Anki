from banco_da_dados import (
    adicionar_card,
    apagar_baralho_por_numero,
    criar_baralho,
    listar_baralhos,
    listar_tabelas,
    revisar_cartoes,
    tabelas_baralhos,
    verificar_tabela_baralhos,
)


def menu_baralhos():
    while True:
        print("*------------------------*")
        print("1. Criar baralho")
        print("2. Adicionar card")
        print("3. Listar baralhos")
        print("4. Apagar baralho")
        print("5. Revisar baralho")
        print("0. Retornar ao menu anterior")
        res = int(input("Digite sua opção: "))

        if res == 1:
            tabelas_baralhos()
            verificar_tabela_baralhos()
            criar_baralho()
        elif res == 2:
            tabela = listar_tabelas()
            adicionar_card(tabela)
        elif res == 3:
            listar_baralhos()
        elif res == 4:
            apagar_baralho_por_numero()
        elif res == 5:
            baralho = listar_baralhos()
            if baralho:
                print(baralho)
                revisar_cartoes(baralho[0])
        elif res == 0:
            break
        else:
            print("Opção inválida. Digite novamente.")
