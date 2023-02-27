#include<fcntl.h>
#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[]){

	//Check if arguments are passed
	if (argc < 2) {
		printf("No arguments were passed\n");
		return -1;
	}

	//Open the file using int that represents a file descriptor
	int fd = open(argv[1], O_WRONLY);

	//Error handling
	if(fd == -1) {
		perror("open");
		return -1;
	}
	printf("%d\n", fd);
	return 0;
}
