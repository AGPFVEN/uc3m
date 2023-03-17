#include<stdio.h>

int main(int argc, char *argv[]){
	//First part of the exercise
	int my_int = 5;
	long int my_long_int = 900000000000; //This value could not be represented with a normal int
	float my_float = 3.14;

	printf("this is my int %d\nthis is my long int %ld\nthis is my float %f\n", my_int, my_long_int, my_float);

	//Second part of the exercise
	int my_2nd_int;

	printf("Enter 2 numbers separated by a comma following n1,n2\n");
	scanf("%d, %d", &my_int, &my_2nd_int);
	printf("This are my new integers:\nfirst one: %d\nsecond one: %d\n", my_int, my_2nd_int);
}
