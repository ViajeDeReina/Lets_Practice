package ch07.sec01.exam01;

public class DmbCellPhone extends Cellphone {
	
	int channel;
	
	DmbCellPhone(String model, String color, int channel){
		this.model = model;
		this.color = color;
		this.channel = channel;
	}
	
	void turnOnDmb() {
		System.out.println("We're receiving channel No." + channel);
	}
	
	void changeChannelDmb(int channel) {
		this.channel = channel;
		System.out.println("Changing channel to No." + channel);
	}
	
	void turnOffDmb() {
		System.out.println("Stop receiving DMB signal.");
	}

}
