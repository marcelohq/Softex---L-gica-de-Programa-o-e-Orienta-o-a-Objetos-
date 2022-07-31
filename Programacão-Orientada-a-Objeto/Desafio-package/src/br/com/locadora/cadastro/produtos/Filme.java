package br.com.locadora.cadastro.produtos;

public class Filme {

    //Atributos da classe
    private String nome;
    private double preco;
    private int id;

    //Método construtor 
    public Filme(String nome, double preco, int id){

        this.nome = nome;
        this.preco = preco;
        this.id = id;

        }
    
    // Métodos gets e sets da classe.
    public String  getNome(){
        return this.nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public double  getPreco(){
        return this.preco;
    }

    public void setPreco(double preco){
        this.preco = preco;
    }

    public void setId(int id){
        this.id = id;
    }

    public int  getId(){
        return this.id;
    }

}
