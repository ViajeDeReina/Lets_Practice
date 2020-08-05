package ch07.sec02.exam06;

public class InstanceOfExample {

	public static void method1(Parent parent) {
		
		if (parent instanceof Child) {
			System.out.println("Successfully converted : method1 - Child");
		}
		else
		{
			System.out.println("Converting Failed : method1 - Child");
		}
	}
	
	public static void method2(Parent parent) {
		Child child = (Child) parent;// THIS MAY CAUSE EXCEPTION ERROR
		System.out.println("Successfully converted : method2 - Child");
	}
	
	public static void main(String[] args) {
		Parent parentA = new Child();
		method1(parentA);
		method2(parentA);
		
		Parent parentB = new Parent();
		method1(parentB);
		//method2(parentB);// THIS MAKE AN EXCEPTION ERROR!!!!!!! :(

	}

}
