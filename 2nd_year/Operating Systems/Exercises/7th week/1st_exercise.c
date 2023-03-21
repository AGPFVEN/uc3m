#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>

void *thread_function(void *arg){
	for (int i = 0; i < 4; i++){
		printf("Thread says hi\n");
		sleep(1);
	}
}
int main(int argc, char *argv[]){
	pthread_t mythread;
	int ret = pthread_create(&mythread, NULL, thread_function, (void *)argv);
	if (ret != 0){
		printf("Error at creating thread\n");
	}

	printf("Waiting thread to finish\n");

	ret = pthread_join(mythread, NULL);
	if (ret != 0){
		printf("Error at joining thread\n");
	}

	printf("Thread joined\n");
}
