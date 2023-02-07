#include<stdio.h>
#include<stdlib.h>

double sumnumbers (double f1, double f2) {
	return (f1 + f2);
}

int main(int argc, char **argv){
	float fI1 = atof(argv[1]);
	float fI2 = atof(argv[2]);

	float sum = sumnumbers(fI1, fI2);
	
	printf("%lf\n", sum);
	return 0;
}

