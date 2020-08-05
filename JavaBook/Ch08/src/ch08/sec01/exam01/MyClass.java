package ch08.sec01.exam01;

public class MyClass {
	
	// FIELD
	RemoteControl rc = new Television();
	
	// CONSTRUCTOR
	MyClass() {
	}
	
	MyClass (RemoteControl rc) {
		this.rc = rc;
		rc.turnOn();
		rc.setVolume(5);
	}
	
	// METHOD
	void methodA () {
		RemoteControl rc = new Audio();
		rc.turnOn();
		rc.setVolume(5);
	}
	
	void methodB (RemoteControl rc) {
		rc.turnOn();
		rc.setVolume(5);
	}
}