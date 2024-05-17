#include <stddef.h> /* NULL */
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>

int main (){
    int a=1;
    if(a == 1){
        a = 2;
    }
    if (a == 2){
        printf("h\n");
    }
}