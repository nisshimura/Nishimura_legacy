public class Square {
    void draw(Turtle t,Vertex v){
        for (int i=0;i<4;i++){
            v.draw(t);
            t.penUp();
            t.go(80);
            t.rotate(90);
            
        }
    }
    public static void main(String[] args){
        Square square = new Square();
        Turtle turtle = new Turtle();
        turtle.move(40,180);
        square.draw(turtle,new RectVertex());
        turtle.move(140, 180);
        square.draw(turtle,new CrossVertex());
        turtle.move(110,250);
        square.draw(turtle,new TriangleVertex());

    }
}
