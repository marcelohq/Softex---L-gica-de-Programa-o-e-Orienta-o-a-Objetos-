public class Professor {
    
    private String nome;
    private int matricula;

    // Método construtor que vai iniciar a classe quando ele for "instanciada" 
    public  Professor(String nome, int matricula){
        this.nome = nome;
        this.matricula = matricula;
    }

    //Métedo set que modifica o valor do atributo nome

    public void setNome(String nome){
        this.nome = nome;
    }

    //Métedo get que retonar o valor do atributo nome
    public String getNome(){
        return this.nome;
    }

    //Métedo set que modifica o valor atributo matricula
    
    public void setMatricula(int matricula){
        this.matricula = matricula;
    }
    
    //Métedo get que retonar o valor do atributo matricula
    public int getMatricula(){
        return this.matricula;
    }
    

public static void main(String[] args) {
        
    //Criando os dois objetos e atribuindo valores aos atributos 
    Professor ivson = new Professor("Ivson", 290712022);
    Professor marcelo = new Professor("Marcelo", 20071992);
        
    //Nome e matrícula do objeto "Ivson"
    System.out.println("Nome: "+ivson.getNome());
    System.out.println("Matrícula: "+ivson.getMatricula());


    //Setando os novos valores do atributo do objeto
    ivson.setNome("Ivson Silva");
    ivson.setMatricula(123456);
        
    // Saída do novo nome e da nova matrícula
    System.out.println("Novo nome: "+ivson.getNome());
    System.out.println("Nova matrícula: "+ivson.getMatricula()+"\n");


    //Nome e matrícula do objeto "Marcelo"
    System.out.println("Nome: "+marcelo.getNome());
    System.out.println("Matrícula: "+marcelo.getMatricula());


    //Setando os novos valores do atributo do objeto
    marcelo.setNome("Marcelo dos Santos");
    marcelo.setMatricula(6543321);
        
    // Saída do novo nome e da nova matrícula
    System.out.println("Novo nome: "+marcelo.getNome());
    System.out.println("Nova matrícula: "+marcelo.getMatricula());

    }
}



