import java.awt.FlowLayout;
import javax.swing.*;

public class Painel {
    public static void main(String[] args) {
        JFrame janela = new JFrame("Meu painel");
        janela.setSize(300, 150);
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        janela.setLayout(new FlowLayout());

        JLabel texto = new JLabel("Puxe a alavanca");
        JButton botao = new JButton("Puxar");
        botao.addActionListener(e -> texto.setText("Banana!"));

        janela.add(texto);
        janela.add(botao);
        janela.setVisible(true);
    }
}