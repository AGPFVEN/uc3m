#include <stdio.h>
#include <stdlib.h>
#include "lib-client.h"

int   N = 10 ;
char *A = "nombre" ;
int   E =  1 ;
int   V = 0x123 ;

int main ( int argc, char *argv[] ){
    int ret;

    // init
    if ((ret = d_init()) < 0) {
        printf("d_init: error code %d\n", ret) ;
        exit(-1) ;
    }

    // set
    /*double v1[3] = {-9.0, 20.0, 900.0};
    char v[] = "kkkkkkkkkkkkkkkkkk\no";
    ret = d_set(1, v, 3, v1);
    if (ret < 0) {
        printf("d_set: error code %d\n", ret) ;
        exit(-1) ;
    }*/
    //printf("d_set(\"%s\", %d, 0x%p)\n", A, E, v1) ;

    return 0;
}