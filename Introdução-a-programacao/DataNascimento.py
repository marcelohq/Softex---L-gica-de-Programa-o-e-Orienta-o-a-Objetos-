from logging import exception

#Função que recebe a data e obriga o usuário a digitar o tipo de valor correto.
def dataCorreta(mensagem):

    while True:
        try:
            data = int(input(mensagem))
        except(TypeError, ValueError):
            print("Você precisa digitar um valor inteiro para o seu nascimento!")
            continue
        else:
            return data
#variável que servirá de condição de parada para o laço que vem a seguir.
parar = False

#Pedindo o nome do usuário 
nome = input("Informe o seu nome: ")
#Laço que puxa a função de validar os valores da data, com a condição de parada o ano informado estar entre 1922 e 2022
while parar == False:
    data = dataCorreta("Informe em que ano você nasceu: ")
    if data <1922 or data >2022:
        print("Você digitou um ano fora do intervalo de 1922 e 2022")
    else:
        parar = True

#Saída dos valores de entrada que foram processados, informando nome e quantos anos você terá em 2022.
print(f"Seu nome é {nome}")
print("Sua idade em 2022 será ",2022 - data,"anos")
