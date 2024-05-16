#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>

void f1(int s)
{
      char msg[] = "Signal 1 has been called\n";
      write(STDOUT_FILENO, msg, sizeof(msg));
}

void f2(int s)
{
      char msg[] = "Signal 2 has been called\n";
      write(STDOUT_FILENO, msg, sizeof(msg));
}

int main()
{
      struct sigaction sa1, sa2;

      sa1.sa_flags = 0;
      sa2.sa_flags = 0;

      sigemptyset(&(sa1.sa_mask));
      sigemptyset(&(sa2.sa_mask));

      sa1.sa_handler = f1;
      sa1.sa_handler = f2;

      sigaction(SIGUSR1, &sa1, NULL);
      sigaction(SIGUSR2, &sa2, NULL);
}