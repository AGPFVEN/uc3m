#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void *printer(void * th_args)
{
      for (int i = 0; i < 3; i++){
            printf("Thread says hi!\n");
            sleep(1);
      }
      printf("Thread says bye!\n");
}

int main(){
      pthread_t th1;
      pthread_attr_t attr;

      pthread_attr_init(&attr);
      pthread_create(&th1, &attr, printer, NULL);
      pthread_join(th1, NULL);
      printf("Main process says bye!\n");
}