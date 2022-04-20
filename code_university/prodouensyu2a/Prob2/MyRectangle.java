public class MyRectangle {
    MyPointNew point1,point2;
    void setPoints(int x1,int y1,int x2,int y2){

        point1 = new MyPointNew();
        point2 = new MyPointNew();
        
        point1.x = x1;
        point1.y = y1;
        point2.x = x2;
        point2.y = y2;
    }
    int computeLength(){
        return Math.abs(point1.x - point2.x);
    }
    int computeWidth(){
        return Math.abs(point1.y - point2.y);
    }
    int computeArea(){
        return computeLength()*computeWidth();
    }
    int computeCircumference(){
        return computeLength()*2+computeWidth()*2;
    }
    
}
