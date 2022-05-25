class Prob67{
    public static String[] japanese={"ichi","ni","san","shi","go"};
    public static String[] english = {"one", "two", "three", "four", "five"};
    public static int[] number ={1,2,3,4,5};

    public int chk(String s,int index){
        for (int i=0;i<5;i++){
            
            if (english[i].equals(s)){
                System.out.println(i+" : "+" "+s+" "+japanese[i]+ " "+number[i]);
                return number[i];
            }
        }
        System.out.println(index + " : " +s+" is not allowed");
        return 0;
    }

    public static void main(String[] args) {
        Prob67 p = new Prob67();
        int sum = 0;
        for (int j=0;j<args.length;j++){
            int a = p.chk(args[j],j);
            if (a!=0){
                sum += a;
            }
        }
        System.out.println("the Sum is "+ sum);
    }

    
} 