public class Prob28 { public static void main(String[] args) {
    Turtle t;
    t = new Turtle();
    t.move(10, 200);
    t.penDown();
    for (int index=0;index<20;index++)
    {
        int dis = 150-(index*5);
        t.go(dis);
        t.rotate(90);
    }
    
    }
}