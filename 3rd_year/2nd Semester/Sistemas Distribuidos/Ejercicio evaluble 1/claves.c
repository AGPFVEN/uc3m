#include "claves.h"

#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>

int init()
{
	// pointer to DIR object
	DIR *dir;
    int dfd = dirfd(dir);
    mkdirat(dfd, "/BASEDEDATOS", S_IRWXU);

	// open directory
	dir = opendir("./BASEDEDATOS/");
	if (dir == NULL){
        mkdirat(dir, "/BASEDEDATOS", S_IRWXU);
		printf("Error at openning Database (directory representing the database)\n");
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