public class MyPointNew {
    int x, y; 
    double getDistance() { return Math.sqrt(x * x + y * y);}
    void setPoint(int sx,int sy){
        x = sx;
        y = sy;
    }
    void printCoord(){
        System.out.println("("+x+","+y+")");
    }
        
}
