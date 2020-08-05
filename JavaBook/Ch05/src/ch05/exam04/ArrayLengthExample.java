package ch05.exam04;

public class ArrayLengthExample {

	public static void main(String[] args) {
		int[] scores = {83, 90, 87};
		
		int sum = 0;
		for (int i=0; i< scores.length; i++)
		{
			sum += scores[i];
		}
		System.out.println("Total Score : "+ sum);
		
		double avg = (double)sum / scores.length;
		System.out.printf("Average : %.2f\n", avg);

	}

}
