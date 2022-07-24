def calculadora(num1, num2, op):
    
    if op == "+":
        return num1 + num2

    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return 0

primeiroNumero = float(input("Informe o valor do primeiro número: "))
segundoNumero = float(input("Informe o valor do segundo número: "))

print("Operaçções disponíveis: Soma / Subtração / Multiplicação e Divisão")
operacao = input("Informe o operador: ")

result = calculadora(primeiroNumero, segundoNumero, operacao)
print("O resultado entre",primeiroNumero,operacao,segundoNumero," é: ",result)



