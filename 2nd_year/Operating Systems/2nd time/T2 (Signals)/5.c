#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>

void f(int s){
      char msg[] = "Signal captured\n";
      write(STDOUT_FILENO, msg, sizeof(msg));
}

void f1(int s){
      char msg[] = "Child signal captured\n";
      write(STDOUT_FILENO, msg, sizeof(msg));
}

int main()
{
      int pid; 

      /*This would make the program to behave the same
            but the the son and father would bahave the same if sigusr1 were sent*/
      //struct sigaction sa1;
      //sa1.sa_flags = 0;
      //sigemptyset(&(sa1.sa_mask));

      pid = fork();

      if (pid == 0) // son
      {
            char msg[] = "Child initialized\n";
            write(STDOUT_FILENO, msg, sizeof(msg));
            sleep(2);
            kill(getppid(), SIGUSR1);
            sleep(3);
            char msg1[] = "Child exit\n";
            write(STDOUT_FILENO, msg1, sizeof(msg1));
      }
      else // father
      { 
            //In this way only father would react to sigusr1
            struct sigaction sa1;
            sa1.sa_flags = 0;
            sigemptyset(&(sa1.sa_mask));
            sa1.sa_handler = f;
            sigaction(SIGUSR1, &sa1, NULL);

            //Only applies to father
            struct sigaction sa2;
            sa2.sa_flags = 0;
            sigemptyset(&(sa2.sa_mask));
            sa2.sa_handler = f1;
            sigaction(SIGCHLD, &sa2, NULL);

            pause();
            pause();
      }
}