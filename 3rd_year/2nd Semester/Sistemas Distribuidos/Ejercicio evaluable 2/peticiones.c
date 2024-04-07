#include "peticiones.h"

static long petid = 0;

void recibir_peticion (peticion_t * p) 
{
   int delay;
   fprintf(stderr, "Recibiendo petición\n");
   p->id = petid++;
  
   /* Simulación de tiempo de E/S */
   delay = rand() % 5;
   sleep(delay);

   fprintf(stderr,"Petición %ld recibida después de %d segundos\n", p->id, delay);
}

void responder_peticion (peticion_t * p) 
{
  int delay;
  char *mz;

  fprintf(stderr, "Enviando petición %ld\n", p->id);

  /* Simulación de tiempo de procesamiento */
  mz = malloc(1000000) ;
  for (int i=0; i<1000000; i++) { mz[i] = 0; }
  free(mz) ;

  /* Simulación de tiempo de E/S */
  delay = rand() % 20;
  sleep(delay);

  fprintf(stderr, "Petición %ld enviada después de %d segundos\n",  p->id, delay);
}