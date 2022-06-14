public class Throw5 {
	public static void main(String[] args) {
		try {
			System.out.println(5/0);
		} catch (Exception e) {
			System.err.println("Exception caught!");
		} catch (ArithmeticException e) {
			System.err.println("NullPointerException caught!");
		}
	}
}
