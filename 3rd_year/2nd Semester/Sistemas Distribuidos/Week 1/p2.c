#include <stdio.h>
#include <stdlib.h>


int main (int argc, char **argv)
{
	printf("Programa P1 \n");

    long ret;
    char *end;

    for(int i=1; i<argc; i++){

        ret = strtol(argv[i], &end, 10);
        printf("Argumento %d: ", i + 1);

        if(*end != '\0'){
            printf("Error de conversión\n");
	        exit(-1);
        } else {
            printf("%ld\n", ret);
        }
    }

	return 0;
}