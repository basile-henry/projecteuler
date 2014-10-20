#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int mergesort(int listA[], int sizeA, int listB[], int sizeB, int *buffer){
	int i = 0;
	int j = 0;

	while (1) {
		if (listA[i] < listB[j]) {
			*(buffer+i+j) = listA[i];
			i++;
		} else {
			*(buffer+i+j) = listB[j];
			j++;
		}

		if (i == sizeA) {
			while (j < sizeB) {
				*(buffer+i+j) = listB[j];
				j++;
			}
			return 0;
		}
		if (j == sizeB) {
			while (i < sizeA) {
				*(buffer+i+j) = listA[i];
				i++;
			}
			return 0;
		}
	}
}

int sort(int* list, int size, int* buffer) {
	if (size == 1) {
		*buffer = *list;
		return 0;
	}

	int a[size/2];
	int b[size - size/2];

	sort(list, size/2, a);
	sort(list + size/2, size - size/2, b);

	mergesort(a, size/2, b, size - size/2, buffer);
	return 0;
}

int main(){

	int SIZE = 20;
	int list[SIZE];
	int sorted[SIZE];

	int i;
	time_t t;

	srand((unsigned) time(&t));

	for (i = 0; i < SIZE; i++) {
		list[i] = rand()%1000;
	}

	sort(list, SIZE, sorted);

	for (i = 0; i < SIZE; i++) {
		printf("%d ", list[i]);
	}
	printf("\n");

	for (i = 0; i < SIZE; i++) {
		printf("%d ", sorted[i]);
	}
	printf("\n");

	return 0;
}