import java.io.Serializable;

//Para fazer a serialização é necessário implementar a interface Serializable
public class Usuario implements Serializable {

    //Atributos da classe
    private String nome;
    private int id; 

    //Método construtor
    public Usuario(String nome, int id) {
        this.nome = nome;
        this.id = id;
    }

    //Métodos gets e sets
    public String getNome(){
        return this.nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public int getId(){
        return this.id;
    }

    public void setId(int id){
        this.id = id;
    }
}