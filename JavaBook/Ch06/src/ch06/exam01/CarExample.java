package ch06.exam01;

public class CarExample {

	public static void main(String[] args) {
		
		Car myCar = new Car(); //creating new OBJECT from Car class
		
		System.out.println("Company : " + myCar.company);
		System.out.println("Model : " + myCar.model);
		System.out.println("Colour : " + myCar.colour);
		System.out.println("Maximum Speed : " + myCar.maxSpeed);
		System.out.println("Current Speed : " + myCar.speed + "km/h");
		
		myCar.speed = 60;
		
		System.out.println("After changed : " + myCar.speed + "km/h");

	}

}
