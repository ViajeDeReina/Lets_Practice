// Ch04> Exercise 02 : Practice the basic loop using FOR

package ch04.exer02;

public class exer02 {

	public static void main(String[] args) {
		int i = 0;
		int sum = 0;
		
		for (i=1; i<=100; i++) {
			if (i%3 == 0) {
				sum += i;
			}
		}
		
		System.out.println(sum);
	}
}