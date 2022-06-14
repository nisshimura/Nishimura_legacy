public class Throw2 {
	public static void methodA(String program) throws Exception {
		if (program.equals("Smalltalk"))
			throw new Exception("I don't know Smalltalk!");
		System.out.println("Program = " + program);
	}
	public static void main(String[] args) {
		try {
			methodA("Java");
			System.out.println("OK! Let's program!");
			methodA("Smalltalk");
			System.out.println("The end");
		}
		catch (Exception e) {
			System.out.println(e.getMessage());
		}
		System.out.println("The actual end");
	}
}
