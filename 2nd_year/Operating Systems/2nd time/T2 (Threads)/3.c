#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

int myglobal = 0;

void* print_point(void* p)
{
      int a;
      for (int i = 0; i < 20; i++){
            a = myglobal;
            a++;
            printf(".");
            sleep(1);
            myglobal = a;  
      }
}

int main()
{
      pthread_t th1;
      pthread_attr_t attr;

      pthread_attr_init(&attr);
      pthread_create(&th1, &attr, print_point, NULL);
      //pthread_join(th1, NULL);

      for (int i = 0; i < 20; i++){
            myglobal++;
            sleep(1);
            printf("m");
      }

      pthread_join(th1, NULL);

      printf("\nmyglobal: %d\n", myglobal);
}