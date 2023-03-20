#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>

int main(int argc, char *argv[]){
	int file_descriptor;
	char test_string[] = "This is the first test string\n";
	char test_string2[] = "This is the second test string\n";
	
	//Create file
	if ((file_descriptor = open("test_file.txt", O_CREAT | O_WRONLY)) < 0){
		printf("Error creating the file\n");
	}

	//Jump 100 bytes beyond the end of the created file
	/*//This is my solution
	lseek(file_descriptor, 100, SEEK_END);

	write(file_descriptor, test_string, sizeof(test_string));
	*/
	
	//This is my professors solution
	if (write(file_descriptor, test_string, sizeof(test_string)) < 0){
		printf("Error at writing the first test string\n");
		return (-1);
	}

	if (lseek(file_descriptor, 100, SEEK_END) < 0){
		printf("Error at lseek\n");
		return (-1);
	}

	if (write(file_descriptor, test_string2, sizeof(test_string2)) < 0){
		printf("Error at writing the second test string\n");
		return (-1);
	}
}
