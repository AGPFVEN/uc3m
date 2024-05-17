#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char* argv[])
{
      pid_t pid1, pid2;
      int array[] = {9, 72, 5, 50}; 
      int Suma1, Resta2, Total, status;

      pid1 = fork();

      switch(pid1)
      {
            case 0: //hijo
                  pid2 = fork();

                  switch (pid2)
                  {
                        case 0: //nieto
                              Suma1 = array[0] + array[1];
                              printf("suma1 = %d\n", Suma1);
                              exit(Suma1);

                        default: // hijo
                              while (pid2 == wait (&status));
                              Resta2 = WEXITSTATUS(status) - array[2];
                              printf("resta2 = %d, estado = %d\n", Resta2, WEXITSTATUS(status));
                              exit(Resta2);
                  }
            
            default: //Proceso 3
                  while (pid1 == wait(&status));
                  Total = array[3] * WEXITSTATUS(status);
                  printf("Total = %d, estado = %d\n", Total, WEXITSTATUS(status));
                  exit(0);
      }
}