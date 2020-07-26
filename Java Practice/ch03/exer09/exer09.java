// Ch03 > Exercise 09 : Basic practice for input data & converting data type by Parse

package ch03.exer09;

import java.util.Scanner;

public class exer09 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("첫번째 수 : " );
		double num1 = (double)Double.parseDouble(scanner.next());
		System.out.print("두번째 수 : " );
		double num2 = (double)Double.parseDouble(scanner.next());
		
		System.out.println("----------------------");
		
		if ((num2 !=0) && (num2 != 0.0)) {
			System.out.printf("결과 : %.2f", num1/num2);
		}
		else {
			System.out.println("결과 : 무한대");
		}
	}
}
