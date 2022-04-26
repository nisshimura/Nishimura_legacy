public class IntSetUser {
	public static void main(String[] args) {
		IntSet s = new IntSet();
		s.init();
		System.out.println("count = " + s.count());
		s.add(4); s.add(1); s.add(6); s.add(4); s.add(3); s.add(5);
		System.out.println("1: " + s.find(1));
		System.out.println("2: " + s.find(2));
		System.out.println("3: " + s.find(3));
		System.out.println("4: " + s.find(4));
		System.out.println("5: " + s.find(5));
		System.out.println("count = " + s.count());
		System.out.println("Index for 3: " + s.getIndex(3));
		System.out.println("Index for 4: " + s.getIndex(4));
		s.remove(4);
		System.out.println("1: " + s.find(1));
		System.out.println("2: " + s.find(2));
		System.out.println("3: " + s.find(3));
		System.out.println("4: " + s.find(4));
		System.out.println("5: " + s.find(5));
		System.out.println("count = " + s.count());
		System.out.println("Index for 3: " + s.getIndex(3));
		System.out.println("Index for 4: " + s.getIndex(4));
	}
}