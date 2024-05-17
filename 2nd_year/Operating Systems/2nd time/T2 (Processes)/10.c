#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>

int main(int argc, char* argv[])
{
      int pid, i, m=10;
      int tiempo_inicial, tiempo_actual;
      tiempo_inicial = time(NULL);
      tiempo_actual = time(NULL) - tiempo_inicial;
      printf("%d: Inicio del programa \n", tiempo_actual);
      for (i=0; i<3; i++)
      {
            pid = fork();
            sleep(1);
            switch(pid){
                  case -1:
                        perror("Error at creating process");
                        exit(-1);
                  case 0:
                        m++;
                        tiempo_actual = time(NULL) - tiempo_inicial;
                        printf("%d: Hijo %d m=%d\n", tiempo_actual, i, m);
                        sleep(2);
                        exit(0);
                  default:
                        tiempo_actual = time(NULL) - tiempo_inicial;
                        printf("%d: creado el proceso %d\n", tiempo_actual, i);
                        if (i%2 == 0){
                              wait(NULL);
                              tiempo_actual = time(NULL) - tiempo_inicial;
                              printf("%d: Finalizo un proceso, valor de m=%d\n", tiempo_actual, m);
                        }
            }
      }
      wait(NULL);
      tiempo_actual = time(NULL) - tiempo_inicial;
      printf("%d: finalizo in proceso, valor de m=%d\n", tiempo_actual, m);
}