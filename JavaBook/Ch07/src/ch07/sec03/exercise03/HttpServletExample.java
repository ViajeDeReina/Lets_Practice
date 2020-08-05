package ch07.sec03.exercise03;

public class HttpServletExample {

	public static void main(String[] args) {
		method(new LoginServelet());
		method(new FileDownloadServlet());
	}
	
	public static void method(HttpServlet servlet) {
		servlet.service();
	}
}