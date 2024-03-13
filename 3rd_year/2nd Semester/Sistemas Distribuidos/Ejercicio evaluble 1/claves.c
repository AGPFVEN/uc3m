#include "claves.h"

#define DB_PATH "BASEDEDATOS"

#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <string.h>
#include <errno.h>


int test(){
	return 0;
}

int init(){
	// pointer to DIR object
	DIR *dir;

	// error has occurred
	if ((dir = opendir(DB_PATH)) == NULL){

		// file does not exist
		if (errno == ENOENT){
			printf("Creating directory\n");
			mkdir(DB_PATH, 0777);
			return 0;

		// other cases
		} else {
			printf("Error at opening %s", DB_PATH);
			return -1;
		}
	}
	
	// dirent structure indicating next directory entry
	struct dirent  *entry;

	// path of files inside DB_PATH
	char path[256];

	// remove each file from directory
	while ((entry = readdir(dir)) != NULL){

		// check if they are sensitive directories
		if(!((strcmp(entry->d_name, ".") == 0) || (strcmp(entry->d_name, "..") == 0))){

			// get file name
			snprintf(path, strlen(DB_PATH) + strlen(entry->d_name) + 4,"./%s/%s", DB_PATH, entry->d_name);

			// remove file
			remove(path);
		}
	}

	// close directory
	closedir(dir);

	return 0;
}

int set_value(int key, char *value1, int N_value2, double *V_value2){

	//printf("%ld\n", sizeof(*V_value2)/sizeof(V_value2[2])); //check

	// check if key is inside the range
	if ((key < 1) || (key >32)){
		printf("key está fuera de rango");
	}

	FILE *stream;

	char ckey[32];
	sprintf(ckey, "%d", key);

	// path of files inside DB_PATH
	char path[256];	
	snprintf(path, strlen(DB_PATH) + 32 + 7,"./%s/%s.txt", DB_PATH, ckey);

	// check if file exists
	if ((stream = fopen(path, "r")) != NULL){
		printf("key ya existe\n");
		return -1;
	}

	// create file
	if ((stream = fopen(path, "w")) == NULL){
		printf("Error abriendo archivo\n");
		return -1;
	}

	// put in file
	char nchar[4];
	sprintf(nchar, "%ld ", strlen(value1));

	if (fputs(nchar, stream) == EOF){
		printf("Error imprimiendo en el archivo\n");
		return -1;
	}

	if (fputs(value1, stream) == EOF){
		printf("Error imprimiendo en el archivo\n");
		return -1;
	}
	
	if (fputs("\n", stream) == EOF){
		printf("Error imprimiendo en el archivo\n");
		return -1;
	}

	//store numbers

	fclose(stream);

	return 0;
}