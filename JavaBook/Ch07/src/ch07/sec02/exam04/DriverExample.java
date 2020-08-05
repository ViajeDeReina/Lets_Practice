package ch07.sec02.exam04;

public class DriverExample {

	public static void main(String[] args) {
		Driver driver = new Driver();
		Vehicle vehicle = new Vehicle();
		Bus bus = new Bus();
		Taxi taxi = new Taxi();
		
		driver.drive(bus);
		driver.drive(taxi);
		driver.drive(vehicle);
	}
}