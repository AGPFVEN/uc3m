#include<stdio.h>

void add_one(int *integer){
	*integer += 1;
}

int main(int argc, char *argv[]){
	int main_integer = 5;

	add_one(&main_integer);

	printf("%d\n", main_integer);
}
