#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#include<unistd.h>
#define BUFFERSIZE 1

int main(int argc, char* argv[]){
    int input_file, nread;
    char buffer[BUFFERSIZE];

    //Open file
    if ((input_file = open(argv[1], O_RDONLY)) < 0){
        printf("Error at opennig origin file\n");
        return (-1);
    }

    //Read and print file
    while ((read(input_file, buffer, BUFFERSIZE)) > 0){
        printf("%s", buffer);
    }

    close(input_file);
    return (0);
}

/* This is the proffesor solution but it's practically the same
int main(int argc, char *argv[]){
	char file_name[50], buffer[BUFFERSIZE];
	int file_descriptor;
	ssize_t bytes_read;

	printf("Enter a file name: ");
	scanf("%s", file_name);

	//Openning
	if ((file_descriptor = open(file_name, O_RDONLY)) < 0){
		printf("Error at openning the file\n");
		return (-1);
	}

	//Reading
	while ((bytes_read = read(file_descriptor, buffer, BUFFERSIZE)) > 0){
		//Writing
		printf("%s", buffer);
	}

	if (bytes_read == 1){
		printf("Error at reading the file\n");
		return (-1);
	}

	close(file_descriptor);
}
*/