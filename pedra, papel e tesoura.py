#Importando bibliotecas

from time import sleep
import random

#Função enche linguiça

def maquina(falar):
    sleep(0.3)
    print('\n')
    print(falar)
    print('\n')

#Definindo uma lista

escolha = ["Pedra", "Papel", "Tesoura"]

while True:
    for p, e in enumerate(escolha):
        print(f"{p + 1}: {e}")
        
    try:
        resposta = int(input("\ndigite um numero das três opções acima: "))
            
        #Pegando a opção escolhida da resposta pela lista

        Pc = escolha[resposta - 1]

        #Computador faz a sua escolha

        b = random.choice(escolha)

        print("Prontos?")
        sleep(0.9)
        maquina("JO")
        maquina("KEN")
        sleep(0)
        maquina("PO!")

        #Exibindo as escolhas dos jogadores

        print(f"Computador: \033[0;36;40m{b}\033[m")
        print(f"Jogador: \033[0;36;40m{Pc}\033[m")
        sleep(2)

        #Funcionamento da escolha do vencedor

        if Pc == b:
            print("\033[0;33;40mEMPATE!\033[m")
        elif (Pc == "Papel" and b == "Tesoura") or (Pc == "Tesoura" and b == "Pedra") or (Pc == "Pedra" and b == "Papel"):
            print("\033[0;31;40mO computador vence!\033[m")
        else:
            print("\033[0;32;40mO jogador vence!\033[m")

    except IndexError:
        print("\033[0;31;40mdigite entre 1 ou 3 pls\033[m")
        continue

    except ValueError:
        print("\033[0;31;40mnao escreva letra pls\033[m")
        continue

    except Exception:
        print("\033[0;31;40mOq vc ta fazendo?!\033[m")

    print("\n")