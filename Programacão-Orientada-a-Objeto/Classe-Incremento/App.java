// Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento.
// Depois, desenvolva três ou mais objetos para testar o código.

public class App {
    public static void main(String[] args) {
        
        //Criando os três objetos
        Aluno aluno1 = new Aluno("Marcelo", 30, "História", 8);
        Aluno aluno2 = new Aluno("Luana", 29, "Matemática", 10);
        Aluno aluno3 = new Aluno("Iara", 3, "Artes", 10);

        //Chamando método falar
        aluno1.Falar();
        aluno2.Falar();
        aluno3.Falar();

        //Acessando o atributo estático que deve valer 3 que é a quantidade de alunos
        System.out.println("Quantidade de alunos: "+aluno1.quantidadeAlunos);
        

    }
}
