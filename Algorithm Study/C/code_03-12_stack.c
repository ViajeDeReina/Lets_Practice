/*#include <stdio.h>
#include <stdlib.h>

typedef struct _NODE {
	int Data;
	struct _NODE* Next;
}NODE;

NODE* head, * end;
NODE* ptrNode;

void InitializeStack() {
	head = (NODE*)malloc(sizeof(NODE));
	end = (NODE*)malloc(sizeof(NODE));
	head->Next = end;
	end->Next = end;
}

void Push(int num) {
	ptrNode = (NODE*)malloc(sizeof(NODE));
	ptrNode->Data = num;
	ptrNode->Next = head->Next;
	head->Next = ptrNode;
}

int Pop() {
	int ret;
	ptrNode = head->Next;
	head->Next = head->Next->Next;
	ret = ptrNode->Data;
	free(ptrNode);

	return ret;
}

void DisplayStack() {
	NODE* indexNode;
	printf("head-> ");

	for (indexNode = head->Next; indexNode != end; indexNode = indexNode->Next) {
		printf("%d -> ", indexNode->Data);
	}

	printf("end\n");
}

void main() {
	int ret;
	InitializeStack();
	Push(1);
	Push(5);
	Push(10);
	Push(20);
	Push(12);

	printf("After calling Push() function for 5 times : \n");
	DisplayStack();

	ret = Pop();
	ret = Pop();
	ret = Pop();

	printf("After calling Pop() function for 3 times :\n");
	DisplayStack();
}*/