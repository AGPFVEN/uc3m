#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h>
#define NUMTH 10

int total_sum = 0;

void *sum(void *arg){
    int sum = total_sum;
    sum = sum + 100;
    //sleep(1);
    printf("Pthread = %d awakes, Total sum = %d\n", (int)pthread_self(), sum);
    total_sum = sum;
}

int main(int argc, char *argv[]){
    //Create thread id
    pthread_t th[NUMTH];

    //Create threads
    for (int i = 0; i < NUMTH; i++){
        pthread_create(&th[i], NULL, (void*)sum, NULL);
    }

    //Join threads
    for (int i = 0; i < NUMTH; i++){
        pthread_join(th[i], NULL);
    }

    //Final sum
    printf("Final sum = %d\n", total_sum);

    //When the sleep function is put in place the sum is equal to 100
    //When the sleep function is not put in place the sum is inconsistent (500 - 900)
}