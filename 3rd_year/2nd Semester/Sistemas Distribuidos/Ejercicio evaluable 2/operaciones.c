#include "operaciones.h"

#define DB_PATH "BASEDEDATOS"

#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <string.h>
#include <errno.h>


int init(){
	// pointer to DIR object
	DIR *dir;

	// error has occurred
	if ((dir = opendir(DB_PATH)) == NULL){

		// file does not exist
		if (errno == ENOENT){
			printf("Creando directorio ...\n");
			mkdir(DB_PATH, 0777);
			return 0;

		// other cases
		} else {
			printf("Error abriendo %s\n", DB_PATH);
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
	if ((N_value2 < 1) || (N_value2 >32)){
		printf("Número de valores en tupla fuera de rango");
	}

	// name of file (key) to string
	char ckey[15];
	if (sprintf(ckey, "%d", key) < 0){
		printf("Error transformando int a string\n");
		return -1;
	}

	// path of files inside DB_PATH
	char path[sizeof(DB_PATH) + sizeof(ckey) + 12];	
	snprintf(path, sizeof(path),"./%s/%s.txt", DB_PATH, ckey);

	// check if file exists
	FILE *stream;
	if ((stream = fopen(path, "r")) != NULL){
		printf("key ya existe\n");
		return -1;
	}

	// create file
	if ((stream = fopen(path, "w")) == NULL){
		printf("Error abriendo archivo %s\n", path);
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

	// guardar floats
	char floatToString[328];
	for (int i = 0; i < N_value2; i++){	
		if (sprintf(floatToString, "%f,", V_value2[i]) < 0){
			printf("Error transformando int a string\n");
			return -1;
		}

		if (fputs(floatToString, stream) == EOF){
			printf("Error imprimiendo value1 en el archivo\n");
			return -1;
		}	
	}

	// cerrar archivo
	if (fclose(stream) == EOF){
		printf("Error cerrando el archivo\n");
		return -1;
	}
	return 0;
}


int get_value(int key, char *value1, int *N_value2, double *V_value2){
	// name of file (key) to string
	char ckey[15];
	if (sprintf(ckey, "%d", key) < 0){
		printf("Error transformando int a string\n");
		return -1;
	}

	// path of files inside DB_PATH
	char path[sizeof(DB_PATH) + sizeof(ckey) + 12];	
	snprintf(path, sizeof(path),"./%s/%s.txt", DB_PATH, ckey);

	// path of files inside DB_PATH
	FILE *stream;
	if ((stream = fopen(path, "r")) == NULL){
		printf("Error abriendo archivo %s\n", path);
		return -1;
	}

	// variables to transform str to int
	char buffer[5] = "";
	int ch;
	char bf[2];
	bf[1] = '\0';
	while ((ch = fgetc(stream)) != '\n'){
		bf[0] = ch;
		strncat(buffer, bf, 1);
	} 

	char *stopstring;
	int charCount = strtol(buffer, &stopstring, 10);

	// get value1
	for (int i = 0; i <= charCount; i++){
		ch = fgetc(stream);
		bf[0] = ch;
		*(value1 + i) = ch;
	}
	*(value1 + charCount) = '\0';	

	// get value 2
	char floatToString[328] = "";
	int i = 0;
	while ((ch = fgetc(stream)) != EOF){
		if(ch == ','){
			printf("%s\n", floatToString);
			V_value2[i] =  strtod(floatToString, &stopstring);
			printf("vv[%i] = %f\n", i, V_value2[i]);
			strcpy(floatToString, "");
			i++;
		} else {
			bf[0] = ch;
			strcat(floatToString, bf);
		}
	}

	fclose(stream);

	return 0;
}

int modify_value(int key, char *value1, int N_value2, double *V_value2){
	// name of file (key) to string
	char ckey[15];
	if (sprintf(ckey, "%d", key) < 0){
		printf("Error transformando int a string\n");
		return -1;
	}

	// path of files inside DB_PATH
	char path[sizeof(DB_PATH) + sizeof(ckey) + 12];	
	snprintf(path, sizeof(path),"./%s/%s.txt", DB_PATH, ckey);

	// check if file exists
	FILE *stream;
	if ((stream = fopen(path, "r")) == NULL){
		printf("key no existe\n");
		return -1;
	}

	// create file
	if ((stream = fopen(path, "w")) == NULL){
		printf("Error abriendo archivo %s\n", path);
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

	// guardar floats
	char floatToString[328];
	for (int i = 0; i < N_value2; i++){	
		if (sprintf(floatToString, "%f,", V_value2[i]) < 0){
			printf("Error transformando int a string\n");
			return -1;
		}

		if (fputs(floatToString, stream) == EOF){
			printf("Error imprimiendo value1 en el archivo\n");
			return -1;
		}	
	}

	// cerrar archivo
	if (fclose(stream) == EOF){
		printf("Error cerrando el archivo\n");
		return -1;
	}
	return 0;
}

int  delete_key(int key){
	// name of file (key) to string
	char ckey[15];
	if (sprintf(ckey, "%d", key) < 0){
		printf("Error transformando int a string\n");
		return -1;
	}

	// path of files inside DB_PATH
	char path[sizeof(DB_PATH) + sizeof(ckey) + 12];	
	snprintf(path, sizeof(path),"./%s/%s.txt", DB_PATH, ckey);

	// check if file exists
	FILE *stream;
	if ((stream = fopen(path, "r")) == NULL){
		printf("key no existe\n");
		return -1;
	}

	remove(path);

	return 0;
}


int exist(int key){
	// name of file (key) to string
	char ckey[15];
	if (sprintf(ckey, "%d", key) < 0){
		printf("Error transformando int a string\n");
		return -1;
	}

	// path of files inside DB_PATH
	char path[sizeof(DB_PATH) + sizeof(ckey) + 12];	
	snprintf(path, sizeof(path),"./%s/%s.txt", DB_PATH, ckey);

	// check if file exists
	FILE *stream;
	if ((stream = fopen(path, "r")) == NULL){
		printf("key no existe\n");
		return 0;
	}
	
	return 1;
}