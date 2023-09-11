from menu_baralhos import menu_baralhos


def menu_inicial():
    while True:
        print("------------- Clone Anki ------------")
        print("Menu :")
        print("Para escolher uma das opções, digite o número na frente dela:")
        print("1. Ver baralhos")
        print("2. Ver revisões")
        print("0. Para sair do Anki")
        res = int(input())

        if res == 0:
            break
        elif res == 1:
            menu_baralhos()


menu_inicial()
