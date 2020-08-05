package ch08.sec01.exam01;

public class SmartTelevision implements RemoteControl, Searchable {
	
    private int volume;
	
	public void turnOn() {
		System.out.println("Turning on the TV");
	}
	
	public void turnOff() {
		System.out.println("Turning off the TV");
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
		
		System.out.println("Current TV Volume : " + this.volume);
	}
	
	public void search(String url) {
		System.out.println("Search for " + url);
	}
}
