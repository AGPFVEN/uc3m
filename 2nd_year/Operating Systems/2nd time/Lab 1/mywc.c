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
	int n_lines = 0;
	int n_words = 0;
	int n_bytes = 0;

	// loop to read and analize file
	do{
		// read 1 byte or char of the file
		data = read(fd, buffer_file, buffer_size);
		if (data == -1){
			printf("Error at reading file\n");
			return -1;
		}

		n_bytes++;

		// analize the char
		if (*buffer_file == '\n'){

			n_lines++;
			n_words++;

		} else if (*buffer_file == ' ' || *buffer_file == '\t' ){

			n_words++;

		}

	} while (data == buffer_size * sizeof(char));
	

	// count first word
	if (n_words != 0){
		n_words++;
	}

	// discount last byte
	if (n_bytes != 0){
		n_bytes--;
	}

	// print the result
	printf("%i %i %i %s\n", n_lines, n_words, n_bytes, argv[1]);

	return 0;
}

