public class Caesar {
    public byte[] anngou(String s,int k){
            byte[] byte1 = s.getBytes();
            byte[] buf = new byte[byte1.length];
            for (int i=0;i<byte1.length;i++){
                
                int num = ((byte1[i]-97)+k+26)%26;
                buf[i] = (byte)(num+97);
            }
            return buf;
        }

    public byte[] hukugou(String s,int k) {
            byte[] byte1 = s.getBytes();
            byte[] buf = new byte[byte1.length];
            for (int i = 0; i < byte1.length; i++) {
                int num = ((byte1[i] - 97) - k + 26) % 26;
                buf[i] = (byte) (num + 97);
            }
            return buf;
        }
    public static void main(String[] args){
        Caesar c = new Caesar();
        String convert="a",all="a";
        for (int i=2;i<args.length;i++){
            convert = args[i];
        
            if (args[0].equals("true")){
                convert = new String(c.anngou(convert, (Integer.valueOf(args[1]))%26));
            }
            else if (args[0].equals("false")){
                convert = new String(c.hukugou(convert, (Integer.valueOf(args[1]))%26));
            }
            if (i==2){
                all = convert;
            }
            else{
                all += " "+convert;
            }        
        }   
        System.out.println(all);
   }
}

