package ch03.exam10;

public class AssignmentOperatorExample {

	public static void main(String[] args) {
		int result = 0;
		result += 10; //adding 10 on result
		System.out.println(result);//this should be 20
		
		result -= 5; //decreasing by 5
		System.out.println(result);
		
		result *= 3; //multiplying by 3
		System.out.println(result);
		
		result /= 5; //dividing by 5
		System.out.println(result);
		
		result %= 3;
		System.out.println(result);		

	}

}
