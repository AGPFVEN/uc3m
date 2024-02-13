#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char *argv[]){
	int *pointer, *pointer2;
	char* string;

	printf("Address of 1st pointer: %p\n", pointer);
	pointer = malloc (sizeof(int));
	printf("Malloc is used\n\n");

	printf("Address of 1st pointer: %p\n", pointer);
	*pointer = 4;
	printf("Content of 1st pointer: %d\n\n", *pointer);

	free(pointer);
	printf("free is used\n");
	printf("Address of 1st pointer: %p\n", pointer);
	printf("Content of 1st pointer: %d\n\n", *pointer);

	printf("Address of 2nd pointer: %p\n\n", pointer2);

	pointer2 = malloc (sizeof(int)); //This line is not written in solution but If it is not written it causes an segmentation fault error
	*pointer2 = 5;
	printf("5 is assigned to 2nd pointer\n");
	printf("Address of 2nd pointer: %p\n", pointer2);
	printf("Content of 2nd pointer: %d\n\n", *pointer2);

	printf("Address of string %p\n", string);
	//printf("Content of string %d\n", *string); //This can not written in this specific line possition because of the lack of positioning (malloc) of the pointer
	
	string = malloc (40);
	strcpy(string, "This is my string pointer"); //This is how you can put strings in a string pointer
	printf("Content of string: %s\n", string);

}
