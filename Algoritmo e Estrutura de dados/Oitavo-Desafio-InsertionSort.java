import java.util.Scanner;
import java.util.Arrays;
public class InsertionSort {
    
    public static void main(String[] args) {
        
	Scanner ler = new Scanner(System.in);
        int vetor[] = new int[30];
        int i = 0;
        int valorIndice;

        while(i < 30){

            System.out.print("Informe o valor do índice "+i+": ");
            valorIndice = ler.nextInt();
            if(valorIndice % 2 == 1){
                vetor[i] = valorIndice;
                i++;
            }
        }

        ler.close();

        System.out.println("Vetor não ordernado: "+Arrays.toString(vetor));

        for (i = 1; i < vetor.length; i++) { 
		
            int j = i;
        
            while (j > 0 && vetor[j] < vetor[j-1]) {
                int aux = vetor[j];
                vetor[j] = vetor[j - 1];
                vetor[j - 1] = aux;
                j -= 1;
            }
        }

        System.out.println("Vetor ordernado com o Isertion Sort: "+Arrays.toString(vetor));
    }

}
