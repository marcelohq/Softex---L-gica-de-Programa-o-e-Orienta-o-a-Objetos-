import br.com.locadora.cadastro.pessoas.Cliente;
import br.com.locadora.cadastro.produtos.Filme;

public class App {
    public static void main(String[] args) {
        
    Cliente ivson = new Cliente("Ivson", "Rua Salvador Dalí, 230", 30072022);
    
    Filme bladeRunner = new Filme("Blade Runner", 22.90, 20071992);

    System.out.println("O cliente "+ivson.getNome()+" comprou o filme "+bladeRunner.getNome()+" por "+bladeRunner.getPreco()+"R$");




    }
}
