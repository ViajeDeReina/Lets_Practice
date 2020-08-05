package ch03.exam04;

public class ArithmetricOperatorExample {

	public static void main(String[] args) {
		int v1 = 5;
		int v2 = 2;
		
		int result1 = v1+v2;
		System.out.println("v1 + v2 = " + result1);
		
		int result2 = v1-v2;
		System.out.println("v1 - v2 = " + result2);
		
		int result3 = v1*v2;
		System.out.println("v1 * v2 = " + result3);
		
		int result4 = v1/v2;
		System.out.println("v1 / v2 = " + result4);
		
		double result5 = (double)v1/v2;
		System.out.println("v1 / v2 = " + result5);
		
		int result6 = v1%v2;
		System.out.println("residue of v1/v2 = " + result6);

	}

}
