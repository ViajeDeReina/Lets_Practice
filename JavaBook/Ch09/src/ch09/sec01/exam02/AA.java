package ch09.sec01.exam02;

public class AA {
	
	B field1 = new B();
	C field2 = new C();
	
	void method1() {
		B var1 = new B();
		C var2 = new C();
	}
	
	// static B filed3 = new B(); <<<< IMPOSSIBLE, since B is not a static class
	static C field4 = new C();
	
	static void method2() {
		// B var1 = new B(); <<<< IMPOSSIBLE, since B is not a static class
		C var2 = new C();
	}
	
	class B {}
	
	static class C {}
}