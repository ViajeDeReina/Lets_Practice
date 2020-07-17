/*#include <stdio.h>

#define MAX 100

int Queue[MAX];
int Front, Rear;

void InitializeQueue() {
	Front = 0;
	Rear = 0;
}

void Put(int num) {
	Queue[Rear++] = num;
	if (Rear >= MAX) {
		Rear = 0;
	}
}

int Get() {
	int ret;
	ret = Queue[Front++];
	if (Front >= MAX) {
		Front = 0;
	}
	return ret;
}

void DisplayQueue() {
	int i;
	printf("Front -> ");
	for (i = Front; i < Rear; i++) {
		printf("%2d -> ", Queue[i]);
	}
	printf("Rear");
}

void main() {
	int ret;
	InitializeQueue();

	Put(1);
	Put(3);
	Put(10);
	Put(20);
	Put(12);

	printf("After calling the function Put() for 5 times : \n");
	DisplayQueue();

	ret = Get();
	ret = Get();
	ret = Get();

	printf("\nAfter calling the function Get() for 3 times : \n");
	DisplayQueue();

	printf("\nAfter calling the function Get() for 2 more times : \n");
	ret = Get();
	ret = Get();
	DisplayQueue();
}*/