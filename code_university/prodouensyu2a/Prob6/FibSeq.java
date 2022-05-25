public class FibSeq {
	public static void printFibs(Printer p, int num) {
		for (int i = 0; i < num; i++)
			p.print(fib(i));
	}
	public static int fib(int n) {
		if (n > 1)
			return fib(n - 1) + fib(n - 2);
		else
			return 1;
	}
	public static void main(String[] args) {
		printFibs(new PrettyPrinter(), 20);
		printFibs(new SimplePrinter(), 20);		
	}
}
