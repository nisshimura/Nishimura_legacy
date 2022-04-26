public class MyPoint38 {
	private int x;
	private int y;

	void setPoint(int xpos, int ypos) {
		x = xpos;
		y = ypos;
	}

	int getX() {
		return x;
	}

	int getY() {
		return y;
	}

	double getDistance() {
		return Math.sqrt(x*x + y*y);
	}
    double getDistanceFrom(MyPoint38 p){
        double d = Math.pow(Math.pow(x-p.x,2)+Math.pow(y-p.y,2),0.5);
		return d;
    }
}

