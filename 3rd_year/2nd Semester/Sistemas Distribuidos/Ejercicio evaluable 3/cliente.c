#include <stdio.h>
#include <stdlib.h>

#include "claves.h"

int main(int argc, char *argv[])
{
	init();

	// set_value
	double *t;
	int size = 3;
	t = (double *)malloc(sizeof(double) * size);
	for (int i = 1; i < size; i++)
	{
		t[i] = (i + 1) * 5;
	}
	set_value(1, "holiwis", size, t);
	
	//get value 
	char *pp;
    double *p;
	int *size_g;
	size_g = (int *) malloc(sizeof(int));
    pp = (char *) malloc(sizeof(char) * 8);
    p = (double *) malloc(sizeof(double) * size);
    get_value(1, pp, size_g, p);
	printf("%f\n", p[2]);

	for (int i = 1; i < size; i++)
	{
		t[i] = i * 9;
	}
	modify_value(1, "hello there", size, t);
    get_value(1, pp, size_g, p);
	printf("%f\n", p[2]);

	printf("%i\n", exist(1));

	delete_key(1);

	printf("%i\n", exist(1));

	exit(0);
}