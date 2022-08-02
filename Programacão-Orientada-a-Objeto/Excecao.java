import java.util.InputMismatchException;
import java.util.Scanner;
public class Excecao {
    
    public static void main(String[] args) {
        
        //Criando instancia do objeto scanner
        Scanner leia = new Scanner(System.in);

        do{
            try{
                //Sistema pede o nome do usuário e ler o valor informado
                System.out.println("Informe sua idade:");
                int idade = leia.nextInt();

                System.out.println("Você tem "+idade+" anos");
                // Quebra do laço se não houve nenhuma exceção
                break;

            }
            // Catch para o erro da entrada de dados não ser um número inteiro.
            catch(InputMismatchException erro) {

                System.out.println("A sua idade deve contar nýmeros, não letras!");
                leia.nextLine(); // Descarta a entrada errada do usuário e impede que o código entre em loop infinito
                
                // Continue para quebrar o ciclo de execução e retonar para o inicio do laço
                continue;
                
            }
        }while(true);    

        //Fechando método Scanner
        leia.close();
    
    }

}
