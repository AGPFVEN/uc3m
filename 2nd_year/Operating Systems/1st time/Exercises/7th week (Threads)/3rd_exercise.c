#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#define MAX_THREADS 10

typedef struct{
    int id;
} param ;

void *say_hi(void *arg){
    param *p = (param*)arg;
    printf("The thread number %d says hello :)\n", p->id);
    return (NULL);
}

int main(int argc, char *argv[]){
    int n, i;
    pthread_t *threads;
    pthread_attr_t pthread_custom_attr;
    param *p;

    n = atoi(argv[1]);
    
    if ((n < 1) || (n > MAX_THREADS)){
        printf("The number of threads should be between 1 and 10\n");
        return (-1);
    }

    threads = (pthread_t*) malloc (n * sizeof(*threads));
    pthread_attr_init(&pthread_custom_attr);
    p = (param*) malloc (n * sizeof(param));

    //Start thread
    for (i = 0; i < n; i++){
        p[i].id = i;
        pthread_create(&threads[i], &pthread_custom_attr, say_hi, (void*)(p + i));
    }

    for (i = 0; i < n; i++){
        pthread_join(threads[i], NULL);
    }
    
    free(p);
    return 0;
}