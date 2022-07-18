programa
{
	
	funcao inicio()
	{
		cadeia resposta

		escreva("Escolha um desses veículos: Trator - Moto - Bicicleta - Trem - Carro - Caminhão - Ônibus\n")
		escreva("Paraquedas - Balão - Avião- Helicóptero - Submarino - Barco - Navio - Lancha\n\n")
		
		escreva("O tipo de veículo é terrestre? ")
		leia(resposta)

		se(resposta == "Sim"){

			escreva("Cabe apenas uma pessoa? ")
			leia(resposta)

			se(resposta == "Sim"){

				escreva("É pesado? ")
				leia(resposta)

				se(resposta == "Sim"){
					
					escreva("Então, o transporte escolhido foi o trator.")
					
				}
				senao se(resposta == "Não"){

					escreva("Tem pedal? ")
					leia(resposta)

					se(resposta == "Sim"){

						escreva("Então, o transporte escolhido foi a bicicleta.")
					}
					senao se(resposta == "Não"){

						escreva("Então, o transporte escolhido foi a moto.")
					}

					senao{
						escreva("Resposta inválida!")
					}
					
				}
				senao{

						escreva("Resposta inválida!")
					
				}
			}		

			senao se(resposta == "Não"){

				escreva("É utilizado como transporte público? ")
				leia(resposta)
	
				se(resposta == "Sim"){
	
					escreva("Cabem mais de 45 passageiros ? ")
					leia(resposta)
	
					se(resposta == "Sim"){
	
						escreva("Então, o transporte escolhido foi o trem.")
						
					}
					senao se(resposta == "Não"){
	
						escreva("Então, o transporte escolhido foi o ônibus.")
						
					}
					senao{
	
						escreva("Resposta inválida!")
						
					}
				}
				senao se(resposta == "Não"){
	
					escreva("É utlizado para levar grandes cargas ? ")
					leia(resposta)
	
					se(resposta == "Sim"){
	
						escreva("Então, o transporte escolhido foi o caminhão.")
						
					}
					senao se(resposta == "Não"){
	
						escreva("Então, o transporte escolhido foi o carro.")
						
					}
					senao{
	
						escreva("Resposta inválida!")
						
					}
				
				}
			}
		}
		
		senao se(resposta == "Não"){

			escreva("O tipo de veículo é aereo? ")
			leia(resposta)

			se(resposta == "Sim"){

				escreva("É pesado? ")
				leia(resposta)

				se(resposta == "Sim"){

					escreva("O veículo pode fazer viagens intercontinentais? ")
					leia(resposta)

					se (resposta == "Sim"){

						escreva("Então, o transporte escolhido foi o avião.")
						
					}
					senao se(resposta == "Não"){

						escreva("Então, o transporte escolhido foi o helicoptero.")
					}

					senao{

						escreva("Resposta inválida!")
						
					}
					

					
				}senao se(resposta == "Não"){

					escreva("Cabe apenas uma pessoa? ")
					leia(resposta)

					se(resposta == "Sim"){

						escreva("Então, o transporte escolhido foi o paraquedas.")
						
					}
					senao se(resposta == "Não"){

						escreva("Então, o transporte escolhido foi o balão.")
						
					}
					senao{

						escreva("Resposta inválida!")
						
					}
					
				}
				senao{

					escreva("Resposta inválida!")
					
				}
				
			}
				
			senao se(resposta == "Não"){

				escreva("O veículo é pesado? ")
				leia(resposta)
				
				se(resposta == "Sim"){

					escreva("O veículo pode ficar submerso? ")
					leia(resposta)

					se (resposta == "Sim"){

						escreva("Então, o transporte escolhido foi o submarino.")
					}
					senao se(resposta == "Não"){

						escreva("Então, o transporte escolhido foi o navio.")
						
					}
					senao{
						escreva("Resposta inválida!")
					}
					
				}
				senao se(resposta == "Não"){

					escreva("O veículo é usado para percorrer pequenas distancias? ")
					leia(resposta)
					
					se (resposta == "Sim"){

						escreva("Então, o transporte escolhido foi a lancha.")
						
					}
					senao se (resposta == "Não"){

						escreva("Então, o transporte escolhido foi o barco.")
					}

					senao{

						escreva("Resposta inválida!")
						
					}
				}
	
			}
			senao{

				escreva("Resposta inválida!")
				
			}
			
		}

		senao{

			escreva("Resposta inválida!")
			
		}
	}
}
	
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 247; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = {resposta, 6, 9, 8};
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */