package ch07.sec03.exam02;

public abstract class Animal {
	public String kind;
	
	public void breath() {
		System.out.println("It breathes.");
	}
	
	public abstract void sound();

}
