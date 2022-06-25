import java.util.*;

class Guess {
    static int sum = 0;

    public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    Random rand = new Random();
    int num = rand.nextInt(Integer.valueOf(args[1]))+Integer.valueOf(args[0]);
    System.out.println("Please input numbers:");
    while (true) {
        System.out.print("Enter a number:");
        String str = scan.next();
        if (Integer.valueOf(str)==num){
            System.out.println("That's correct!");
            return;
        }
        if (Integer.valueOf(str)>num){
            System.out.println("Wrong! Too High");
        }
        else if(Integer.valueOf(str)<num){
            System.out.println("Wrong! Too Low");
        }
    }
    }
}