#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#define MAX_THREAD 10

typedef struct {
      int id;
} param;

void* f(void* args)
{
      param* p = (param*) args;
      printf("Hello from thread n%d\n", p->id); 
      return (NULL);
}

int main(int argc, char* argv[])
{
      if (argc < 2){
            printf("Need to enter a num!\n");
            return -1;
      }

      int th_num = atoi(argv[1]); 

      if (th_num > MAX_THREAD){
            printf("Max number of threads is %d\n", MAX_THREAD);
            return -1;
      }

      pthread_t *th = (pthread_t *) malloc(th_num * sizeof(th)); //E
      pthread_attr_t custom_attr;
      pthread_attr_init(&custom_attr);

      param* p = (param*) malloc(th_num * sizeof(param));

      for (int i = 0; i < th_num; i++)
      {
            p[i].id= i;
            pthread_create(&th[i], &custom_attr, f, (void *) (p + i));
      }
      for (int i = 0; i < th_num; i++)
      {
            pthread_join(th[i], NULL);
      }

      free(th);
      free(p);
}