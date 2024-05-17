#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>

int hijo()
{
      int numleido = 1;
      printf("Introduce un numero: (del 0 a 255)\n");
      scanf("%d", &numleido);
      exit(numleido);
}

int main(int argc, char* argv[])
{
      int pid, estado, hijomuerto, numescrito = 1;

      pid = fork();

      if (pid ==0) //child
      {
            hijo();
      }
      else //parent
      {
            printf("%d\n", numescrito);
            sleep(1);
            numescrito++;
            hijomuerto = waitpid(pid, &estado, WNOHANG);

            if (hijomuerto == pid)
            {
                  numescrito = WEXITSTATUS(estado);
                  pid = fork();
                  if (pid == 0)
                  {
                        hijo();
                  }
            }
      }
}