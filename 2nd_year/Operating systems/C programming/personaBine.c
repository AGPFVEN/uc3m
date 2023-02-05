#include <stdio.h>
#include <string.h>
#include <stdlib.h>


/* Hola mundo */

int main (int argc, char ** argv) {

  char nombre[32];
  int edad;

  if (argc < 2)
  {
     printf("Usage:  persona <nombre> <edad> \n");
     exit(-1);
  }

  strcpy(nombre, argv[1]);
  edad = atoi (argv[2]);

  printf ("Nombre: %s  Edad: %d \n", nombre, edad);}
