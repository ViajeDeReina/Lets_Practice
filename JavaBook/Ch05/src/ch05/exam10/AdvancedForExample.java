package ch05.exam10;

public class AdvancedForExample {

	public static void main(String[] args) {
		int[] scores = {95, 71, 84, 93, 87};
		
		int sum = 0;
		for (int score : scores)
		{
			sum = sum + score;
		}
		System.out.println("Total Score : " + sum);
		
		double avg = (double)sum / scores.length;
		System.out.printf("Average : %.1f", avg);

	}

}
