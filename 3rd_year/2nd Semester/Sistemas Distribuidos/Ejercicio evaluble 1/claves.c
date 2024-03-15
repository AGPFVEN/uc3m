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

	// check if key is inside the range
	if ((key < 1) || (key >32)){
		printf("key está fuera de rango");
	}

	// name of file (key) to string
	char ckey[32];
	if (sprintf(ckey, "%d", key) < 0){
		printf("Error transformando int a string\n");
		return -1;
	}

	// path of files inside DB_PATH
	char path[256];	
	snprintf(path, strlen(DB_PATH) + 32 + 7,"./%s/%s.txt", DB_PATH, ckey);

	// check if file exists
	FILE *stream;
	if ((stream = fopen(path, "r")) != NULL){
		printf("key ya existe\n");
		return -1;
	}

	// create file
	if ((stream = fopen(path, "w")) == NULL){
		printf("Error abriendo archivo\n");
		return -1;
	}

	// put in file size of string
	if (sprintf(ckey, "%ld\n", strlen(value1)) < 0){
		printf("Error transformando int a string\n");
		return -1;
	}

	// number of chars in string (of value1)
	if (fputs(ckey, stream) == EOF){
		printf("Error imprimiendo número de carácteres de value1 en el archivo\n");
		return -1;
	}

	// store value1
	if (fputs(value1, stream) == EOF){
		printf("Error imprimiendo value1 en el archivo\n");
		return -1;
	}
	if (fputs("\n", stream) == EOF){
		printf("Error imprimiendo value1 en el archivo\n");
		return -1;
	}

	//store numbers
	for (int i = 0; i < N_value2; i++){	
		if (sprintf(ckey, "%f,", V_value2[i]) < 0){
			printf("Error transformando int a string\n");
			return -1;
		}

		if (fputs(ckey, stream) == EOF){
			printf("Error imprimiendo value1 en el archivo\n");
			return -1;
		}	
	}

	fclose(stream);

	//read
	if ((stream = fopen(path, "r")) == NULL){
		printf("Error abriendo archivo\n");
		return -1;
	}

	char buffer[5] = "";
	int ch;
	char bf[2];
	while ((ch = fgetc(stream)) != '\n'){
		bf[0] = ch;
		strncat(buffer, bf, 1);
	} 

	char *stopstring;
	int charCount = strtol(buffer, &stopstring, 10);

	for (int i = 0; i <= charCount; i++){
		ch = fgetc(stream);
		bf[0] = ch;
	}

	printf("ho\n");
	int o = charCount;
	while ((ch = fgetc(stream)) != EOF){
		bf[0] = ch;
		printf("%s %i\n", bf, o);
		o++;
	}

	fclose(stream);

	return 0;
}