import java.util.*;

class Prob91 {
    static int sum = 0;
    private void processInput(String inString) {this.sum+=Integer.valueOf(inString);}

    public static void main(String[] args) {
    Prob91 app = new Prob91();
    Scanner scan = new Scanner(System.in);
    System.out.println("Please input numbers:");
    while (true) {
        String str = scan.next();
        if (str.equals("end")||str.equals("quit")){System.out.println(app.sum);return;}
        app.processInput(str);
    }
    }
}