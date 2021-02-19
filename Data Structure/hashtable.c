#include <stdio.h>
#include <stdlib.h>


/* hashTable을 bucket의 배열로 본다. */
/* key를 고유하게 갖는다. value는 부차적인 요소임 */
struct bucket* hashTable = NULL;
int SIZE = 10; // 초기 bucket size


struct node {
	int key;
	int value;
	struct node* next;
};

struct bucket {
	// bucket의 가장 앞 녀석
	struct node* head;
	int count;
};

/* "이 key와 value를 가진 node"를 만들어줘 */
struct node* createNode(int key, int value) {
	struct node* newNode;
	newNode = (struct node*)malloc(sizeof(struct node));

	newNode->key = key;
	newNode->value = value;
	
	newNode->next = NULL;

	return newNode;
}

int hashFunction(int key) {
	// 몇번 bucket에 들어가라 !
	// key(mod SIZE)
	return key % SIZE;
}

/* bucket 내 
	head & count update */
void insert(int key, int value) {
	
	int hashIndex = hashFunction(key); /* hash bucket 알려준다. */
	struct node* newNode = createNode(key, value); /* 삽입할 newnode 생성 */

	/* 내가 넣고자 하는 인덱스에 값이 이미 없는 경우*/
	if (hashTable[hashIndex].count == 0) {
		hashTable[hashIndex].count = 1;
		hashTable[hashIndex].head = newNode;
		newNode->next = NULL;
	}
	/* 내가 넣고자 하는 인덱스에 값이 이미 있는 경우 - COLLISION */
	else {
		hashTable[hashIndex].count++;
		/* 새로운 노드가 head가 된다. */
		newNode->next = hashTable[hashIndex].head;
		hashTable[hashIndex].head = newNode;
	}

}

/* value는 검사를 안하네 ?*/
void delete(int key) {

	int hashIndex = hashFunction(key);	
	struct node* horse = hashTable[hashIndex].head; /* 없으면 NULL 임*/
	struct node* trace = NULL; /*head부터 해서 쫓아 올 녀석*/
	
	if (horse) {
		while (horse != NULL) {
			/* 같을 때 까지 달린다 */
			if (horse->key == key) {
				/* 포인터 변경 */
				if (horse == hashTable[hashIndex].head)
					hashTable[hashIndex].head = horse->next;
				else
					trace->next = horse->next; /* 이 타이밍에서 trace가 NULL일 수는 없다.*/
				
				hashTable[hashIndex].count--;
				free(horse); /* delete 요소 free */
				return;
			}
			trace = horse;
			horse = horse->next;
		}
		printf("\nThere is no key!!\n");

	}
	/* key 가 없다 */
	else{
		printf("\nThere is no Key\n");
	}
}

void search(int key) {
	int hashIndex = hashFunction(key);
	struct node* horse = hashTable[hashIndex].head;
	if (horse) {
		while (horse != NULL) {
			if (horse->key == key) {
				printf("FOUND !! -  key : %d, value = %d \n", horse->key,horse->value); 
				return;
			}
			horse = horse->next;
		}
		printf("\n There is no Key\n");
	}
	else {
		printf("\n There is no Key\n");
	}
}

void display() {
	struct node* horse;

	for (int i = 0; i < SIZE; i++) {
		horse = hashTable[i].head;
		printf("Bucket : %d \n", i);
		while (horse != NULL) {
			printf("(key : %d , val : %d) ", horse->key, horse->value);
			horse = horse->next;
		}
		printf("\n");
	}
	printf("------------ END of Display -------------\n");
}
int main() {

	hashTable = (struct bucket*)calloc(SIZE,sizeof(struct bucket));
	insert(0, 1);


	insert(1, 10);

	insert(11, 10);

	insert(21, 10);
	insert(31, 20);
	insert(6, 25);
	insert(86, 4);
	insert(3, 40);

	display();

	delete(31);
	delete(21);

	display();

}