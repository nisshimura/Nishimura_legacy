public class PrettyPrinter implements Printer{
	protected int counter = 0;
	public void print(int i) {
		System.out.print(i);
		if (++counter < 6) {
			System.out.print("  ");
		} else {
			System.out.println();
			counter = 0;
		}
	}
}
