package ch07.sec02.exam03;

public class CarExample {

	public static void main(String[] args) {
		Car car = new Car();
		
		for (int i = 1; i<=5; i++)
		{
			int problemLocation = car.run();
			
			switch (problemLocation) {
			
			case 1:
				System.out.println("FrontLeft Tire is altered to HankookTire.");
				car.frontLeftTire = new HankookTire("FrontLeft", 15);
				break;
			case 2:
				System.out.println("FrontRight Tire is altered to KumhoTire.");
				car.frontRightTire = new KumhoTire("FrontRight", 13);
				break;
			case 3:
				System.out.println("BackLeft Tire is altered to HankookTire.");
				car.backLeftTire = new HankookTire("BackLeft", 14);
				break;
			case 4:
				System.out.println("FrontLeft Tire is altered to KumhoTire.");
				car.backRightTire = new KumhoTire("BackRight", 17);
				break;
			}
			
			System.out.println("----------------------------------------------");
		}
	}
}
