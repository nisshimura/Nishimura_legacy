public class Car {
	protected int num;
	protected double gas;
	protected int speed;
	protected double fuelEff;

	public Car() {
		System.out.println("Made a new Car instance");	
	}
	
	public Car(int newNum, double newFuelEff) {
		num = newNum;
		gas = 0.0;
		speed = 0;
		fuelEff = newFuelEff;
		System.out.println("Made a new Car instance");	
		System.out.println("Set number to " + num + " and fuel efficiency to " + fuelEff);
	}
	
	public void setCar(int newNum, double newFuelEff) {
		num = newNum;
		gas = 0.0;
		speed = 0;
		fuelEff = newFuelEff;	
		System.out.println("Set number to " + num + " and fuel efficiency to " + fuelEff);
	}
	
	public void setSpeed(int newSpeed) {
		speed = newSpeed;
		System.out.println("Set speed to " + speed);
	}
	
	public void addGas(double added) {
		gas = gas + added;
		System.out.println(added + " liters of gas was added");
		System.out.println("Car now has " + gas + " liters of gas");
	}
	
	public void drive(int hours) {
		double consumed = speed * hours / fuelEff;
		gas = gas - consumed;
		System.out.println("Car was driven " + hours + " hours at " + speed + "Km/hr");
		System.out.println("Car consumed " + consumed + " liters of gas");
		System.out.println("Car now has " + gas + " liters of gas");
	}
	
	public static void main(String[] args) {
		Car car = new Car(12345, 10.0);
		car.addGas(40.0);
		car.setSpeed(60);
		car.drive(3);
	}
}
