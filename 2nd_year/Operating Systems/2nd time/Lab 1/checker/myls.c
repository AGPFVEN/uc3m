//P1-SSOO-23/24

#include <stdio.h>		// Header file for system call printf
#include <unistd.h>		// Header file for system call gtcwd
#include <sys/types.h>	// Header file for system calls opendir, readdir y closedir
#include <dirent.h>
#include <string.h>


int main(int argc, char *argv[])
{
	// string containing path 
	char *givenPath;

	// select path
	if (argc < 2){
		givenPath = "./";
	} else {
		givenPath = argv[1];
	}

	// pointer to DIR object
	DIR *dir;

	// open directory
	dir = opendir(givenPath);
	if (dir == NULL){
		printf("Error at openning directory '%s'\n", givenPath);
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

