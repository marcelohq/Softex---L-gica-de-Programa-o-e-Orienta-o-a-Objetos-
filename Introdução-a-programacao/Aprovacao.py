
nomeAluno = input("Informe o nome do aluno: ")
nota = float(input("Informe a nota do aluno: "))
faltas = int(input("Informe a quantidade de faltas do aluno: "))

if nota < 7 or faltas >3:
    print("O aluno ",nomeAluno," está reprovado")
else:
    print("O aluno ",nomeAluno," foi aprovado!!")


