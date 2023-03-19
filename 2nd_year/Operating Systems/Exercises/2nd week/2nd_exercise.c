#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int switch_integers(int *pointer, int *pointer2){
	printf("Inside switch_integers\n");
	int temp_int;

	printf("Address of first pointer: %p\n", pointer);
	printf("Address of second pointer: %p\n", pointer2);

	temp_int = *pointer;

	*pointer = *pointer2;
	*pointer2 = temp_int;

	printf("%d\n", *pointer2);
	printf("End of switch_integers\n\n");
}

int main(int argc, char *argv[]){
	int int1, int2;

	int1 = 10;
	int2 = 25;

	printf("Before the switch\n");
	printf("Address of first pointer: %p\n", &int1);
	printf("Content of first int: %d\n", int1);
	printf("Address of second pointer: %p\n", &int2);
	printf("Content of second int: %d\n\n", int2);

	switch_integers(&int1, &int2);

	printf("After the switch\n");
	printf("Address of first pointer: %p\n", &int1);
	printf("Content of first int: %d\n", int1);
	printf("Address of second pointer: %p\n", &int2);
	printf("Content of second int: %d\n", int2);
}
