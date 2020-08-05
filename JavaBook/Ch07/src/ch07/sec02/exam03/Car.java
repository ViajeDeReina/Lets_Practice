package ch07.sec02.exam03;

public class Car {
	
	Tire frontLeftTire = new Tire("Front left", 6);
	Tire frontRightTire = new Tire("Front right", 2);
	Tire backLeftTire = new Tire("Back left", 3);
	Tire backRightTire = new Tire("Back right", 4);
	
	int run() {
		System.out.println("[The car runs now.]");
		if (frontLeftTire.roll() == false) {stop(); return 1;}
		if (frontRightTire.roll() == false) {stop(); return 2;}
		if (backLeftTire.roll() == false) {stop(); return 3;}
		if (backRightTire.roll() == false) {stop(); return 4;}
		return 0;
	}
	
	void stop() {
		System.out.println("[The car stops.]");
	}
}