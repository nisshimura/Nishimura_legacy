import java.io.*;
import java.nio.charset.*;
import java.nio.file.*;
import java.util.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
public class Prob94 {
public static void main(String[] args) {
    try {
    List<String> list = Files.readAllLines(Paths.get("message.txt"), Charset.defaultCharset());
    BufferedWriter output = Files.newBufferedWriter(Paths.get("output94.txt"),Charset.defaultCharset());
    
    for (Iterator<String> line = list.iterator(); line.hasNext(); ) {
        String [] txt = line.next().split(" ");
        String out="";
        for (int i=txt.length-1;i>=0;i--){
            out = out + txt[i]+" ";
            
        }
        output.write(out);
        if (line.hasNext())
            output.newLine();
    }
    output.close();
    } catch(IOException e) {
    System.err.println("IOException " + e.toString());
    }
    }
}