public class Prob102 {
    public static void main(String[] args) {
        // Light al = new Light();
        // al.on();

        (new Object(){void on(){System.out.println("Turn it on!!");}}).on();
    }
}

// class Light {
//     public void on() { System.out.println("Turn it on!"); }
// }