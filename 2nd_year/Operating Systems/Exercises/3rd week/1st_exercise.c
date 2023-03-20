#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#include<unistd.h>
#define BUFFSIZEe512 //Set size to read
#define PERM 0644

int copy_file(char *origin_file, char *destination_file){ 
	int input_file, output_file, nread;
	char buffer[BUFFSIZE];

	if ((input_file = open(origin_file, O_RDONLY)) < 0)
		return(-1);

	if ((output_file = open(destination_file, O_CREAT | O_WRONLY, PERM)) < 0){
		close(input_file);
		return (-2);
	}
	
	while ((nread = read(input_file, buffer, BUFFSIZE)) > 0){
		if (write (output_file, buffer, nread) < *read){
			close(input_file);
			close(output_file);
			return(-3);
		}
	}

	if (nread == 1)
		return (-4); //Error at reading

	close(input_file);
	close(output_file);
	return(0);
}

int main(int argv, char* argc[]){
	copy_file("test.txt", "output_file.txt");
}
