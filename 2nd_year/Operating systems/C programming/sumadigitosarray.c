#include<stdio.h>
#include<stdlib.h>
int main (int argc, char ** argv){
	//Declarations of vatiables
	int v[10];
	int sum = 0;
	int i;
	
	//Get values for vector
	for(i = 0; i < 10; i++){
		v[i] = atoi(argv[i]);
		printf("%d", v[i]);
	}

	return 0;
}
