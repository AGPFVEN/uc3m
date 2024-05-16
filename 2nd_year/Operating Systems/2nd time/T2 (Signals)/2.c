#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>

#define _GNU_SOURCE

int finTiempo = 0;

void captureSignal(int s)
{
      char msg[20];
      sprintf(msg, "Signal received: %d\n", s);
      write(STDOUT_FILENO, msg, sizeof(msg));
      finTiempo = 1;
}

int main()
{
      struct sigaction sa1;
      int i, faltan;

      sa1.sa_handler = captureSignal;
      sa1.sa_flags = 0;
      sigemptyset(&(sa1.sa_mask));
      sigaction(SIGALRM, &sa1, NULL);

      alarm(3);
            printf("Give a number (you have 3 seconds)\n");
            scanf("%d", &i);
            if (finTiempo)
                  printf("Time passed\n");
            else
                  printf("number read %d\n", i);
}