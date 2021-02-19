#include <stdio.h>
#include <stdlib.h>


/* hashTable�� bucket�� �迭�� ����. */
/* key�� �����ϰ� ���´�. value�� �������� ����� */
struct bucket* hashTable = NULL;
int SIZE = 10; // �ʱ� bucket size


struct node {
	int key;
	int value;
	struct node* next;
};

struct bucket {
	// bucket�� ���� �� �༮
	struct node* head;
	int count;
};

/* "�� key�� value�� ���� node"�� ������� */
struct node* createNode(int key, int value) {
	struct node* newNode;
	newNode = (struct node*)malloc(sizeof(struct node));

	newNode->key = key;
	newNode->value = value;
	
	newNode->next = NULL;

	return newNode;
}

int hashFunction(int key) {
	// ��� bucket�� ���� !
	// key(mod SIZE)
	return key % SIZE;
}

/* bucket �� 
	head & count update */
void insert(int key, int value) {
	
	int hashIndex = hashFunction(key); /* hash bucket �˷��ش�. */
	struct node* newNode = createNode(key, value); /* ������ newnode ���� */

	/* ���� �ְ��� �ϴ� �ε����� ���� �̹� ���� ���*/
	if (hashTable[hashIndex].count == 0) {
		hashTable[hashIndex].count = 1;
		hashTable[hashIndex].head = newNode;
		newNode->next = NULL;
	}
	/* ���� �ְ��� �ϴ� �ε����� ���� �̹� �ִ� ��� - COLLISION */
	else {
		hashTable[hashIndex].count++;
		/* ���ο� ��尡 head�� �ȴ�. */
		newNode->next = hashTable[hashIndex].head;
		hashTable[hashIndex].head = newNode;
	}

}

/* value�� �˻縦 ���ϳ� ?*/
void delete(int key) {

	int hashIndex = hashFunction(key);	
	struct node* horse = hashTable[hashIndex].head; /* ������ NULL ��*/
	struct node* trace = NULL; /*head���� �ؼ� �Ѿ� �� �༮*/
	
	if (horse) {
		while (horse != NULL) {
			/* ���� �� ���� �޸��� */
			if (horse->key == key) {
				/* ������ ���� */
				if (horse == hashTable[hashIndex].head)
					hashTable[hashIndex].head = horse->next;
				else
					trace->next = horse->next; /* �� Ÿ�ֿ̹��� trace�� NULL�� ���� ����.*/
				
				hashTable[hashIndex].count--;
				free(horse); /* delete ��� free */
				return;
			}
			trace = horse;
			horse = horse->next;
		}
		printf("\nThere is no key!!\n");

	}
	/* key �� ���� */
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