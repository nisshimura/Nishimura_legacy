import java.awt.Color;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.border.LineBorder;

public class GridBagLayoutSample {

    private void createAndShowGUI() {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setBounds(10, 10, 500, 250);
        frame.setTitle("GridBagLayoutSample");

        JPanel p = new JPanel();
        GridBagLayout gblayout = new GridBagLayout();
        p.setLayout(gblayout);

        JLabel l1 = new JLabel("label1", SwingConstants.CENTER);
        JLabel l2 = new JLabel("label2", SwingConstants.CENTER);
        JLabel l3 = new JLabel("label3", SwingConstants.CENTER);
        JLabel l4 = new JLabel("label4", SwingConstants.CENTER);

        l1.setBorder(new LineBorder(Color.BLACK, 2));
        l2.setBorder(new LineBorder(Color.BLACK, 2));
        l3.setBorder(new LineBorder(Color.BLACK, 2));
        l4.setBorder(new LineBorder(Color.BLACK, 2));

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 1;
        gbc.gridheight = 2;
        gbc.insets = new Insets(1, 1, 1, 1);
        gbc.weightx = 1.0;
        gbc.weighty = 1.0;
        gblayout.setConstraints(l1, gbc);
        p.add(l1);

        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.gridwidth = 1;
        gbc.gridheight = 1;
        gbc.insets = new Insets(1, 1, 1, 1);
        gbc.weightx = 1.0;
        gbc.weighty = 1.0;
        gblayout.setConstraints(l2, gbc);
        p.add(l2);

        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 1;
        gbc.gridy = 1;
        gbc.gridwidth = 1;
        gbc.gridheight = 1;
        gbc.insets = new Insets(1, 1, 1, 1);
        gbc.weightx = 1.0;
        gbc.weighty = 1.0;
        gblayout.setConstraints(l3, gbc);
        p.add(l3);

        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 2;
        gbc.gridheight = 1;
        gbc.insets = new Insets(1, 1, 1, 1);
        gbc.weightx = 1.0;
        gbc.weighty = 1.0;
        gblayout.setConstraints(l4, gbc);
        p.add(l4);

        frame.getContentPane().add(p);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new GridBagLayoutSample().createAndShowGUI();
            }
        });
    }
}
