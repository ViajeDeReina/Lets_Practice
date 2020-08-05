package ch07.sec01.exam01;

public class DmbCellPhonExample {

	public static void main(String[] args) {
		DmbCellPhone dmbCellPhone = new DmbCellPhone("Huawei P20", "Black", 10);
		
		System.out.println("Model : " + dmbCellPhone.model);
		System.out.println("Color : " + dmbCellPhone.color);
		
		System.out.println("Channel : "+dmbCellPhone.channel);
		
		dmbCellPhone.powerOn();
		dmbCellPhone.bell();
		dmbCellPhone.sendVoice("Digame?");
		dmbCellPhone.receiveVoice("Hola, soy Marco.");
		dmbCellPhone.sendVoice("Hola, Marco. Que pasa?");
		dmbCellPhone.hangUp();
		
		dmbCellPhone.turnOnDmb();
		dmbCellPhone.changeChannelDmb(12);
		dmbCellPhone.turnOffDmb();

	}

}
