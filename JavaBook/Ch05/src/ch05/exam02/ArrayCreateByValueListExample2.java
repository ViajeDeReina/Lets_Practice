package ch05.exam02;

public class ArrayCreateByValueListExample2 {

	public static void main(String[] args) {
		int[] scores;
		scores = new int[] {83, 90, 87};
		int sum1 = 0;
		for (int i =0; i<3; i++)
		{
			sum1 += scores[i]; //while the FOR LOOP works, it will fill up the array by its num
		}
		
		System.out.println("Total : " + sum1);
		
		int sum2 = add(new int[] {83, 90, 87});
		System.out.println("Total : " + sum2);
		System.out.println();
	}
	
	public static int add(int[] scores)// This is called METHOD, feels like FUNCTION of C.
	{
		int sum = 0;
		for (int i=0; i<3; i++)
		{
			sum += scores[i];
		}
		return sum;
	}

}
