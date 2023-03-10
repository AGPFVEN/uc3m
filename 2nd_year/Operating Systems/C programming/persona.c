#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void main(int argc, char ** argv){
	char name[32];
	int age;
	if (argc < 2){
		printf("Not enough arguments provided");
	}

	//Take data
	strcpy(name, argv[1]);
	age = atoi(argv[2]);

	//Print data
	printf("Hi %s, of %i years old\n", name, age);
}
