package ch08.sec02.exam02;

public class Bus implements Vehicle{
	@Override
	public void run() {
		System.out.println("The Bus runs.");
	}
	
	public void checkFare() {
		System.out.println("Check the fare.");
	}
}