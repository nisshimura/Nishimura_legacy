public class RectVertex extends Vertex{ 
    void draw(Turtle t){
        int kaku = 4;
        int hen = 20;
        int naikaku=360/kaku;
        t.penDown();
        t.go(hen);
        for (int j=0;j<kaku-1;j++){
            t.rotate(naikaku);
            t.go(hen);
        }
        t.rotate(naikaku);
    }
}
