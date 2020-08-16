package ch09.sec02.exam01;

public class AnonymousExample {

	public static void main(String[] args) {
		Anonymous anony = new Anonymous(); //the object has been created
		
		anony.field.wake(); //6 O'clock
		anony.method1(); //7 O'clock
		
		anony.method2(
			new Person() {
				void study() {
					System.out.println("공부합니다.");
				}
				@Override
				void wake() {
					System.out.println("8시에 일어납니다.");
					study();
				}
			});
	}
}