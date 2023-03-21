#include<stdio.h>
#include<unistd.h>

int main(int argc, char *argv[]){
	int  pid;

	pid = fork();

	if (pid == 0) {
		printf("I am the son process\n");
		printf("pid = %d, ppid = %d\n", getpid(), getppid());
		printf("Bye father\n");
	} else {
		sleep(1);
		printf("I am the father\n");
		printf("pid = %d, ppid = %d\n", getpid(), getppid());
		printf("Bye son\n");
	}
}
//If the sleep() function is not written the parent ends before the child, it shows that the new
//parent of the child is process 1 (init). That is beacause when the father dies, init adopts the
//son so that it does not become a zombie.
