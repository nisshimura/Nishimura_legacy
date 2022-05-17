public class MyVectorUser {
    public static void main(String[] args) {
        MyVector v1 = new MyVector(5, 6);
        MyVector v2 = new MyVector(20, 22);
        MyVector v3 = new MyVector(20, 22);
        System.out.println("Number of MyVector instances is " + MyVector.getNumVec());
        System.out.println(v1);
        System.out.println(v2);
        if (v1==v2) {
                System.out.println("V1 and v2 are the same!");
                v1.print();
        } else {
                System.out.println("V1 and v2 are different!");
                v1.print();
                v2.print();
        }
        if (v2.isEqual(v3)) {
                System.out.println("V2 and v3 are the same!");
                v2.print();
        } else {
                System.out.println("V2 and v3 are different!");
                v2.print();
                v3.print();
        }
}
}
