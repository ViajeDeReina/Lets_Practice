package ch07.sec01.exam02;

public class StudentExample {

	public static void main(String[] args) {
		Student student = new Student("Felipe", "123456-7890123", 200601033);
		System.out.println("Name : " + student.name);
		System.out.println("SSN :" + student.ssn);
		System.out.println("Student No. : " + student.studentNo);
	}
}