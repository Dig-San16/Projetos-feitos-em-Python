#Importando bibliotecas
from time import sleep 
import random

#Corpo da forca
def boneco(errors):
    stages = [
        "_\n |\n O\n",
        "_\n |\n O\n |\n",
        "_\n |\n O\n/|\n",
        "_\n |\n O\n/|\\\n",
        "_\n |\n O\n/|\\\n/ \n",
        "_\n |\n O\n/|\\\n/ \\\n"
    ]
    print(stages[errors])
    print("\n")

#Título
print("/" * 30)
print("\033[0;33;40m        JOGO DA FORCA       \033[m")
print("/" * 30)
print("\n")

#Repetição "Pai de todos"
while True:
    #Código que pode ocorrer uma exceção
    try: 
        modo = int(input("digite 1 se for jogar com alguém ou 2 se for jogar só com o computador: "))
        if modo not in (1,2):
            print("\033[0;31;40mDigite entre 1 ou 2 pfvr\033[m")
            print("\n")
            continue

    #Lidando com a exceção
    except ValueError:
        print("\033[0;31;40mnão aceito caracteres mano\033[m")
        print("\n")
        continue

    #Condição caso o jogador escolha 1
    if modo == 1:
        sleep(3)
        print("vc escolheu jogar com alguém")
        sleep(3)
        print("\n")

        #Palavra a ser escrita para depois ser adinhada
        palavra = input("digite uma palavra: ").lower().strip()

        #Pulando 300 linhas, a ideia é fazer com que o jogador não veja a palavra
        print("\n" * 300)

        #Variáveis principais
        digitadas = []
        acertos = []
        erros = 0

        #Repetição principal
        while True:
            senha = ""
            for l in palavra:
                #Senha vai receber cada letra da palavra escrita se ela estiver na lista acertos, como ela não está, será acrescentado o traço(-)
                senha += l if l in acertos else '-'

            #Condição caso o jogador vença
            if senha == palavra:
                print(senha)
                print("\033[0;32;40mVoce acertou!\033[m")
                exit()

            #Ambiente do jogador
            print(senha)
            print(f"erros: {erros}/6")
            Letra = input("digite uma letra: ").lower().strip()

            #Condição caso o jogador escreva mais de uma letra
            if len(Letra) != 1:
                print("\n")
                print("\033[0;33;40mEscreva apenas uma letra!\033[m")
                continue

            #Condição caso o jogador escreva uma letra já escrita  
            if Letra in digitadas:
                print("\n")
                print("\033[0;33;40mVc ja usou essa letra!\033[m")
                continue

            #Toda letra escrita pelo jogador é adicionado na lista 'digitadas'
            digitadas += Letra

            #Condição caso o jogador acerte uma letra
            if Letra in palavra:
                print("\n")
                acertos += Letra
            #Condição caso o jogador erre uma letra
            else:
                erros += 1
                #A cada erro que o jogador comete, o corpo da forca se forma
                if erros == 1:
                    boneco(0)
                elif erros == 2:
                    boneco(1)
                elif erros == 3:
                    boneco(2)
                elif erros == 4:
                    boneco(3)
                elif erros == 5:
                    boneco(4)

                #Assim que chegar a 6 erros, o jogador perde
                else:
                    boneco(5)
                    print(f"\033[0;31;40mVc perdeu!\033[m")
                    print(f"a palavra era: \033[0;34;40m{(palavra).upper()}\033[m")
                    exit()

    #Condição caso o jogador escolha 2   
    if modo == 2:
        sleep(3)
        print("vc escolheu jogar com o computador")
        sleep(3)
        print("\n")

    #intervalo para o Computador escolher uma palavra
    print("O computador está escolhendo uma palavra, aguarde...")
    sleep(3)

    #Variáveis principais
    palavra = []
    digitadas = []
    acertos = []
    erros = 0

    #Comando que le um arquivo que guarda algumas palavras
    with open('palavras.txt', 'r') as palavras:
        line = palavras.readlines()
        while line:
            #Uma palavra é escolhida
            a = random.choice(line)

            #depois é adicionada na variável "palavra"
            palavra.append(a)

            #E assim converte a palavra para string
            b = "".join(palavra).strip().lower()

    #Daqui em diante é mesma coisa explicada antes

    while True:
        senha = ""
        for l in b:
            senha += l if l in acertos else '-'

        if senha == b:
            print(senha)
            print("\033[0;32;40mVoce acertou!\033[m")
            exit()
    
        print(senha)
        print(f"erros: {erros}/6")

        Letra = input("digite uma letra: ").lower().strip()

        if len(Letra) != 1:
            print("\n")
            print("\033[0;33;40mEscreva apenas uma letra!\033[m")
            continue
                
        if Letra in digitadas:
            print("\n")
            print("\033[0;33;40mVc ja usou essa letra!\033[m")
            continue

        digitadas += Letra

        if Letra in b:
            print("\n")
            acertos += Letra
        else:
            erros += 1
            if erros == 1:
                boneco(0)
            elif erros == 2:
                boneco(1)
            elif erros == 3:
                boneco(2)
            elif erros == 4:
                boneco(3)
            elif erros == 5:
                boneco(4)
            else:
                boneco(5)
                print("\n")
                print(f"\033[0;31;40mVc perdeu!\033[m")
                print(f"a palavra era: \033[0;34;40m{(b).upper()}\033[m")
                exit()