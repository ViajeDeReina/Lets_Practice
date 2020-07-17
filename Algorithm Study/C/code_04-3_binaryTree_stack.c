#include "code_04-3_binaryTree.h"
#define MAX 100

NODE* Stack[MAX];
int Top;

void InitializeStack() {
	Top = 0;
}

void Push(NODE* ptrNode) {
	Stack[Top] = ptrNode;
	Top = (Top++) % MAX;
}

NODE* Pop() {
	NODE* ptrNode;

	if (!IsStackEmpty()) {
		ptrNode = Stack[--Top];
		return ptrNode;
	}
	else {
		printf("The stack is empty.\n");
	}
	return NULL;
}

int IsStackEmpty() {
	if (Top == 0) {
		return TRUE;
	}
	else
		return FALSE;
}