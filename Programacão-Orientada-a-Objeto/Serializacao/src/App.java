//Crie um exemplo de como funcionam a serialização e a desserialização de um sistema qualquer. Utilize as classes, 
//os objetos e métodos padrões da Java e insira um endereço físico fictício.
import java.io.*;

public class App {
    public static void main(String[] args) throws IOException, ClassNotFoundException {

        Usuario marcelo = new Usuario("Marcelo", 12);
        
        //Criando objeto que receberá o arquivo e o endereço físico  | Criando o endereço físico do arquivo que vai receber o fluxo de bytes
        ObjectOutputStream saidoObjeto = new ObjectOutputStream(new FileOutputStream("src/usuario.serializable"));

        saidoObjeto.writeObject(marcelo); // Serializando o objeto "marcelo"

        saidoObjeto.close(); //Finalizando o processo

        //Criando objeto que receberá o fluxo de bytes   || Pegando o endereço do fluxo do fluxo de bytes
        ObjectInputStream entradaObjeto = new ObjectInputStream(new FileInputStream("src/usuario.serializable"));
        
        Usuario desserializado = (Usuario) entradaObjeto.readObject();// Lendo o fluxo de bytes e atribuindo as informações a um objeto criado, neste caso é o objeto "desserializado"
        entradaObjeto.close();//Finalizando o processo

        //Mostando os atributos do objeto que foi desserializado. Deve conter as mesmas informações que foram passadas pelo método construtor. Nome: Marcelo, Id: 12.
        System.out.println("Nome do objeto desserializado: "+desserializado.getNome());
        System.out.println("Id do objeto desserializado: "+desserializado.getId());
        

    }
}
