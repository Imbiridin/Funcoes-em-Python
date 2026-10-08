package RECURSIVIDADE;

import javax.swing.JOptionPane;

public class Main {
    public static void main(String[] args) {
        Fatorial ft = new Fatorial();

        String numero_T = JOptionPane.showInputDialog("Digite o numero para saber o fatorial: ");
        ft.setNumero(Integer.parseInt(numero_T));

        JOptionPane.showMessageDialog(null, ft.calcularFatorial(ft.getNumero()));
    },
}
