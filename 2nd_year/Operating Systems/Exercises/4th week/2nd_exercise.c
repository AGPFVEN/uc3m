#include<stdio.h>
#include<dirent.h>
#include <time.h>
#include <dirent.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>

int main(int argc, char *argv[]){
	char directory_name[100];
	DIR *directory;
	struct dirent *directory_content;

	//Recieve directory
	printf("Input the name of a directory: ");
	scanf("%s", &directory_name);
	
	/* //This is my solution
	//Get directory
	directory = opendir(directory_name);
	
	//Read directory content
	if (directory){

		while ((directory_content = readdir(directory)) != NULL){
			printf("%s\n", directory_content -> d_name);
		}

		closedir(directory);
	}
	return 0;*/

	//Professor solution
	int er;
	char nomdir[100], nomfich[100], resp[30];
	struct stat atr;
	DIR *d;
	struct dirent *rd1;
	time_t fecha;

	strcpy(nomdir, directory_name);

	if ((d=opendir(nomdir))==NULL) {
  		printf ("No existe ese directorio \n");
  		return -1;
	} else {
  		while (( rd1 =readdir(d)) != NULL) {
    			if ( (strcmp(rd1->d_name, ".")!=0 )&& (strcmp(rd1->d_name, "..")!=0 )){
      				strcpy (nomfich, nomdir);
      				strcat (nomfich, "/");
      				strcat (nomfich, rd1->d_name);
      				printf ("fichero :%s:", nomfich);
    			}
  		} /* while*/
  		
		closedir (d);
	}
}/* main*/
