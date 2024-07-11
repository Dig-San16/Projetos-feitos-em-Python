#importando a biblioteca

from time import sleep

#Funcionamento das perguntas

def pergunta(falar):
    a = input(falar).lower()
    while a != "sim" and a != "não" and a != "nao":
        print("\033[0;32;40mdigite entre SIM ou NÂO por favor\033[m")
        a = input(falar).lower()
    else:
        return a
    
#Região enche linguiça

def desembuchar(falar):
    sleep(4)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print(falar)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('\n')

desembuchar('Olá cara')
desembuchar('vamos dar uma olhada nas profundezas da internet em busca de encontrar a resposta dos motivos e causas de vc ser tão diferente dos outros?')
desembuchar('para começarmos, vc deve seguir algumas regrinhas...')
desembuchar('é o seguinte, vc só pode responder entre sim ou não')
desembuchar('e é só isso mesmo, vamos começar!')
sleep(3)

#Região de perguntas

personalidade = []

E = pergunta("diz ai, tu é extrovertido?: ")
personalidade.append('E') if E == 'sim' else personalidade.append("I")

I = pergunta("Tu é mais pé no chão do que idealista e sonhador?: ")
personalidade.append('S') if I == 'sim' else personalidade.append("N")

D = pergunta("Vc é mais lógico do que sentimental?: ")
personalidade.append('T') if D == 'sim' else personalidade.append("F")

V = pergunta("Seu estilo de vida é mais organizado e metódico do que livre e espontaneo?: ")
personalidade.append('J') if V == 'sim' else personalidade.append("P")

#Imprimindo os Resultados

a = ''.join(personalidade)

if 'NT' in a:
    print("Sua personalidade é:", '\033[0;35;40m' + a + '\033[m')
elif 'NF' in a:
    print("Sua personalidade é:", '\033[0;32;40m' + a + '\033[m')
elif 'S' and 'P' in a:
    print("Sua personalidade é:", '\033[0;33;40m' + a + '\033[m')
else:
    print("Sua personalidade é:", '\033[0;36;40m' + a + '\033[m')