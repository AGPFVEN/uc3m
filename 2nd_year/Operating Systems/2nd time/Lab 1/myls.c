//P1-SSOO-23/24

#include <stdio.h>		// Header file for system call printf
#include <unistd.h>		// Header file for system call gtcwd
#include <sys/types.h>	// Header file for system calls opendir, readdir y closedir
#include <dirent.h>
#include <string.h>


int main(int argc, char *argv[])
{
	// string containing path 
	char *given_path;

	// select path
	if (argc < 2){
		given_path = "./";
	} else {
		given_path = argv[1];
	}

	// pointer to DIR object
	DIR *dir;

	// open directory
	dir = opendir(given_path);
	if (dir == NULL){
		printf("Error at openning directory '%s'\n", given_path);
		return -1;
	}

	// dirent structure indicating next directory entry
	struct dirent  *entry;

	// read contents of directory
	while ((entry = readdir(dir)) != NULL){
		printf("%s\n", entry->d_name);
	}

	// close directory
	closedir(dir);

	return 0;
}

