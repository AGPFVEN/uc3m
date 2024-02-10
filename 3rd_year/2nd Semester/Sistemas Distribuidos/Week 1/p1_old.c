#include <stdio.h>

int main (int argc, char **argv)
{
	printf("Programa P1 \n");

    for(int a=0; a<argc; a++){
        printf("Argumento %d: %s\n", a + 1, argv[a]);
    }

	return 0;
}