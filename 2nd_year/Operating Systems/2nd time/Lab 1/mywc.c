//P1-SSOO-23/24

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	/*If less than two arguments (argv[0] -> program, argv[1] -> file to process) print an error y return -1*/
	if(argc < 2){
		printf("Too few arguments\n");
		return -1;
	}

	// open file
	int fd = open(argv[1], O_RDONLY);
	if (fd == -1){
		printf("Error at opening file\n");
		return -1;
	}

	// declare variables in order to read file
	char* buffer_file = malloc(sizeof(char));
	int buffer_size = 1;
	ssize_t data;

	// read
	do{
		data = read(fd, buffer_file, buffer_size);
		printf("%s\n", buffer_file);
	} while (data == buffer_size * sizeof(char));

	return 0;
}

