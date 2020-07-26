// Ch04> Exercise 03 : Roll the dices till the summation reaches 5

package ch04.exer03;

public class exer03 {

	public static void main(String[] args) {
		int sum = 0;
		while (sum !=5) {
			int dice1 = (int)(Math.random()*6)+1;
			int dice2 = (int)(Math.random()*6)+1;
			System.out.printf("(%d, %d)\n", dice1, dice2);
			sum = dice1 + dice2;
			if (sum ==5) {
				break;
			}
		}
	}
}