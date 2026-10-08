package RECURSIVIDADE;

public class Fatorial {
    private int numero;

    public int getNumero(){
        return numero;
    }

    public void setNumero(int numero){
        this.numero = numero;
    }

    public long calcularFatorial(int numero){
        if (numero == 0){
            return 1;
        }
            return numero * calcularFatorial(numero-1);
    }
}