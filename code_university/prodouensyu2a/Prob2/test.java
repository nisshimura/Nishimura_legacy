public class test { public static void main(String[] args) {
    Turtle t;
    t = new Turtle();
    t.move(100,100);
    int kaku = 4;
    int hen = 20;
    int naikaku=360/kaku;
    t.penDown();
    t.go(hen);
    for (int j=0;j<kaku-1;j++){
        t.rotate(naikaku);
        t.go(hen);
    }  
    t.penUp();
}
}