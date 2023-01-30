#include<stdio.h>

int main () {
	long int num=9;
	int num1;
	double r=5.1; 
	printf ("; %ld;  ; %4ld;  ; %-4ld;  ; %6.4ld;  ; %2d; \n", num, num, num, num, num1);
	printf ("; %f;  ; %9f;  ; %-9f;  ; %9.4f;  ; %2f;  \n", r, r, r, r, r);
	printf ("; %c;  ; %s;  ; %7s;  ; %-7s;  ; %7.4s; \n", 'a', "uno", "dos", "tres", "cuatro");

	printf ("dar numeros separados por ; \n");
	scanf ("%d; %ld", &num1, &num);
	printf ("; %d; ; %ld; \n", num1, num);

}
