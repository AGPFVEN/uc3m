#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<signal.h>
#include<time.h>

void caputure_Signal1(int s){
    printf("The signal: %d has come\n", s);
    printf("Time: %ld\n", time(NULL));
}

void son_Shut_Down(int s){
    printf("The son: %d has finished\n", s);
    printf("Time: %ld\n", time(NULL));
}

int main(int argc, char *argv[]){
    int pid;
    struct sigaction sa1, sa2;

    pid = fork();

    if (pid == 0){
        //Son process
        sleep(10);
        kill(getppid(), SIGUSR1);
        sleep(3);
    } else if (pid > 0){
        //Parent process
        sa1.sa_handler = caputure_Signal1;
        sa1.sa_flags = 0;
        sigemptyset(&(sa1.sa_mask));
        sigaction(SIGUSR1, &sa1, NULL);

        sa2.sa_handler = son_Shut_Down;
        sa2.sa_flags = 0;
        sigemptyset(&(sa2.sa_mask));
        sigaction(SIGCHLD, &sa2, NULL);

        pause();

    } else {
        //Fail
        printf("Fail at creating a process\n");
    }
}