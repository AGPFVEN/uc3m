#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv)
{
      int pid = fork();

      if (pid == 0)
      {
            printf("Child process with PID: %i\n", getpid()); 
      }
      else
      {
            sleep(2);
            printf("Parent process with PID: %i\n", getpid()); 
      }
}