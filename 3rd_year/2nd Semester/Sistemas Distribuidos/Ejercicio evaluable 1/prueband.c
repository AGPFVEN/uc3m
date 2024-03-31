#include "claves.h"
#include <stdlib.h>

int main (int argc, char *argv[])
{
    double v1[3] = {-9.0, 20.0, 900.0};

    set_value(1, "kkkkkkkkkkkkkkkkkk\no", 3, v1);

    char *stringRes = "ooo";
    stringRes = (char*) malloc(256 * sizeof(char));
    int* k; 
    k = (int*) malloc(sizeof(int));
    double *v2;
    v2 = (double*) malloc(32 * sizeof(double));
    get_value(1, stringRes, k, v2);
    printf("%i\n", *k);
    printf("%c\n", stringRes[19]);
    printf("%f\n", v2[2]);
    
    double v3[4] = {-9.0, 20.0, 900.0, 400000.0};
    
    modify_value(1, "un\nvalor", 4, v3);
    get_value(1, stringRes, k, v2);
    printf("%i\n", *k);
    printf("%c\n", stringRes[0]);
    printf("%f\n", v2[3]);

    delete_key(1);

    return 0;
}