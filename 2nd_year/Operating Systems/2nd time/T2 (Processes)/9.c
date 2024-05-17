#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main (int argc, char *argv[]) 
{
	int num_proc, i, pid, status;

	num_proc = atoi(argv[1]);

	for (i=0; i<num_proc; i++) {
		pid = fork();
		if (pid == 0) {
                  printf("Child process of %i with PID: %i\n",i ,getpid()); 
                  //printf("%i\n",getpid()); 
            }
		else{
                  printf("parent process of %i with PID: %i\n", i, getpid()); 
                  //printf("%i\n",getpid()); 
		      wait (&status); 
            }
            //bucle esperando la finalización del hijo creado
	}
}