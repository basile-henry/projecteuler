#include <stdio.h>

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

int sort(int* list, int size) {
	if (size == 1) {
		return 0;
	}

	sort(list, size/2);
	sort(list+size/2, size - size/2);

	int* a;
	int* b;

	memcpy(a, list, size/2);
	memcpy(b, list+size/2,size - size/2);

	mergesort(a, size/2, b, size - size/2, list);

	return 0;
}

int main(){
	int a[6] = {1,2,3,4,5,6};
	int b[4] = {3,4,8,9};

	int p[10];
	mergesort(a, 6, b, 4, p);


	int i;
	for (i = 0; i < 10; i++) {
		printf("%d ", *(p+i));
	}
	printf("\n");

	int list[10] = {5,64,12,24,10,1,3,89,4,20};
	printf("%d\n", *(list + 11/2));

	sort(list, 10);

	for (i = 0; i < 10; i++) {
		printf("%d ", *(list+i));
	}
	printf("\n");

	// int l[1] = {2}
	// int *d = sort(l,1);
	// printf("%d\n", *d);
	return 0;
}