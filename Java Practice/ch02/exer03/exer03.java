// Ch02 > Exercise 03 : Basic practice for data input using Scanner

package ch02.exer03;

import java.util.Scanner;

public class exer03 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("[필수 정보 입력]");
		System.out.print("1. 이름 : ");
		String name = scanner.nextLine();
		System.out.print("2. 주민번호 앞 6자리 : ");
		String number = scanner.nextLine();
		System.out.print("3. 전화번호 : ");
		String tel = scanner.nextLine();
		
		System.out.println("\n[입력한 내용]");
		System.out.printf("%s\n%s\n%s", name, number, tel);
	}

}