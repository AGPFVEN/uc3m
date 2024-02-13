//P1-SSOO-23/24

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	/*If less than two arguments (argv[0] -> program, argv[1] -> file to process) print an error y return -1*/
	if(argc < 2)
	{
		printf("Too few arguments\n");
		return -1;
	}

	//Open file
	int fd = open(argv[1], O_RDONLY);
	if (fd == -1){
		printf("Error at opening file\n");
		return -1;
	}

	//Read file
	char* file_buffer = malloc(sizeof(char));
	read(fd, file_buffer, sizeof(char));

	printf("%s\n", file_buffer);

	return 0;
}

