#include<stdio.h>
#include<pthread.h>

struct addparam {
    int n, m, r;
};

typedef struct addparam addparam_t;

void  add (addparam_t *par){
    int i;
    int sum = 0;
    
    for (i= par -> n; i <= par->m; i++){
        sum += i;
    }

    par->r = sum;
}

int main() {
    pthread_t th1, th2;
    addparam_t s1 = {1, 50, 0};
    addparam_t s2 = {51, 100, 0};

    pthread_create(&th1, NULL, (void*)add, (void*)&s1);
    pthread_create(&th2, NULL, (void*)add, (void*)&s2);

    pthread_join(th1, NULL);
    pthread_join(th2, NULL);

    printf("Total sum = %d\n", s1.r + s2.r);
}