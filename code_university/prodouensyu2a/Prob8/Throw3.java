public class Throw3 {
	public static void methodA(String program) throws Exception {
		try {
			if (program.equals("Smalltalk"))
				throw new Exception("I don't know Smalltalk!");
		}
		finally {
			System.out.println("The finally program is " + program);
		}			
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
