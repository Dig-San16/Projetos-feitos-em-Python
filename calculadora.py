#Lista de operadores númericos
operadores = ["+","-","x","/"]

#Repetição pai de todos
while True:
    #Código que se espera uma exceção
    try:
        #Variáveis principais
        a = float(input("digite um numero: "))
        b = float(input("digite outro numero: "))
        operador = input("digite entre uma das operações (+,-,x,/): ")

        #Condição caso o operador escrito não estiver na lista
        if operador not in operadores:
            print("\033[1;34;40mdigite o operador correto\033[m")
            print("\n")
            continue 

        #Ambiente que seleciona a conta a ser somada
        for o in operadores:
            if operador == "+":
                soma = a + b
            elif operador == "-":
                soma = a - b
            elif operador == "x":
                soma = a * b
            else:
                soma = a / b

        #Mostrando o resultado
        print(f"\033[1;32;40m{a} {operador} {b} = {soma}\033[m")

    #Condição caso um erro do tipo ValueError ocorrer
    except ValueError:
        print("\033[1;34;40mdigite apenas número\033[m")

    #Condição caso um erro do tipo ZeroDivisionError ocorrer
    except ZeroDivisionError:
        print(f"\033[1;34;40m{a} {operador} {b} = infinito\033[m")
    
    #pulando linha
    print("\n")