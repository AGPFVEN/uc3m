#include<stdio.h>
#include<string.h>

int main(int argc, char *argv[]){
	int int_vector[10];	
	printf("This is the size of a 10-element vector: %ld bytes\n", sizeof(int_vector));

	char string[] = "This is four";  //This is an example string of length 12
	char string_copy[8];

	// This is waht the professor did
	printf("Length of string: %lu\nNumber of positions in the array: %lu\nContent of string: %s\n",
		sizeof(string), sizeof(string)/sizeof(char), string);
	printf("Length of string using strlen: %lu\n\n", strlen(string));

	strcpy(string, "Hi Anna");
	printf("After strcpy\n");
	printf("Length of string: %lu\nNumber of positions in the array: %lu\n", sizeof(string), sizeof(string)/sizeof(char));
	printf("Length of string using strlen: %lu\n", strlen(string));
	
	
	//This is my try 
	/*
	memcpy(string_copy, string, 8); //The function strncpy doesn't work ?
	
	char string_copy2[9];
	
	for (int i = 0; i < 9; i++){
		printf("%d\n", string[i]);
		string_copy2[i] = string[i];
	}

	printf("This is the string: %s\n", string);
	printf("This is the first copy: %s\n", string_copy);
	printf("This is the second copy %s\n", string_copy2);
	*/
}
