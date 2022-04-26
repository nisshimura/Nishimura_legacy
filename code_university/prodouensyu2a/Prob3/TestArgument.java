public class TestArgument {
	int change1(int x) {
		x += 4;
		return x;
	}

	void change2(int x) {
		x++;
	}

	void changePoint1(MyPoint p) {
		p = new MyPoint();
		p.setPoint(2, 2);
	}

	void changePoint2(MyPoint p) {
		p.setPoint(2, 2);
	}

	void changeArray1(int[] a) {
		a[0] = 20;
	}

	public static void main(String[] args) {
		TestArgument testArgument = new TestArgument();

		int x = 4;
		System.out.println("(1) x = " + x);

		x = testArgument.change1(x);
		System.out.println("(2) x = " + x);

		testArgument.change2(x);
		System.out.println("(3) x = " + x);

		MyPoint p = new MyPoint();
		System.out.println("(4) p = (" + p.getX() + ", " + p.getY() + ")");

		testArgument.changePoint1(p);
		System.out.println("(5) p = (" + p.getX() + ", " + p.getY() + ")");

		testArgument.changePoint2(p);
		System.out.println("(6) p = (" + p.getX() + ", " + p.getY() + ")");

		int[] a = new int[] {4, 22};
		testArgument.changeArray1(a);
		System.out.println("(7) a[0] = " + a[0]);
		System.out.println("    a[1] = " + a[1]);
	}
}
