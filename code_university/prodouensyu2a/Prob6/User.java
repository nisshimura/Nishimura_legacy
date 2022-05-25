public class User {
	public static void testClass(A a) {
		a.showMessage();
	}
	
	public static void testInterface(IX i) {
		i.showMessage();
		i.show();
	}
	
	public static void main(String[] args) {
		A a = new A();
		B b = new B();
		C c = new C();
		D d = new D();
		
		testClass(a);
		testClass(b);
		testClass(d);
		testInterface(c);
		testInterface(d);
	}
}
