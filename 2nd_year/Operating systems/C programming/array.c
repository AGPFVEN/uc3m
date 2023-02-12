#include<stdio.h>

int main(int argc, char **argv) {
	int myArray[5];
	int i;

	for (i=0; i<5; i++){
		printf("Input a number: \n");
		scanf("%d", &myArray[i]);
		printf("%d\n", i);
	}

	for (i=0; i<5; i++){
		printf("%d ", myArray[i]);
	}

	printf("\n");
	return 0;
}
