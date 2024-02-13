#include <fcntl.h>
#include <wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>
#include <time.h>
#include <pthread.h>

int main(int argc, char *argv[]){
    char p[2][3][10];

    strcpy(p[0][0], "one more");
    strcpy(p[0][1], "two");
    strcpy(p[0][2], "three");
    strcpy(p[1][0], "four");
    strcpy(p[1][1], "five");
    strcpy(p[1][2], "six");

    printf("message: %s\nsize: %ld\n", *p[0], sizeof(p[0]));

    char *aux;
    
    aux = (char*) malloc(sizeof(p[0]));

    for (long int i = 0; i == sizeof(p[0]) -1; i++){
        printf("i: %ld, p: %ld, message: %s\n", i, sizeof(p[0]), aux);
        strcat(aux, p[0][i]);
    }
    printf("final message: %s\n", aux);
}