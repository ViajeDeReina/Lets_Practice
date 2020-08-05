package ch07.sec03.exam01;

public abstract class Phone {
	
	public String owner;
	
	public Phone(String owner) {
		this.owner = owner;
	}
	
	public void turnOn() {
		System.out.println("Turning on the phone.");
	}
	
	public void turnOff() {
		System.out.println("Turning off the phoone.");
	}
}