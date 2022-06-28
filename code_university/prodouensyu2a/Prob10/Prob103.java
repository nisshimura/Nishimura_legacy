import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Prob103 {
    private static String labelPrefix = "Total : ";
    private int num = 0;
    private JLabel label;
    JTextArea text = new JTextArea(10, 20);

    class ButtonAction1 implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            num += Integer.valueOf(text.getText());
            label.setText(labelPrefix + num);
        }
    }

    class ButtonAction2 implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            num = 0;
            label.setText(labelPrefix + num);
        }
    }

    public Component createComponents() {
        label = new JLabel(labelPrefix + "0    ");
        JButton button_add = new JButton("ADD");
        JButton button_clear = new JButton("clear");


        ButtonAction1 action1 = new ButtonAction1();
        ButtonAction2 action2 = new ButtonAction2();
        button_add.addActionListener(action1);
        button_clear.addActionListener(action2);

        JPanel pane = new JPanel();
        GridBagLayout layout = new GridBagLayout();
        pane.setLayout(layout);
        GridBagConstraints gbc = new GridBagConstraints();

        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 2;
        gbc.gridheight = 2;
        gbc.insets = new Insets(1, 1, 1, 1);
        gbc.weightx = 1.0;
        gbc.weighty = 1.0;
        layout.setConstraints(text, gbc);
        pane.add(text);

        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 1;
        gbc.gridheight = 1;
        gbc.insets = new Insets(1, 1, 1, 1);
        gbc.weightx = 1.0;
        gbc.weighty = 1.0;
        layout.setConstraints(button_add, gbc);
        pane.add(button_add);

        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 1;
        gbc.gridy = 2;
        gbc.gridheight = 1;
        gbc.gridwidth = 1;
        gbc.insets = new Insets(1, 1, 1, 1);
        gbc.weightx = 1.0;
        gbc.weighty = 1.0;
        layout.setConstraints(button_clear, gbc);
        pane.add(button_clear);

        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 0;
        gbc.gridy = 3;
        gbc.gridheight = 1;
        gbc.gridwidth = 1;
        gbc.insets = new Insets(1, 1, 1, 1);
        gbc.weightx = 1.0;
        gbc.weighty = 1.0;
        layout.setConstraints(label, gbc);
        pane.add(label);
        return pane;
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Prob103");
        Prob103 app = new Prob103();
        Component contents = app.createComponents();

        frame.getContentPane().add(contents, BorderLayout.CENTER);
        frame.setBounds(10, 10, 300, 200);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
