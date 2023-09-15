 import datatime 

 def calcular_proximo_intervalo(nivel, ultima_revisao):
     if nivel == 1 :
         return 1
     elif nivel == 2:
         return 6
     else:
         return calcular_proximo_intervalo(nivel -1, ultima_revisao) * 2

def mostrar_cartao(cartao):
    # mostra o cartao front 
    print()
 
    # mostra o cartao front # mostra o cartao front 
