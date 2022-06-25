import java.io.*;
import java.nio.charset.*;
import java.nio.file.*;
import java.util.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Pattern;

import javax.swing.text.AbstractDocument.BranchElement;

public class C {
    public static boolean is_num(String text) {
        Pattern pattern = Pattern.compile("^[0-9]+$|-[0-9]+$");
        return pattern.matcher(text).matches();
    }

    public static void main(String[] args) {
        try {
            List<String> list = Files.readAllLines(Paths.get("input.txt"), Charset.defaultCharset());
            BufferedWriter output = Files.newBufferedWriter(Paths.get("output.txt"), Charset.defaultCharset());

            for (Iterator<String> line = list.iterator(); line.hasNext();) {
                List<String> txt = Arrays.asList(line.next().split(""));
                String out = "";
                Boolean flag = true;
                List<String> txt_list = new ArrayList<String>();

                while (txt.contains("(")) {
                    System.out.println(txt.toString());
                    for (int i = 0; i < txt.size(); i++) {
                        int now = 0;
                        if (txt.get(i).equals("(")) {
                            int num = 0;
                            for (int j=i;j<txt.size();j++) {     
                                System.out.println(txt.get(j));        
                                if (txt.get(j).equals("(")) {
                                    break;
                                } else if (txt.get(j).equals(")")) {
                                    System.out.println("kooooo");
                                    flag = false;
                                    for (int k = i + 1; k < j; k++) {
                                        boolean purasu = true;
                                        if (C.is_num(txt.get(k)) && purasu) {
                                            num += Integer.valueOf(txt.get(k));
                                        } else if (C.is_num(txt.get(k))) {
                                            num -= Integer.valueOf(txt.get(k));
                                        } else {
                                            if (txt.get(k).equals("-")) {
                                                purasu = false;
                                            } else if (txt.get(k).equals("+")) {
                                                purasu = true;
                                            } else {
                                                System.out.println("invalid input!!!");
                                            }
                                        }
                                        now = k;
                                    }
                                    
                                }
                            }
                            if (flag == false) {
                                txt_list.add(String.valueOf(num));
                            } else {
                                txt_list.add(txt.get(i));
                            }
                            System.out.println(txt_list.toString());
                        }
                    }
                }

                output.write(out);
                if (line.hasNext())
                    output.newLine();
            }
            output.close();
        } catch (IOException e) {
            System.err.println("IOException " + e.toString());
        }
    }
}