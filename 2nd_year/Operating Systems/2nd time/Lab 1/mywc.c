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
	int buffer_size = 1;
	char* buffer_file = malloc(sizeof(char) * buffer_size);
	ssize_t result;
	int n_lines = 0, n_words = 0, n_bytes = 0, in_word = 0;

	// loop to read and analyze file
	while ((result = read(fd, buffer_file, buffer_size)) != 0) {

		// read 1 byte or char of the file
		if ((result) == -1){

			printf("Error at reading file\n");
			return -1;

		}

		n_bytes++;

		// new line case
		if (*buffer_file == '\n'){
			n_lines++;
		}

		// anlyze word state
		if (in_word == 0){

			// start of a word
			if (!(*buffer_file < 32 || *buffer_file == 127)) {
				n_words++;
				in_word = 1;
			}	

		} else {

			// end of a word
			if (*buffer_file < 32 || *buffer_file == 127){
				in_word = 0;
			}

		}

	}	

	// print the result
	printf("%i %i %i %s\n", n_lines, n_words, n_bytes, argv[1]);

	return 0;
}

