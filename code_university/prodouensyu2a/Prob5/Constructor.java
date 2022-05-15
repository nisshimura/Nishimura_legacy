class SuperClass {
	public SuperClass() {
		System.out.println("SuperClass() called");
	}
	
	public SuperClass(int x) {
		System.out.println("SuperClass(int x = " + x + ") called");
	}
}

public class Constructor extends SuperClass {
	public Constructor() {
		super();
	}
	public Constructor(int x) {
	}
	public Constructor(int x, int y) {
		super(x);
	}
	public Constructor(int x, int y, int z) {
		super();
	}
	public static void main(String[] args) {
		Constructor c1 = new Constructor();
		Constructor c2 = new Constructor(5);
		Constructor c3 = new Constructor(5, 13);
		Constructor c4 = new Constructor(5, 1, 3);		
	}
}