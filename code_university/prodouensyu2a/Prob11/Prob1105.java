import java.lang.Math;
public class Prob1105 {
    public boolean isAble(String s){
        boolean isNumeric = s.matches("[+-]?\\d*(\\.\\d+)?");
        boolean isOK = false;
        if (s.length()==1 || s.charAt(0)!='0'){
            isOK = true;
        }
        return isNumeric&&isOK;
    }
    public String get_u_1000(int num){
        String text = "";
        if (num>=100){
            switch ((int)(num/100)){
                case 1:
                    text += "one";
                    break;
                case 2:
                    text += "two";
                    break;
                case 3:
                    text += "three";
                    break;
                case 4:
                    text += "four";
                    break;
                case 5:
                    text += "five";
                    break;
                case 6:
                    text += "six";
                    break;
                case 7:
                    text += "seven";
                    break;
                case 8:
                    text += "eight";
                    break;
                case 9:
                    text += "nine";
                    break;
            }
            text +=  " hundred ";
            num -= (int)(num/100)*100;
        }
        if (num >= 20) {
            switch ((int) (num / 10)) {
                case 2:
                    text += "twenty";
                    break;
                case 3:
                    text += "thrity";
                    break;
                case 4:
                    text += "fourty";
                    break;
                case 5:
                    text += "fifty";
                    break;
                case 6:
                    text += "sixty";
                    break;
                case 7:
                    text += "seventy";
                    break;
                case 8:
                    text += "eighty";
                    break;
                case 9:
                    text += "ninety";
                    break;
            }
            num -= (int) (num / 10)*10;
            if (num!=0) {
                text += "-";
            }
        }
        
        switch ((int) num) {
            case 0:
                text += "zero";
                break;
            case 1:
                text += "one";
                break;
            case 2:
                text += "two";
                break;
            case 3:
                text += "three";
                break;
            case 4:
                text += "four";
                break;
            case 5:
                text += "five";
                break;
            case 6:
                text += "six";
                break;
            case 7:
                text += "seven";
                break;
            case 8:
                text += "eight";
                break;
            case 9:
                text += "nine";
                break;
            case 10:
                text += "ten";
                break;
            case 11:
                text += "eleven";
                break;
            case 12:
                text += "twenteen";
                break;
            case 13:
                text += "thrteen";
                break;
            case 14:
                text += "fourteen";
                break;
            case 15:
                text += "fifteen";
                break;
            case 16:
                text += "sixteen";
                break;
            case 17:
                text += "seventeen";
                break;
            case 18:
                text += "eighteen";
                break;
            case 19:
                text += "nineteen";
                break;
        }
        return text;
    }
    public String getmoji(long num){
        String text = "";
        
        if (num>=Math.pow(10, 12)){
            text += get_u_1000((int)(num/ Math.pow(10, 12)))+" trillion ";
            num -= (int) (num / Math.pow(10, 12)) * Math.pow(10, 12);
        }
        if (num >= Math.pow(10, 9)) {
            text += get_u_1000((int) (num / Math.pow(10, 9))) + " billion ";
            num -= (int) (num / Math.pow(10, 9)) * Math.pow(10, 9);
        }
        
        if (num >= Math.pow(10, 6)) {
            text += get_u_1000((int) (num / Math.pow(10, 6))) + " million ";
            num -= (int) (num / Math.pow(10, 6)) * Math.pow(10, 6);
        }
        
        if (num >= Math.pow(10, 3)) {
            text += get_u_1000((int) (num / Math.pow(10, 3))) + " thousand ";
            num -= (int) (num / Math.pow(10, 3)) * Math.pow(10, 3);
        }
        
        text += get_u_1000((int)num);
        return text;
    }
    public static void main(String[] args) {
        Prob1105 a = new Prob1105();
        // if (a.isAble(args[0])){
        //     System.out.println(a.getmoji(integer.valueOf(args[0])));
        // }
        // else{
        //     System.out.println("ERROR!!");
        // }
        System.out.println(a.getmoji(Long.valueOf("999999999")));

    }
}
