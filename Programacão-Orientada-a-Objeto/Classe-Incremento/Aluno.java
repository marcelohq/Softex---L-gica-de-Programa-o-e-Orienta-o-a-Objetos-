// Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento.
// Depois, desenvolva três ou mais objetos para testar o código.
public class Aluno{

//Atributo da classe
    String nome;
    int idade;
    String disciplina;
    float nota;
    static int quantidadeAlunos;

//Método construtor que inicia o objeto e incrementar a quantidade de alunos
    public Aluno(String nome, int idade, String disciplina, float nota){

        this.nome = nome;
        this.idade = idade;
        this.disciplina = disciplina;
        this.nota = nota;
        quantidadeAlunos ++;

    }
//Métedo que aluno fala seu nome, idade, nota e disciplina favorita.
    void Falar(){

        System.out.printf("Olá, meu nome é "+this.nome+", eu tenho "+this.idade+" anos, minha nota é "+this.nota+" e minha disciplina favorita é "+this.disciplina+"\n");
        
    }
}


