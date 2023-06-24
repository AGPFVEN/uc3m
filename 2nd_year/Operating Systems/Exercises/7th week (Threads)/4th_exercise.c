#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>

//Function that prints id and wait 2 secs to end
void *show_identity2(void *arg){
    printf("I am the first thread and I will wait 1 sec\n");
    sleep(2);
    printf("I am the first thread and I finished waiting\n");
    return NULL; } //Function that prints id and wait 2 secs to end

void *show_identity5(void *arg){
    printf("I am the second thread and I will wait 5 sec\n");
    sleep(5);
    printf("I am the second thread and I finished waiting\n");
    return NULL;
}

int main(int argc, char *argv[]){
    pthread_t th1, th2;
    pthread_attr_t pthread_custom_attr;
    pthread_attr_init(&pthread_custom_attr);

    pthread_create(&th1, &pthread_custom_attr, show_identity2,(void*)NULL);
    pthread_create(&th2, &pthread_custom_attr, show_identity5,(void*)NULL);

    pthread_join(th1, NULL);
    pthread_join(th2, NULL);

    return 1;
}