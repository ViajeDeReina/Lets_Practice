/*#include <stdio.h>
#include <stdlib.h>

typedef struct _NODE {
	int Data;
	struct _NODE* Next;
}NODE;

NODE* Front, * Rear;
NODE* ptrNode;

void InitializeQueue() {
	Front = (NODE*)malloc(sizeof(NODE));
	Rear = (NODE*)malloc(sizeof(NODE));
	Front->Next = Rear;
	Rear->Next = Front; // this means : when the list ends, it automatically goes to Front
}

void Put(int num) {
	ptrNode = (NODE*)malloc(sizeof(NODE));
	ptrNode->Data = num;

	if (Front->Next == Rear) {
		Front->Next = ptrNode;
		ptrNode->Next = Rear;
		Rear->Next = ptrNode;
	}
	else {
		Rear->Next->Next = ptrNode;
		ptrNode->Next = Rear;
		Rear->Next = ptrNode;
	}
}

int Get() {
	int ret;
	NODE* deleteNode; //it will be similar to deleteNode function of linked list.
	printf("\n");

	if (Front->Next == Rear) {
		printf("Queue Empty\n");
	}
	else {
		deleteNode = Front->Next;
		Front->Next = deleteNode->Next;
		ret = deleteNode->Data;
		printf("get() : %d", ret);
		free(deleteNode);
	}
	return ret;
}

void DisplayQueue() {
	NODE* ptrTemp;

	if (Front->Next != Rear) {
		for (ptrTemp = Front->Next; ptrTemp->Next != Rear; ptrTemp = ptrTemp->Next) {
			printf("%d -> ", ptrTemp->Data);
		}
		printf("%d\n", ptrTemp->Data);
	}
	else if (Front->Next == Rear) {
		printf("Queue Empty\n");
	}
}

void main() {
	int ret;
	InitializeQueue();
	printf("Let's call the Put() function!\n");

	Put(1);
	Put(3);
	Put(10);
	Put(20);
	Put(12);

	printf("After calling the Put() function for 5 times : \n");
	DisplayQueue();

	ret = Get();
	ret = Get();
	ret = Get();

	printf("\nAfter calling the Get() function for 3 times : \n");
	DisplayQueue();

	ret = Get();
	ret = Get();

	printf("\nAfter calling the Get() function for 2 more times : \n");
	DisplayQueue();
}*/