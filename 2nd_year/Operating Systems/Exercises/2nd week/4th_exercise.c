#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[]){
	printf("Input the length of your vector: ");

	int size_of_vector;
	scanf("%d", &size_of_vector);

	//This is the solution because the problem requires
	int *v;
	v = (int *) malloc (size_of_vector * sizeof(int));

	//This is a normal solution (mine)
	int vector[size_of_vector];

	for (int i = 0; i < size_of_vector; i++){
		printf("Input an element of your int vector: ");
		//scanf ("%d", &vector[i]); //Part of my solution
		scanf ("%d", &v[i]);
	}

	for (int i = size_of_vector - 1; i >= 0; i -= 1){
		//printf("%d\n", vector[i]); //Part of my solution
		printf("%d\n", v[i]);
	}
}
