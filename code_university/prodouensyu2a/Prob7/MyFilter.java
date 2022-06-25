
import java.util.ArrayList;
import java.util.Random;
public class MyFilter {
    public ArrayList<ArrayList<Integer>> make_pairs(ArrayList<Integer> lonly){
        ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();

        for (int i=0,j=0;i<lonly.size()/2;i++,j=j+2){
            ArrayList<Integer> tmp = new ArrayList<Integer>();
            tmp.add(lonly.get(j));
            tmp.add(lonly.get(j+1));
            list.add(tmp);
        }
        return list;
    }
    // public int[][] compare_del(int[][] array){
        
    //     int num = 0;
    //     for (int i = 0; i < array.length; i++) {

    //         if (array[i][0] > array[i][1]) {
    //             num++;
    //         }
    //     }
    //     int[][] strong = new int[num][2];
    //     int flag =0; 
    //     for (int i=0;i<array.length;i++){
            
    //         if (array[i][0]>array[i][1]){
    //             strong[flag][0] = array[i][0];
    //             strong[flag][1] = array[i][1];
    //             flag++;
    //         }
    //     }
    //     return strong;
    // }
    public ArrayList<ArrayList<Integer>> compare_del(ArrayList<ArrayList<Integer>> array){
        ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
        
        for (int i = 0; i < array.size(); i++){
            if (array.get(i).get(0) > array.get(i).get(1)){
                list.add(array.get(i));
            }
        }
        return list;
    }
    public static void main(String[] args){
        ArrayList<Integer> lonly = new ArrayList<Integer>();
        int num = 0;
        if (args.length==0){
            System.out.println("No numbers!!");
            return;
        }
        num = Integer.valueOf(args[0]);
        if (num==0){
            System.out.println("Not valid!!");
            return;
        }
        Random ran = new Random();
        int[] nums = new int[num];
        for (int i = 0; i < num; i++) {
            int tmp = ran.nextInt(10);
            nums[i]=tmp;
            System.out.print(tmp);
        }

        System.out.print("\n");
        for (int i=0;i<num;i++){
            lonly.add(nums[i]);
        }
        MyFilter m  = new MyFilter();
        ArrayList<ArrayList<Integer>> pairs = m.make_pairs(lonly);
        ArrayList<ArrayList<Integer>> list = m.compare_del(pairs);
        
        if (list.size()!=0){
            for (int i = 0; i < list.size(); i++) {
                System.out.print(list.get(i).get(0));
                System.out.print(list.get(i).get(1));
            }
            
        }
    }
}
