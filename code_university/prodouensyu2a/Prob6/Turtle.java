/* Turtle.java
 *
 * Copyright (C) 2004 by Shigeru Chiba,  All rights reserved.
 * Updated for Programming 2 class (2015)
 *
 */
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.awt.Rectangle;
import java.awt.image.BufferedImage;
import java.util.List;
import java.util.LinkedList;


class Pond extends JPanel {
    private BufferedImage bimg;
    private List<Turtle> turtles;     // must be atomic.

    private static final int WIDTH = 400;
    private static final int HEIGHT = 400;

    public Pond() {
        bimg = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);
        Graphics pen = bimg.createGraphics();
        pen.setColor(Color.white);
        pen.fillRect(0, 0, WIDTH, HEIGHT);
        turtles = new LinkedList<Turtle>();

        JFrame app = new JFrame("Turtle");
        app.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JMenu speed = new JMenu("Speed");
        ActionListener listener = new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    String cmd = e.getActionCommand();
                    if (cmd.equals("extreme"))
                        Turtle.interval = 0;
                    else if (cmd.equals("very fast"))
                        Turtle.interval = Turtle.SLOW_INTERVAL / 10;
                    else if (cmd.equals("fast"))
                        Turtle.interval = Turtle.SLOW_INTERVAL / 2;
                    else
                        Turtle.interval = Turtle.SLOW_INTERVAL;
                }
            };

        speed.add("slow").addActionListener(listener);
        speed.add("fast").addActionListener(listener);
        speed.add("very fast").addActionListener(listener);
        speed.add("extreme").addActionListener(listener);

        JMenuBar bar = new JMenuBar();
        bar.add(speed);
        app.setJMenuBar(bar);
        app.setSize(WIDTH, HEIGHT);
        app.setResizable(false);
        app.getContentPane().add(this);
        app.setVisible(true);
    }

    public void addTurtle(final Turtle t) {
    	SwingUtilities.invokeLater(new Runnable(){
    		public void run(){
    			turtles.add(t);
    		}
    	});
    }

    public Graphics makePen() {
        return bimg.createGraphics();
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(bimg, 0, 0, this);
        
        for(Turtle t : turtles){
        	t.paint(g);
        }
    }
}

public class Turtle {
    static final int TURTLE_SIZE = 5;
    static final int SLOW_INTERVAL = 100;
    static int interval = SLOW_INTERVAL;

    private static final double STRIDE = 5.0;
    private static Pond pond = null;

    private Graphics pen;
    private double xpos, ypos;
    private int direction;
    private boolean penIsDown;
    private Color penColor;

    Rectangle clipRegion = null;
    
    private static synchronized void makePond() {
        if (pond == null)
            pond = new Pond();
    }

    public Turtle() {
        makePond();
        pen = pond.makePen();
        xpos = ypos = 0.0;
        direction = 0;
        penIsDown = false;
        penColor = Color.blue;
        pond.addTurtle(this);
    }
    
    private void setClip(int x0, int y0, int margin) {
        Rectangle r = new Rectangle(x0 - margin, y0 - margin,
                                    margin * 2, margin * 2);
        if (clipRegion == null)
            clipRegion = r;
        else
            clipRegion.add(r);
    }

    private void partlyRepaint() {
        if (clipRegion != null)
        	pond.repaint(clipRegion);
        else
        	pond.repaint();
        
        clipRegion = null;
    }

    private void repaint() {
        pond.repaint();
    }

    void paint(Graphics g) {
        g.setColor(Color.black);
        g.drawOval((int)xpos - TURTLE_SIZE, (int)ypos - TURTLE_SIZE,
                   TURTLE_SIZE * 2, TURTLE_SIZE * 2);
    }

    public void penDown() { penIsDown = true; }

    public void penUp() { penIsDown = false; }

    public boolean isDown() { return penIsDown; }

    public void setColor(Color c) { penColor = c; }

    public void setDirection(double d) { direction = (int)d; }

    public void setDirection(int d) { direction = d; }

    public void rotate(int r) {
        direction = (direction + r) % 360;
    }

    public void rotate(double r) { rotate((int)r); }

    public void go(int distance) {
        go((double)distance);
    }

    public void go(double distance) {
        double x = xpos;
        double y = ypos;
        if (direction == 0)
            x += distance;
        else if (direction == 90)
            y -= distance;
        else if (direction == 180)
            x -= distance;
        else if (direction == 270)
            y += distance;
        else {
            double r = direction * Math.PI * 2.0 / 360.0;
            x = xpos + distance * Math.cos(r);
            y = ypos - distance * Math.sin(r);
        }

        move(x, y);
    }

    public void move(int x, int y) {
        move((double)x, (double)y);
    }

    public void move(double x, double y) {
        if (penIsDown) {
            pen.setColor(penColor);
            double x2 = xpos - x;
            double y2 = ypos - y;
            int step;
            if (interval > 0) {
                step = (int)(Math.sqrt(x2 * x2 + y2 * y2) / STRIDE);
                if (step < 2)
                    step = 2;
            }
            else
                step = 1;

            for (int i = step - 1; i >= 0; --i) {
                double xx = x + x2 * i / step;
                double yy = y + y2 * i / step;
                setClip((int)xpos, (int)ypos, TURTLE_SIZE + 2);
                setClip((int)xx, (int)yy, TURTLE_SIZE + 2);
                pen.drawLine((int)xpos, (int)ypos, (int)xx, (int)yy);
                xpos = xx;
                ypos = yy;
                partlyRepaint();
                if (i > 0 && interval > 0)
                    try {
                        Thread.sleep(interval);
                    }
                    catch (InterruptedException e) {}
            }
        }
        else
            if (interval > 0)
                try {
                    Thread.sleep(interval / 2);
                }
                catch (InterruptedException e) {}

        setClip((int)xpos, (int)ypos, TURTLE_SIZE + 2);
        xpos = x;
        ypos = y;
        setClip((int)x, (int)y, TURTLE_SIZE + 2);
        partlyRepaint();
    }

    public void print(String text) {
        pen.setColor(penColor);
        pen.drawString(text, (int)xpos, (int)ypos);
        repaint();
    }
}

