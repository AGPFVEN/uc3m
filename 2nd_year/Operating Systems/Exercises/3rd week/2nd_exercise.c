#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
#define BUFFERSIZE 512

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
