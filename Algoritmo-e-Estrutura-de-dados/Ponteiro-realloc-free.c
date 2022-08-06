// Crie um vetor com ponteiros utilizando alocação dinâmica na linguagem C, que:

// - use a função realloc;
// - use a função sizeof;
// - que tenha tamanho 22 de vetor;
// - depois libere o bloco utilizando a função free.

// Escolha e descreva um padrão de projetos.

#include <stdio.h>
#include <stdlib.h>

int main(){

    int *vetor = NULL, i; //Declaração do ponteiro recebendo valor nulo | Declaração da variável contadora i.

    //A função malloc irá alocar um espaço dinâmico de acordo com o tamanho e tipo primitivo, que são obtidos através do sizeof. 
    vetor = (int *) malloc(4 * sizeof(int)); //Vetor vai receber um ponteiro do tipo int, que tem o tamanho de 4 bytes multiplicado por 4, ou seja: o ponteiro será um vetor com 4 posições de 4 bytes cada.

    vetor[0] = 1;
    vetor[1] = 3;
    vetor[2] = 15;
    vetor[3] = 15;

    printf("Vetor alocado dinamicamente com a função malloc. Tendo 4 posições: \n");

    for(i = 0; i < 4 ; i++){

        printf("vetor[%d]: %d\n", i, vetor[i]);

    }

    vetor = (int * ) realloc(vetor, 22 * sizeof(int)); // Realocando a quantidade de posições de memória. Agora o ponteiro terá 5 posições. O realloc vai pegar o ponteiro, a quantidade de posições e o tamanho do tipo do ponteiro.
    
    //Preenchendo Vetor
    for(i = 0; i < 22 ; i++){

        vetor[i] = i * 2;

    }

    //Lendo vetor
    
    printf("Vetor com novo tamanho: \n");
    for(i = 0; i < 22 ; i++){

        printf("vetor[%d]: %d\n", i, vetor[i]);

    }
    
    free(vetor); // Liberando o espaço de memória do ponteiro que foi alocado durante o programa. 


    return 0;
}