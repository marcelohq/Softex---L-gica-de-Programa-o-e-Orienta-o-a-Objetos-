package br.com.locadora.cadastro.pessoas;


public class Cliente {

    //Atributos da classe
    private String nome;
    private String endereco; 
    private int id;

    //Método construtor 
    public Cliente(String nome, String endereco, int id){

    this.nome = nome;
    this.endereco = endereco;
    this.id = id;
    
    }

    // Métodos gets e sets da classe.
    public String  getNome(){
        return this.nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public String  getEndereco(){
        return this.endereco;
    }

    public void setEndereco(String endereco){
        this.endereco = endereco;
    }

    public void setId(int id){
        this.id = id;
    }

    public int  getId(){
        return this.id;
    }


}

