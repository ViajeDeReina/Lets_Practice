package ch07.sec01.exam01;

public class Cellphone {
	String model;
	String color;
	
	void powerOn() {
		System.out.println("Turnning on the power.");
	}
	void powerOff() {
		System.out.println("Turning off the power.");
	}
	void bell() {
		System.out.println("Ringing the bell.");
	}
	void sendVoice(String message) {
		System.out.println("Me : " + message);
	}
	void receiveVoice(String message) {
		System.out.println("She : " + message);
	}
	void hangUp() {
		System.out.println("Hung up the phone.");
	}
}
