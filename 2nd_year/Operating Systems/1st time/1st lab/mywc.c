#include<fcntl.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char *argv[]){

	//Check if arguments are passed
	if (argc < 2) {
		printf("No arguments were passed\n");
		return -1;
	}

	//Open the file using int that represents a file descriptor
	int fd = open(argv[1], O_RDONLY);

	//Error handling
	if(fd == -1) {
		perror("open");
		return -1;
	}

	//Declaring ints
	int lines;
	int words;
	int bytes;
	char buffer[1];

	//Reading file and increasing
	ssize_t byte_read = read(fd, buffer, sizeof(buffer));
	printf("%c", buffer[0]);

	while (byte_read != 0 && byte_read != -1){
		byte_read = read(fd, buffer, sizeof(buffer));
		lseek(fd, 0, SEEK_CUR);
		printf("%c", buffer[0]);
		if (buffer[0] == '\n'){
			printf("enter new line");
		}
	}

	close(fd);

	//printf("%c\n", buffer[0]);
	return 0;
}
