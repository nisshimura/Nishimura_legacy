public class User extends C {
	static void showMessages(String s, A v) {
		System.out.print(s);
		v.m1();
		v.m2();
		v.m3();
		System.out.println();
	}
	public static void main(String[] args) {
		A v1 = new A();
		B v2 = new B();
		C v3 = new C();
		User v4 = new User();
		showMessages("1)", v1);
		showMessages("2)", v2);
		showMessages("3)", v3);
		showMessages("4)", v4);
	}
}
