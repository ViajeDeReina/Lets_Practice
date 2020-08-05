package ch08.sec01.exam01;

public interface RemoteControl {
	// this is like CONSTANT
	public int MAX_VOLUME = 10;
	public int MIN_VOLUME = 0;
	
	// METHOD - we just give them name & variable, NOT specify the procedure
	public void turnOn();
	public void turnOff();
	public void setVolume(int volume);
}