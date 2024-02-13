#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>

void say_hi(){
    //Loop to say hi
    for (int i = 0; i < 3; i++){
        printf("hi, I am a thread 1\n");
        sleep(1);
    }

    //Say Bye
    printf("Bye\n");
}

int main(){
    //Declare thread
    pthread_t th1;

    //Initialize thread
    printf("Launching thread ...\n");
    if (pthread_create(&th1, NULL, (void*)say_hi, NULL) != 0){
        printf("Error at creating the thread\n");
        abort();
    }

    //Join thread
    printf("Joining thread ...\n");
    if (pthread_join(th1, NULL) != 0){
        printf("Error at joining the thread\n");
        abort();
    }
}