public class Throw4 {

	public static void main(String[] args) {
		try {
			System.out.println("Before a");
			a();
			System.out.println("After a");
		}
		catch (NumberFormatException e) {
			System.out.println("main: " + e);
		}
		finally {
			System.out.println("main: finally");
		}
	}
	
	public static void a() {
		try {
			System.out.println("Before b");
			b();
			System.out.println("After b");
		}
		catch (NumberFormatException e) {
			System.out.println("a: " + e);
		}
		finally {
			System.out.println("a: finally");
		}
	}

	public static void b() {
		try {
			System.out.println("Before c");
			c();
			System.out.println("After c");
		}
		catch (ArithmeticException e) {
			System.out.println("b: " + e);
		}
		finally {
			System.out.println("b: finally");
		}
	}
	
	public static void c() {
		try {
			Integer i = Integer.valueOf("6.19");
		}
		catch (NumberFormatException e) {
			throw e;
		}
		finally {
			System.out.println("c: finally");
		}
	}

}
