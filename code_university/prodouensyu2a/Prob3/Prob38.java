public class Prob38 {
    public static void main(String[] args) {
        MyPoint38 p = new MyPoint38();
        MyPoint38 q = new MyPoint38();
        p.setPoint(20, 22);
        q.setPoint(4, 22);

        System.out.println(p.getDistanceFrom(q));
    }
}
