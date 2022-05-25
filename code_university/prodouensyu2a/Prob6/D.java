public class D extends A implements IX, IY {
	public void showMessage() {
		System.out.println("D is called");
	}
	public void show() {
		System.out.println("D is shown");
		IY.super.show();
	}
}
