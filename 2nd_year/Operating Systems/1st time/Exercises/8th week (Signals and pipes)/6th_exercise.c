#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char *argv[]){
    int fd[2];
    __pid_t pid;

    if (pipe(fd) == -1){
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    pid = fork();

    if (pid == -1){
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0){
        //Child process
        close(fd[0]);
        close(STDOUT_FILENO);
        dup(fd[1]);
        execlp("ls", "ls", NULL);
        perror("execlp");
        exit(-1);
    } else {
        //Parent
        close(fd[1]);
        close(STDIN_FILENO);
        dup(fd[0]);
        close(fd[0]);
        execlp("wc", "wc", NULL);
        perror("execlp");
    }
}