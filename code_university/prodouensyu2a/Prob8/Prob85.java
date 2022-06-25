import java.util.ArrayList;

public class Prob85 {
    public  ArrayList<Byte> alpha_notin(ArrayList<Byte> byte1){
        ArrayList<Byte> result = new ArrayList<Byte>();
        for(byte i=97;i<123;i++){
            result.add(i);
        }
        for(int i=0;i<byte1.size();i++){
            result.remove(byte1.get(i));
        }
        return result;
    }
    public static class InvalidInputException extends Exception{
        private static final long serialVersionUID = 1L;
        public InvalidInputException(String msg){
            super(msg);
        }
    }
    
    public static void main(String[] args) throws InvalidInputException{
        ArrayList<Byte> group = new ArrayList<Byte>();

        if(args.length==0){
            throw new InvalidInputException("Invalid Input");
        }
        for (int i=0;i<args.length;i++){
            if(args[i].matches(".*[0-9].*")){
                throw new InvalidInputException("Invalid Input");
            }
        }
        for (int i=0;i<args.length;i++){
            byte[] byte1 = args[i].getBytes();
            for (int k=0;k<byte1.length;k++){
                if (!group.contains(byte1[k])){
                    group.add(byte1[k]);
                }
            }
        }   
        Prob85 p = new Prob85();
        ArrayList<Byte> result = p.alpha_notin(group);
        
        
        if (result.size()==0){
            System.out.println("true");
        }
        else{
            System.out.println("false");
            for (int i=0;i<result.size();i++){
                byte a = result.get(i);
                char character = (char) a;
                System.out.print(character +" ");
            }
        }
    }
}
