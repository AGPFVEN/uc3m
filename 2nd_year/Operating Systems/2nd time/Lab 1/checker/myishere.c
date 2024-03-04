//P1-SSOO-23/24

#include <stdio.h>
#include <sys/types.h>
#include <dirent.h>
#include <string.h>


int main(int argc, char *argv[])
{
	/* If less than three arguments (argv[0] -> program, argv[1] -> directory to search, argv[2] -> file to find) print an error y return -1 */
	if(argc < 3)
	{
		printf("Too few arguments\n");
		return -1;
	}

	// pointer to DIR object
	DIR *dir;

	// open directory
	dir = opendir(argv[1]);
	if (dir == NULL){
		printf("Error at openning directory \n");
		return -1;
	}

	// dirent structure indicating next directory entry
	struct dirent  *entry;

	// integer that works as a bool to check if the condition is complete
	int checker = 0;

	// read contents of directory
	while (((entry = readdir(dir)) != NULL) && checker != 1){
		
		// check if entry name (name of file) is equal to argument
		if (strcmp(entry->d_name, argv[2]) == 0){
			checker++;
		}

	}

	// print result
	if (checker == 0){
		printf("File %s is not in directory %s\n", argv[2], argv[1]);
	} else {
		printf("File %s is in directory %s\n", argv[2], argv[1]);
	}

	// close directory
	closedir(dir);

	return 0;
}
