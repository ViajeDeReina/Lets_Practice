// Ch04> Exercise 04 : find the x & y which makes 4x+5y = 60

package ch04.exer04;

public class exer04 {

	public static void main(String[] args) {
		int i = 0;
		int j = 0;
		
		for (i=1; i<=10; i++) {
			for (j=1; j<=10; j++) {
				if (4*i+5*j == 60) {
					System.out.printf("(%d, %d)\n", i, j);
				}
			}
		}
	}
}