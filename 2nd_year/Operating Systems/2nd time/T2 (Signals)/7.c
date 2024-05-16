#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>

#define SHARED_START 1
#define SHARED_FINISH 10

int main()
{
      int pid;

      pid = fork();

      if (pid == 0) // son
      {
            for (int i = SHARED_START; i < SHARED_FINISH; i++){
                  if ((i % 2) != 0){
                        pause();
                        i++;
                  }
                  else
                  {
                        printf("Printed by child %d\n", i);
                        i++;
                        kill(getppid(), SIGUSR1);
                  }
            }
      }
      else //father
      {
            for (int i = SHARED_START; i < SHARED_FINISH; i++){
                  if ((i % 2) == 0){
                        pause();
                        i++;
                  }
                  else
                  {
                        printf("Printed by father %d\n", i);
                        i++;
                        kill(pid, SIGUSR1);
                  }
            }
      }
}