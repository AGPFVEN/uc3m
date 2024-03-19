#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// execute the program with args: cat t.txt
// to see the perfect demonstation

int main(int argc, char** argv) {
    pid_t pid;
    pid = fork();
    switch (pid) {
        case -1: /* error */
            exit(-1);
        case 0: /* proceso hijo */
            printf("This is son process 1\n");
            //execvp takes control of the process
            if (execvp(argv[1], &argv[1])<0) { perror("error"); }
            printf("This is son process 2\n");
            break;
        default:
            printf("Proceso padre\n");
    }
    return 0;
}