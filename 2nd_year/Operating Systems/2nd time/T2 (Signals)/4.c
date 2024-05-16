#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>

void f(int s)
{
      char msg[] = "Segmentation fault occurred\n";
      write(STDOUT_FILENO, msg, sizeof(msg));
      signal(SIGSEGV, SIG_DFL); //return to normal behaviour after execution of this function
      write(STDOUT_FILENO, msg, sizeof(msg));
}

int main()
{
      struct sigaction sa1;

      sa1.sa_flags = 0;
      sigemptyset(&(sa1.sa_mask));
      sa1.sa_handler = f;
      sigaction(SIGSEGV, &sa1, NULL);

      int* p;
      p=0;
      printf("Pointer put: %d\n", *p);
      *p= 5; //Not executed
      printf("Pointer put correctly: %d\n", *p);
}