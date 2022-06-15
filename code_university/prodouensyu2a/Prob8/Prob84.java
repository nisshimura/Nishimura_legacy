public class Prob84 {
	public static void main(String[] args) throws Exception {
        Object x[] = new Integer[5];
        try{
            x[0] = "a";
        }
        catch (Exception arrayStoreException){
            System.out.println("Array Store Exception caught!!!");
        }
	}
}
