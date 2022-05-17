public class MyVector {
    private double [] elements;
    static int count;

    public MyVector(double x,double y){
        elements = new double[2];
        elements[0]=x;
        elements[1]=y;

        count++;
    }
    boolean isEqual(MyVector v){
        return v.elements[0]==elements[0]&&v.elements[1]==elements[1];
    }   
    static int getNumVec(){
        return count;
    }
    void print(){
        System.out.println("("+elements[0]+","+elements[1]+")");
    }
}