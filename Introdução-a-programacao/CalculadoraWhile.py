import os
import time
def soma(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1, numero2):
    return numero1 / numero2

operacao = -1

while operacao != 0:
    print("Escolha uma das operações: ")
    print("1: Soma \n2: Subtração\n3: Multiplicação \n4: Divisão \n0: Sair")
    operacao = int(input("Informe a operação escolhida: "))

    if operacao == 0:
        break
    elif operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4:
        print("Essa opção não existe")
        executar = False
        time.sleep(3)
    else:
        executar = True
    
    os.system('cls')

    if executar == True:
        numero1 = int(input("Informe o primeiro número: "))
        numero2 = int(input("Informe o segundo valor: "))
            
        if operacao == 1:
            resultado = soma(numero1, numero2)
            print("O resultado da soma entre ",numero1," e ",numero2," é: ",resultado,"\n")
        elif operacao == 2:
            resultado = subtracao(numero1, numero2)
            print("O resultado da divisão entre ",numero1," e ",numero2," é: ",resultado,"\n")
        elif operacao == 3:
            resultado = multiplicacao(numero1, numero2)
            print("O resultado da multiplicação entre ",numero1," e ",numero2," é: ",resultado,"\n")
        elif operacao == 4:
            resultado = divisao(numero1, numero2)
            print("O resultado da divisão entre ",numero1," e ",numero2," é: ",resultado,"\n")
print("Operacação finalizada.")





