#include "claves.h"

int init()
{
    // crear archivo
    FILE *file;
    char file_name[] = "BASE-DE-DATOS";

    // open file
    file = fopen(file_name, "w");

    //close file
    fclose(file);

    return 0;
}