quantidadeRodas = int(input("Informe a quantidade de rodas do veículo: "))
peso = float(input("Informe o peso bruto do veículo em kg: "))
quantidadePessoas = int(input("Informe a quantidade de pessoas que cabem no veículo: "))

if quantidadeRodas >=2 and quantidadeRodas <=3 :
    print("Veículos com duas ou três rodas")
elif quantidadeRodas == 4 and quantidadePessoas <=8 and peso <= 3500:
    print("Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg")
elif quantidadeRodas >=4 and peso >=3501 and peso <=6000:
    print("Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg")
elif quantidadeRodas >=4 and quantidadePessoas >=8:
    print("Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;")
elif quantidadeRodas >=4 and peso >6000:
    print("Veículos com quatro rodas ou mais e com mais de 6000 kg")
