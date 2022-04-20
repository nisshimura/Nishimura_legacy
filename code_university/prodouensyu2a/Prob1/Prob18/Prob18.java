import javax.swing.text.StyledEditorKit;

public class Prob18 {
    public static void main(String[] args){
        int n=5;
        int steps=0;
        System.out.println(steps + " : " + n);
        while(n!=1){
            if (n%2==0){
                n = n/2;
            }
            else{
                n = n*3+1;
            }
            System.out.println(++steps + " : " + n);
        }
        System.out.println("Steps : "+ steps);
    }
}
