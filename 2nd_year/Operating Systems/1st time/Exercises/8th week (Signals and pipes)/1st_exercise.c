#include<stdio.h>
#include<unistd.h>
#include<signal.h>
#include<stdlib.h>

void sig_handler(int signo){
    if (signo == SIGUSR1) {
        printf("Received SIGUSR1 signal\n");
    }
}

int main(int argc, char *argv[]){
    int pid;
    struct sigaction sa1;

    pid = fork();

    if (pid == 0){
        //Son process
        sa1.sa_handler = sig_handler;
        sa1.sa_flags = 0;
        sigemptyset(&(sa1.sa_mask));
        sigaction(SIGUSR1, &sa1, NULL);
        pause();

    } else if (pid > 0) {
        //Parent process
        sleep(10);
        kill(pid, SIGUSR1);
        exit(0);

    } else {
        //Error
        printf("Fork failed\n");
        exit(1);
    }
}