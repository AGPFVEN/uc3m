#include<stdio.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<fcntl.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char *argv[]){
	//Check if there's enough arguments
	if (argc < 2){
		printf("Not enough arguments\n");
	}
	
	//Pipe varibles
	int fd[2];
	char buf[1024];

	//Process varibales
	pid_t pid = fork();
	int status;

	if (pid == 0){
		//Redirect output
		close(fd[0]);
		dup2(fd[1], STDOUT_FILENO);
		
		//Execute command
		execvp(argv[1], &argv[1]);

		//Manage Output part of the pipe
		close(fd[1]);
		while(read(fd[0], buf, sizeof(buf)) > 0) {
			printf("%s", buf);
		}
		close(fd[0]);

		exit(0);
	}
	
	wait(NULL);
}
