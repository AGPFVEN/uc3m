#ifndef LIB_CLIENT_H
#define LIB_CLIENT_H

   // Inicializar un array distribuido de N números enteros.
   int d_init () ;

   // Inserta el valor en la posición i del array nombre.
   int d_set (int key, char *value1, int N_value2, double *V_value2);

   // Recuperar el valor del elemento i del array nombre. 
   int d_get (char *nombre, int i, int *valor);

#endif