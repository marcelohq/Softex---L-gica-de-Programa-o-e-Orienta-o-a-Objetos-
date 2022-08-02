import java.util.Scanner;

public class Main {
    

    public static void main(String[] args) {
        
        //Fazendo a instancia do objeto scanner
        Scanner ler = new Scanner(System.in);

        //Lendo nome do usuário
        System.out.println("Informe o seu nome: ");
        String nome = ler.nextLine();

        //Fechando objeto "ler"
        ler.close();
        
        //Método que deixa uma String maiscula 
        String nomeMaisculo = nome.toUpperCase();
        //Método que informa o caracter de acordo com o indice informado
        char primeiraLetra = nome.charAt(0);
        //Método que retorna o número de carateres de uma string
        int quantidadeLetras = nome.length();
        
        //Saída dos dados
        System.out.println("Nome: "+nomeMaisculo);
        System.out.println("Primeira letra do seu nome: "+primeiraLetra);
        System.out.println("Quantidade de letras que tem o seu nome: "+quantidadeLetras);

    }
}
