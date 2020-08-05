package ch04.exercise03;

public class Exercise03 {

	public static void main(String[] args) {
		// let's roll dice till it gets 5.
		
		int dice1, dice2;
		int sum;
		
		while (true)
		{
			dice1 = (int)(Math.random()*6) +1;
			dice2 = (int)(Math.random()*6) +1;
			sum = dice1 + dice2;
			
			if (sum == 5)
			{break;}
			
			System.out.printf("Roll the dice! Now we've got %d, %d. The summation is %d.\n", dice1, dice2, sum);
		}
	
		System.out.printf("Roll the dice! Now we've got %d, %d. The summation is %d.\n", dice1, dice2, sum);
		System.out.println("Now we have 5, and it's completed.");
	}

}
