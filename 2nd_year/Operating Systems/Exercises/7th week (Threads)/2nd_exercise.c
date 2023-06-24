#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>

int MYGLOBAL = 0;

void *print_point(void *arg){
    int i, j;
    for (i = 0; i < 20; i++){
        j = MYGLOBAL;
        j += 1;
        printf(".");
        fflush(stdout);
        sleep(1);
        MYGLOBAL = j;
    }
    return NULL;
}

int main(){
    pthread_t th;
    int i;

    //Create thread
    if (pthread_create(&th, NULL, print_point, NULL) != 0){
        printf("Error at creating thread\n");
        abort();
    }

    //Concurrent operations
    for (i = 0; i < 20; i++){
        MYGLOBAL = MYGLOBAL + 1;
        printf("o");
        fflush(stdout);
        sleep(1);
    }

    //Join thread
    if (pthread_join(th, NULL) != 0){
        printf("Error at joining thread");
        abort();
    }

    printf("MYGLOBAL = %d\n", MYGLOBAL);
    exit(0);
}