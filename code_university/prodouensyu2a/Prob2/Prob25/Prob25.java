public class Prob25 {
    public static void main(String[] args){
        MyPoint p = new MyPoint();
        MyPoint q = new MyPoint();

        p.x = 20;
        p.y = 20;

        q.x = 4;
        q.y = 15;

        double d = p.getDistance();
        double dq = q.getDistance();

        System.out.println("p is " +d+" far from the origin");
        System.out.println("q is "+dq+" far from the origin");
    }
}
