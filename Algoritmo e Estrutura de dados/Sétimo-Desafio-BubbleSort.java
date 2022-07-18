import java.util.Arrays;
import java.util.Scanner;

public class BubbleSort {
    
    public static void main(String[] args) {
        
        Scanner ler = new Scanner(System.in);
        int auxiliar;
        int vetor[] = new int[10];
        
        for(int i = 0; i < vetor.length; i++){

            System.out.print("Informe o valor da posição "+i+": ");
            vetor[i] = ler.nextInt();
        }

        ler.close();
        
        System.out.println("Vetor não ordenado: "+Arrays.toString(vetor));

        for(int i = 9; i >=0; i--) {
            
            for(int j = 0; j <= i - 1; j++){

                if(vetor[j] > vetor[j + 1]){
                    auxiliar = vetor[j];
                    vetor[j] = vetor[j + 1];
                    vetor[j + 1] = auxiliar;
                }

            }
        }

        System.out.println("Vetor ordenado: "+Arrays.toString(vetor));

    }

}
