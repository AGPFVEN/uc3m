#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>

void captureSignal (int s){
      printf("SIGNAL RECEIVED in child: %d\n", s);
}

int main()
{
      struct sigaction sa1;

      pid_t pid = fork();
      
      if (pid == 0) //hijo
      {
            sa1.sa_handler = captureSignal;
            sa1.sa_flags = 0;
            sigemptyset(&(sa1.sa_mask));
            sigaction(SIGUSR1, &sa1, NULL);
            pause();
      }
      else
      {
            sleep(10);
            kill(pid, SIGUSR1);
            exit(0);
      }
}