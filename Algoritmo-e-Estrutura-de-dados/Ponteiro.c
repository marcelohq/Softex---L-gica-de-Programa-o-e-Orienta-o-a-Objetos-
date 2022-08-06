// Crie um vetor com ponteiros utilizando alocação dinâmica na linguagem C, que:

// - use a função realloc;
// - use a função sizeof;
// - que tenha tamanho 22 de vetor;
// - depois libere o bloco utilizando a função free.

// Escolha e descreva um padrão de projetos.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){

    int *vetor = NULL, i, tamanho = 22; //Declaração do ponteiro recebendo valor nulo | Declaração da variável contadora i.

    //A função malloc irá alocar um espaço dinâmico de acordo com o tamanho e tipo primitivo, que são obtidos através do sizeof. 
    vetor = (int *) malloc(5 * sizeof(int)); //Vetor vai receber um ponteiro do tipo int, que tem o tamanho de 4 bytes multiplicado por 22, ou seja: o ponteiro será um vetor com 22 posições com 4 bytes cada.

    printf("Vetor alocado dinamicamente com a função malloc. Tendo 22 posições: \n");

    for(i = 0; i < 22 ; i++){

        *(vetor + i) = rand() % 100;

    }

    for(i = 0; i < 22 ; i++){

        printf("&d ", *(vetor + i));

    }

    vetor = (int * ) realloc(vetor, 5 * sizeof(int)); // Realocando a quantidade de posições de memória. Agora o ponteiro terá 5 posições. O realloc vai pegar o ponteiro, a quantidade de posições e o tamanho do tipo do ponteiro.
    
    free(vetor); // Liberando o espaço de memória do ponteiro que foi alocado durante o programa. 


    return 0;
}