#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>

#define SHARED_START 1
#define SHARED_FINISH 10

void f(int s)
{
      char msg[] = "Child signal recieved\n";
      write(STDOUT_FILENO, msg, sizeof(msg));
}
void f1(int s)
{
      char msg[] = "father signal recieved\n";
      write(STDOUT_FILENO, msg, sizeof(msg));
}

int main()
{
      int pid;
      struct sigaction sa1;
      sa1.sa_flags = 0;
      sigemptyset(&(sa1.sa_mask));

      pid = fork();

      if (pid == 0) // son
      {
            sa1.sa_handler = f;
            sigaction(SIGUSR2, &sa1, NULL);
            for (int i = SHARED_START + 1; i < SHARED_FINISH; i++){
                  if ((i % 2) != 0){
                        pause();
                  }
                  else
                  {
                        printf("Printed by child %d\n", i);
                        kill(getppid(), SIGUSR1);
                  }
            }
            printf("Child end\n");
            exit(0);
      }
      else //father
      {
            sa1.sa_handler = f1;
            sigaction(SIGUSR1, &sa1, NULL);
            for (int i = SHARED_START; i < SHARED_FINISH; i++){
                  if ((i % 2) == 0){
                        pause();
                  }
                  else
                  {
                        printf("Printed by father %d\n", i);
                        kill(pid, SIGUSR2);
                  }
            }
            wait(NULL);
      }
}