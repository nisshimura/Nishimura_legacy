class A {
 void methodA() { System.out.println("A"); }
}


class B extends A {
 void methodB() { System.out.println("B"); }
}


public class Prob55 {
    public static void main(String[] args) {
        B b = new A();
    }
}
