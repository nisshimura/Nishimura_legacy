public class DialogTest {
    public static void main(String[] args) {
    String text = javax.swing.JOptionPane.showInputDialog(null);
    switch(text){
        case "1" :
            System.out.println("freshman");
            break;
        case "2" :
            System.out.println("sophomore");
            break;
        case "3" :
            System.out.println("junior");
            break;
        case "4" :
            System.out.println("senior");
            break;
        default :
            System.out.println("Unknown");
    }   
    }
}