#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void *f(void *arg)
{
      printf("Execution initiated\n");
      int *v;

      // Access first 3 arguments 
      v = (int*)arg;
      printf("TH args values: %d, %d, %d\n", v[0], v[1], v[2]);
      printf("End execution of threads\n");
}

int main()
{
      pthread_attr_t attr;
      pthread_t thid;

      int args[] = {11, 22, 33, 44};
      
      printf("In main: %d, %d, %d\n", args[0], args[1], args[2]);

      pthread_attr_init(&attr);
      pthread_create(&thid, &attr, f, (void *) args);
      pthread_join(thid, NULL);
}