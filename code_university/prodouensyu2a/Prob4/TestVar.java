public class TestVar {
	int cnt1 = 5;
	static int cnt2 = 5;

	void dec1() {
		cnt1--;
	}

	static void dec2() {
		cnt2--;
	}

	void show() {
		System.out.println("cnt1 = " + cnt1 + ", cnt2 = " + cnt2);
	}

	public static void main(String[] args) {
		TestVar v1 = new TestVar();
		TestVar v2 = new TestVar();
		System.out.println("(a)");
		v1.show();
		v2.show();
		v1.dec1();
		System.out.println("(b)");
		v1.show();
		v2.show();
		dec2();
		System.out.println("(c)");
		v1.show();
		v2.show();
	}
}
