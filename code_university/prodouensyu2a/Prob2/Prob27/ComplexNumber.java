public class ComplexNumber {
    int x, y; 
    void abs(){
        double ab;
        ab = Math.sqrt(Math.pow(x, 2)+Math.pow(y, 2));
        System.out.println("abs is "+ab);
    }
    void print(){
        System.out.println(x + "+" + y+"i");
    }
        
}
