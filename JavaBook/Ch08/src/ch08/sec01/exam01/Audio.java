package ch08.sec01.exam01;

public class Audio implements RemoteControl {
	
    private int volume;
	
	public void turnOn() {
		System.out.println("Turning on the Audio");
	}
	
	public void turnOff() {
		System.out.println("Turning off the Audio");
	}
	
	public void setVolume(int volume) {
		if (volume > RemoteControl.MAX_VOLUME) {
			this.volume = RemoteControl.MAX_VOLUME;
		}
		else if (volume < RemoteControl.MIN_VOLUME) {
			this.volume = RemoteControl.MIN_VOLUME;
		}
		else {
			this.volume = volume;
		}
		
		System.out.println("Current Audio Volume : " + this.volume);
	}
}