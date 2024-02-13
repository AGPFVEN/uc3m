#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#include<unistd.h>
#define BUFFSIZE 1 //Set size to read
#define PERM 0644

int copy_file(char *origin_file, char *destination_file){ 
	int input_file, output_file, nread;
	char buffer[BUFFSIZE];

	//Origin file
	if ((input_file = open(origin_file, O_RDONLY)) < 0) {
		printf("Error at openning origin file\n");
		return(-1);
	}

	//Destination file
	if ((output_file = open(destination_file, O_WRONLY | O_TRUNC | O_CREAT, PERM)) < 0){

		printf("Error at openning destination file\nClosing origin file ...\n");

		close(input_file);
		printf("Origin file closed\n");
		return (-2);
	}

	//Copy file from origin to destination in BUFFERSIZE steps
	while ((nread = read(input_file, buffer, BUFFSIZE)) > 0){
		if (write (output_file, buffer, nread) < 0){
			close(input_file);
			close(output_file);
			return (-3);
		}
	}

	if (nread == 1){
		return (-4); //Error at reading
	}

	close(input_file);
	close(output_file);
	printf("it worked\n");
	return(0);
}

int main(int argv, char* argc[]){
	copy_file("test1.txt", "output_file.txt");
}
