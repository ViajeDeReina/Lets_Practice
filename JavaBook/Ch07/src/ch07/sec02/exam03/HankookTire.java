package ch07.sec02.exam03;

public class HankookTire extends Tire {
	
	public HankookTire (String location, int maxRotation) {
		super(location, maxRotation);
	}
	
	@Override
	public boolean roll() {
		++accumulatedRotation;
		if(accumulatedRotation < maxRotation) {
			System.out.println(location + " HankookTire's life cycle : " + (maxRotation - accumulatedRotation) + " times");
			return true;
		}
		else {
			System.out.println("*** " + location + " HankookTire Punk ***");
			return false;
		}
	}

}
