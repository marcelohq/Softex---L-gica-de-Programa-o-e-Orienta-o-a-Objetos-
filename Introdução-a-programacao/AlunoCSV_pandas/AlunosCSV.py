# Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. 
# O arquivo deve ter a seguinte estrutura:

# aluno: Nome do aluno;
# nota_1: Primeira nota;
# nota_2: Segunda nota;
# faltas: Número de faltas;

# O programa lerá esse arquivo e criará duas colunas. 
# A primeira coluna será “media”, que terá a média das duas notas do aluno. 
# A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

# O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. 
# O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

# Por fim, o programa deverá mostrar na tela:
# - o maior número de faltas;
# - a média geral das notas dos alunos;
# - e a maior média.

# Veja em anexo um exemplo do arquivo “notas_alunos.csv”.

import pandas as pd


#Criando o 'dataframe'
dataframe = pd.read_csv("notas_alunos.csv")


#Linha que tira a média das notas dos alunos e adiciona em uma coluna chamada medita_notas.

media = (dataframe["nota_1"] + dataframe["nota_2"]) / 2
dataframe["media_notas"] = media


#Adicionando alunos aprovados e reprovadas na coluna "situacao"

dataframe.loc[(dataframe["faltas"] > 5) | (dataframe["media_notas"] < 7), "situacao"] = "Reprovado"
dataframe.loc[(dataframe["faltas"] <= 5) & (dataframe["media_notas"] >= 7), "situacao"] = "Aprovado"

print(dataframe)

#Resumo de quem teve mais falta, tirou maior média e média total da turma.
print("Maior quantidade de faltas: "+str(dataframe["faltas"].max()))
print("Maior média: "+str(dataframe["media_notas"].max()))
print("Média da turma: "+str(dataframe["media_notas"].mean()))

dataframe.to_csv("alunos_situacao.csv")






