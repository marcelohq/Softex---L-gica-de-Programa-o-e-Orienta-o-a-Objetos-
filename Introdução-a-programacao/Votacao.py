# Desenvolva um código que simule uma eleição com três candidatos. 
# - candidato_X => 889 
# - candidato_Y => 847 
# - candidato_Z => 515 
# - branco => 0 
# O código deve perguntar se deseja finalizar a votação depois do voto. 
# Caso o número do voto não corresponda a nenhum candidato ou seja branco, ele deve ser tratado como nulo.  
# Se for inserido um texto ao invés de número, o código deve retornar uma mensagem para votar novamente. 
# Quando a votação for finalizada, o código deverá mostrar o vencedor,
# aquele com o maior número de votos e, também, a quantidade de votos de cada candidato, os brancos e nulos  

import time
import os


#Função para limpar a tela 

def limparTela():
    os.system('cls')

#Variáveis que vão contar os votos e a condição de parada do laço principal

continuar = "Sim"
candidatoX = 0
candidatoY = 0
candidatoZ = 0
brancosNulos = 0

#Laço da votação, quando o que for escrito for diferente de Sim a votação termina.
while continuar == "Sim":
    print("V O T A Ç Ã O   P A R A   P R E S I D E N T E\n")
    print("889: candidato_X \n847: candidato_Y\n515: candidato_Z \n0: branco")

    #Tratamento de exceção, caso o usuário digite um texto e não um valor inteiro.
    try:
        voto = int(input("Infome o número do candidato: "))
    except(TypeError, ValueError):
            print("Você precisa digitar um valor inteiro para votar. Não vale texto nem números reais")
            time.sleep(2)
            limparTela()
            continue

    #Contagem dos votos válidos e nulos

    else:
        if(voto == 889):
        
            candidatoX = candidatoX + 1
        
        elif(voto == 847):

            candidatoY = candidatoY + 1
        
        elif(voto == 515):

            candidatoZ = candidatoZ + 1
        else:
            brancosNulos = brancosNulos + 1

        #Pergunta para saber se o usuário quer continuar votando
        continuar = input("Deseja continuar votatando ?\n\nEntão digite Sim:  ")
        limparTela()

print("\nEleição finalizada!\n")
#Laço e "instruções" para contagem dos votos
for i in range(10, 0, -1):
    print("Tempo para a contagem de votos ser finalizada: ",i)
    time.sleep(1)

print("Contagem concluída!\n")

time.sleep(1)

#Condicionais que revelam o vencedor

if candidatoX > candidatoY and candidatoX > candidatoZ:
    print("----------------------------------------\n")
    print("Candidato X foi o vencendor das eleições!")
    print("----------------------------------------\n")
elif candidatoY > candidatoX and candidatoY > candidatoZ:
    print("----------------------------------------\n")
    print("Candidato Y foi o vencedor das eleições!")
    print("----------------------------------------\n")
elif candidatoZ > candidatoX and candidatoZ > candidatoY:
    print("----------------------------------------\n")
    print("Candidato Z foi o vencedor das eleições!")
    print("----------------------------------------\n")
else:
    print("Houve um empate entre os três candidatos.\nQue loucura, cara.")

time.sleep(1)

#Instruções que revelam a quantidade de votos de cada candidato e o total de votos nulos.

print(f"Quanditade de votos recebidos do canditado X: {candidatoX}")
print(f"Quanditade de votos recebidos do canditado Y: {candidatoY}")
print(f"Quanditade de votos recebidos do canditado Z: {candidatoZ}")
print(f"Quanditade de votos brancos e nulos: {brancosNulos}")