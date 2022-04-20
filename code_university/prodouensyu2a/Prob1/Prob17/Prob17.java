public class Prob17 {
    public static void main(String[] args){
        for (int i=1;i<41;i++){
            if (i%3==0&&i%4==0){
                System.out.println("TripQuad");
            }
            else if(i%3==0){
                System.out.println("Trip");
            }
            else if(i%4==0){
                System.out.println("Quad");
            }
            else{
                System.out.println(i);
            }
        }
    }
}
