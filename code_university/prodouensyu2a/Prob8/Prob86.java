public class Prob86 {
    public static void main(String[] args) {
        if (args.length==0){
            System.out.println("No amount specified");
            return;
        }
        int target = Integer.valueOf(args[0]);
        int conbi=0;
        for (int i=0;i*500<=target;i++)
            for (int j=0;i*500+j*100<=target;j++)
                for (int k=0;i*500+j*100+k*50<=target;k++)
                    for (int l=0;i*500+j*100+k*50+l*10<=target;l++)
                        for (int m=0;i*500+j*100+k*50+l*10+m*5<=target;m++)
                            for (int n=0;i*500+j*100+k*50+l*10+m*5+n*1<=target;n++){
                                int max = i*500+j*100+k*50+l*10+m*5+n*1;
                                if(max==target){
                                    //System.out.println("i"+i+" j"+j+" k"+k+" L"+l+" m"+m+" n"+n);
                                    conbi += 1;
                                }
                            }
        System.out.println(conbi);
            
    }
}
