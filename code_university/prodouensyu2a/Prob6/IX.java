public interface IX {
	void showMessage();
	
	default void show() {
		System.out.println("IX is shown");
	}
}
