package ch09.sec02.exam02;

public class Anonymous {
	
	RemoteControl field = new RemoteControl() {
		@Override
		public void turnOn() {
			System.out.println("Turning on the TV");
		}
		@Override
		public void turnOff() {
			System.out.println("Turning off the TV");
		}
	};
	
	void method1() {
		RemoteControl localVar = new RemoteControl() {
			@Override
			public void turnOn() {
				System.out.println("Turning on the Audio");
			}
			@Override
			public void turnOff() {
				System.out.println("Turning off the Audio");
			}
		};
		localVar.turnOn();
	}
	
	void method2(RemoteControl rc) {
		rc.turnOn();
	}
}