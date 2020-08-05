package ch03.exam09;

public class LogicalOperatorExample {

	public static void main(String[] args) {
		
		int charCode = 'A';
		
		if ((charCode >= 65) & (charCode <= 90))
			{
			System.out.println("You've got a capital letter.");
			}
		
		if ((charCode >= 97) && (charCode <=122))
		{
			System.out.println("You've got a small letter.");
		}
		
		if (!(charCode < 48) && !(charCode > 57))
		{
			System.out.println("It's a digit between 0~9.");
		}
		
		int value = 6;
		
		if ((value%2 == 0) | (value%3 == 0))
		{
			System.out.println("It's multiplier of 2 or 3.");
		}
		
		if ((value%2 == 0) || (value%3 == 0))
		{
			System.out.println("It's multiplier of 2 or 3.");
		}

	}

}
