# Classe que implementa os métodos das operações com os números complexos
class Complexo:
    def somar(a, b, c): #Método de adição 
        return a + b + c

    def subtrair(a, b, c): #Método de subtracao
        return a - b - c

    def multiplicar(a, b, c): #Método de multiplicacao
        return a * b* c

    def dividir(a, b, c): #Método de dividir
        return (a/b) / c

#Método que informa a propriedade real e imagem da número complexo
    def propriedadeReaImg(a): 
        print("Propriedade real de "+str(a)+" é: "+str(a.real))
        print("propriedade imaginária de "+str(a)+" é: "+str(a.imag)+"\n")