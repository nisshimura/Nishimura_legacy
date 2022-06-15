public class Prob76 {
    public boolean is_selfnum(String[] s){
        int[] num_ar=new int[10];
        for (int i=0;i<s.length;i++){
            num_ar[Integer.valueOf(s[i])]++;
        }
        for (int i=0;i<s.length;i++){
            if (Integer.valueOf(s[i])!=num_ar[Integer.valueOf(i)]){
                System.out.println("break");
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args){
        Prob76 p = new Prob76();
        String s = args[0];
        String[] s_ar = s.split("");
        if (p.is_selfnum(s_ar)){
            System.out.println("true");
        }
        else{
            System.out.println("false");
        }
    }
}
