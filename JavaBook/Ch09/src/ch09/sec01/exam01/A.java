package ch09.sec01.exam01;

public class A {
	A(){System.out.println("Object A has been created.");}
	
	class B{
		B() {System.out.println("Object B has been created.");}
		int field1;
		void method1() {}
	}
	
	static class C{
		C() {System.out.println("Object C has been created.");}
		int field1;
		static int field2;
		void method1() {}
		static void method2() {}
	}
	
	void method() {
		
		class D{
			D(){System.out.println("Object D has been created.");}
			int field1;
			void method1() {}
		}
	
	D d = new D();
	d.field1 = 3;
	d.method1();
	}
}
