#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char* argv[])
{
      pid_t pid;
      int i = 0;

      while (i < 3)
      {
            pid = fork();

            switch (pid)
            {
                  case -1:
                        perror("Error al crear el proceso hijo\n");
                        exit(-1);

                  case 0:
                        printf("Hola, soy el proceso %d\n", getpid());

                        if ((i % 2) == 0){
                              i++;
                        } else {
                              i--;
                        }

                  default:
                        i++;
                        break;
            }
      }
}