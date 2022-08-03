#Importação da classe que implementa os métodos das operações com os números complexos
from NumerosComplexos import *

a = 1 + 3j # Atribuindo o número complexo a varíavel a
b = 3 + 9j # Atribuindo o número complexo a varíavel b
c = 4 + 2j # # Atribuindo o número complexo a varíavel c


print(Complexo.somar(a, b, c)) #Método de adição 
print(Complexo.subtrair(a, b, c)) #Método de subtracao
print(Complexo.multiplicar(a, b, c)) #Método de multiplicacao
print(Complexo.dividir(a, b, c)) #Método de dividir

#Método que informa a propriedade real e imagem do número complexo 
Complexo.propriedadeReaImg(a)
Complexo.propriedadeReaImg(b)
Complexo.propriedadeReaImg(c)

