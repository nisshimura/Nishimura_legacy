public class TriangleVertex extends Vertex{
    void draw(Turtle t){
        int kaku = 3;
        int hen = 20;
        int naikaku=120;
        t.penDown();
        t.go(hen);
        for (int j=0;j<kaku-1;j++){
            t.rotate(naikaku);
            t.go(hen);
        }
        t.rotate(naikaku);
}
}
