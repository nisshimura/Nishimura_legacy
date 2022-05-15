public class test {
    private int x;
    protected int y;

    void check(test a) {
        x = 1; // (1)
        a.x = 2; // (2)
        y = 3; // (3)
        a.y = 4; // (4)
    }
}


public class myname extends test {
    void check(test a, B b) {
        x = 5; // (5)
        a.x = 6; // (6)
        b.x = 7; // (7)
        y = 8; // (8)
        a.y = 9; // (9)
        b.y = 10; // (10)
    }
}
