package ch03.exam11;

public class ConditinalOperationExample {

	public static void main(String[] args) {
		int score = 85;
		
		char grade = (score > 90)? 'A': ((score > 80)? 'B':'C');
		System.out.println("You've got "+ score + " points. Your grade is " + grade);

	}
}
