import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.lang.Math;

public class Prob104 {
    public static void main(String[] args) {
        File file1 = new File("input1041.txt");
        File file2 = new File("input1042.txt");

        ArrayList<ArrayList<String>> input2 = new ArrayList<ArrayList<String>>();
        ArrayList<ArrayList<String>> input1 = new ArrayList<ArrayList<String>>();

        try (BufferedReader br = new BufferedReader(new FileReader(file1))) {
            String line = null;
            while ((line = br.readLine()) != null) {
                ArrayList<String> tmp1 = new ArrayList<String>();
                if (line.isEmpty()) {
                    tmp1.add("NULL");
                }

                else {
                    String[] nums = line.split(",");
                    for (String num : nums) {
                        if (num.isEmpty()) {
                            tmp1.add("0");
                        } else {
                            tmp1.add(num);
                        }
                    }
                }
                input1.add(tmp1);
            }
        } catch (FileNotFoundException e) {
            System.out.println("file input error");
        } catch (IOException e) {
            System.out.println("error is occured");
        }

        try (BufferedReader br = new BufferedReader(new FileReader(file2))) {
            String line = null;
            while ((line = br.readLine()) != null) {
                ArrayList<String> tmp2 = new ArrayList<String>();
                if (line.isEmpty()) {
                    tmp2.add("NULL");
                }
                else {
                    String[] nums = line.split(",");
                    for (String num : nums) {
                        if (num.isEmpty()) {
                            tmp2.add("0");
                        } else {
                            tmp2.add(num);
                        }
                    }
                }
                input2.add(tmp2);
            }
        } catch (FileNotFoundException e) {
            System.out.println("file input error");
        } catch (IOException e) {
            System.out.println("error is occured");
        }
        System.out.println(input1);
        System.out.println(input2);

        ArrayList<ArrayList<String>> output = new ArrayList<ArrayList<String>>();
        for (int i=0;i<Math.max(input1.size(),input2.size());i++){
            ArrayList<String> tmp = new ArrayList<String>();
            if (input1.get(i).get(0).equals("NULL")){
                for (int j=0;j<input2.get())
            }
            else if (input2.get(i).get(0).equals("NULL")){

            }
            else{

            }
        }
    }

}
