public class Prob210 {
    public static void main(String[] args){
        MyRectangle square;
        square = new MyRectangle();
        int x1 = 20, y1 = 22, x2=4, y2=15;
        square.setPoints(x1, y1, x2, y2);

        int s = square.computeArea();
        int l = square.computeCircumference();

        System.out.println("The area of the rectangle is " + s + ",and the circumference is "+l);
    }
}
