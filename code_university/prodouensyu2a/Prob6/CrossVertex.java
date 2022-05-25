public class CrossVertex extends Vertex{
    void draw(Turtle t){
        t.penDown();
        t.go(5);
        t.go(-10);
        t.go(5);
        t.rotate(90);
        t.go(5);
        t.go(-10);
        t.go(5);
        t.rotate(-90);
    }
}
