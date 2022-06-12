programa
{
	
	funcao inicio()
	{
		real nota = 0.0, maiorNotaA = 0.0, maiorNotaB = 0.0, maiorNotaC = 0.0, maiorNotaD = 0.0, maiorNota = 0.0 
		cadeia nome, nomeA= "", nomeB = "", nomeC = "", nomeD = "", nomeMaior = "", turma = "" 
		inteiro quantidadeAprovados = 0, quantidadeA= 0, quantidadeB = 0, quantidadeC = 0, quantidadeD = 0 


	    para(inteiro i = 1 ; i<=100 ; i++){
      
         escreva("Informe o nome do aluno: ")
         leia(nome)
         escreva("Informe a nota do aluno: ")
         leia(nota)
         escreva("Informe a turma do aluno: ")
         leia(turma)

         limpa()
         
         se (nota >=7){

            quantidadeAprovados = quantidadeAprovados + 1
            
            se (nota > maiorNota){
            
               nomeMaior = nome
               maiorNota = nota

            }
            
            se ( turma == "A"){
            
                  quantidadeA = quantidadeA + 1

                        se (nota > maiorNotaA) {

                           maiorNotaA = nota
                           nomeA = nome
                        }
            	}     

            senao se ( turma == "B"){

                  quantidadeB = quantidadeB + 1

                        se (nota > maiorNotaB){

                           maiorNotaB = nota
                           nomeB = nome
                        }
                 }            
               
            senao se ( turma == "C"){

                 quantidadeC = quantidadeC + 1

                        se (nota > maiorNotaC){

                           maiorNotaC = nota
                           nomeC = nome
                        }
           	 }
               
               
            senao se ( turma == "D"){

                  quantidadeD = quantidadeD + 1

                        se (nota > maiorNotaD){

                           maiorNotaD = nota
                           nomeD = nome
                        }
            	}           
         }  
  
	 }
 
       escreva("Total de estudantes aprovados: ", quantidadeAprovados)

       se(quantidadeA < 1){

		escreva("\nA turma A não teve nenhum aluno aprovado.")
       	
       }senao se(quantidadeA == 1){

		escreva("\nA turma A conseguiu aprovar um aluno.\n")
		escreva("Aluno: ",nomeA,"\n")
		escreva("Nota: ",maiorNotaA)
       }senao{

		escreva("\nForam aprovados ",quantidadeA," alunos da turma A\n")
		escreva(nomeA, " obteve a maior nota da turma A, tirando ",maiorNotaA)
       	
       }
       
       se(quantidadeB < 1){

		escreva("\nA turma B não teve nenhum aluno aprovado.")
       	
       }senao se(quantidadeB == 1){

		escreva("\nA turma B conseguiu aprovar um aluno.\n")
		escreva("Aluno: ",nomeB,"\n")
		escreva("Nota: ",maiorNotaB)
       }senao{

		escreva("\nForam aprovados ",quantidadeB," alunos da turma B\n")
		escreva(nomeA," obteve a maior notada turma B, tirando ",maiorNotaB)
       	
       }

	se(quantidadeC < 1){

		escreva("\nA turma C não teve nenhum aluno aprovado.")
       	
       }senao se(quantidadeC == 1){

		escreva("\nA turma C conseguiu aprovar um aluno.\n")
		escreva("Aluno: ",nomeC,"\n")
		escreva("Nota: ",maiorNotaC)
       }senao{

		escreva("\nForam aprovados ",quantidadeC," alunos da turma C\n")
		escreva(nomeA, " obteve a maior nota da turma C, tirando ",maiorNotaC)
       	
       }
       
       se(quantidadeD < 1){

		escreva("\nA turma D não teve nenhum aluno aprovado.")
       }senao se(quantidadeD == 1){

		escreva("\nA turma D conseguiu aprovar um aluno.\n")
		escreva("Aluno: ",nomeD,"\n")
		escreva("Nota: ",maiorNotaD,"\n")
	  }senao{
		escreva("\nForam aprovados ",quantidadeD," alunos da turma D\n")
		escreva(nomeA, " obteve a maior nota da turma D, tirando ",maiorNotaA)
       }
      
       escreva("\n",nomeMaior, " foi o estudante que obteve a maior nota entre todas as turmas, ficando com ",maiorNota,"\n")
       
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 519; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */