import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

import java.lang.Math;
import java.io.FileWriter;
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

        ArrayList<ArrayList<Integer>> output = new ArrayList<ArrayList<Integer>>();
        
        for (int i=0;i<Math.min(input1.size(),input2.size());i++){
            ArrayList<Integer> tmp = new ArrayList<Integer>();
            
            if (input1.get(i).size()==input2.get(i).size()){
                
                for (int j=0;j<input1.get(i).size();j++){
                    tmp.add(Integer.valueOf(input1.get(i).get(j))*Integer.valueOf(input2.get(i).get(j)));
                }
            }
            else{
                if (input1.get(i).get(0).equals("NULL")){
                    for (int j=0;j<input2.get(i).size();j++){
                        tmp.add(0);
                    }
                }
                else if (input2.get(i).get(0).equals("NULL")){
                    
                    for (int j=0;j<input1.get(i).size();j++){
                        tmp.add(0);
                    }
                }
                else if (input1.get(i).size()!=input2.get(i).size()){
                    for (int j=0;j<Math.min(input1.get(i).size(),input2.get(i).size());j++){
                        tmp.add(Integer.valueOf(input1.get(i).get(j))*Integer.valueOf(input2.get(i).get(j)));
                    }
                    for (int j=Math.min(input1.get(i).size(),input2.get(i).size());j<Math.max(input1.get(i).size(),input2.get(i).size());j++){
                        tmp.add(0);
                    }
                }
            }
            output.add(tmp);
        }

        for(int i=Math.min(input1.size(), input2.size());i<Math.max(input1.size(), input2.size());i++){
            ArrayList<Integer> tmp = new ArrayList<Integer>();
            if (!input1.get(i).isEmpty()){
                for (int j=0;j<input1.get(i).size();j++){
                    tmp.add(0);
                }
            }
            else if (!input2.get(i).isEmpty()){
                for (int j=0;j<input2.get(i).size();j++){
                    tmp.add(0);
                }
            }
            output.add(tmp);
        }
        try{
            File out = new File("output1041.txt");
            FileWriter out_file = new FileWriter(out);
            for (int i=0;i<output.size();i++){
                for (int j=0;j<output.get(i).size();j++){
                    out_file.write(String.valueOf(output.get(i).get(j)));
                    if (j!=output.get(i).size()-1){
                        out_file.write(",");
                    }
                }
                out_file.write("\n");
            }
            out_file.close();
          }catch(IOException e){
            System.out.println(e);
          }
        
    }

}
