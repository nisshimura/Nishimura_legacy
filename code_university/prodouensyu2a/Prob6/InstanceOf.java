class S {
}

class T extends S {
}

public class InstanceOf {
	public static void main(String[] args) {
		System.out.println("a) " + ((new S()) instanceof S));
		System.out.println("b) " + ((new S()) instanceof T));
		System.out.println("c) " + ((new T()) instanceof S));
		System.out.println("d) " + ((new T()) instanceof T));
		System.out.println("e) " + ((new S()) instanceof Object));
		System.out.println("f) " + ((new T()) instanceof Object));			
	}
}