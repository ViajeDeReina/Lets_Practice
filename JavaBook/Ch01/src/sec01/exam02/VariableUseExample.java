
package sec01.exam02;

public class VariableUseExample {
  public static void main(String[] args) {
	int hour = 3;
	int minute = 5;
	System.out.println(hour + "hrs " + minute + "mins");
	
	int totalMinute = (hour * 60) + minute;
	System.out.println("TTL " + totalMinute + " mins");
  }
}
