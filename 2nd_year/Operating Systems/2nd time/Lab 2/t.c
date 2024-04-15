#include <stddef.h>			/* NULL */
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>

// execute the program with args: cat t.txt
// to see the perfect demonstation

int main(int argc, char** argv) {
    int size, fd;
    if ((fd = open("1.txt", O_RDONLY)) == -1){
        perror("Error opening file in stardard input");
    }

    size = lseek(fd, 0L, SEEK_END);

    printf("%i\n", size);



    //int pid;

    //pid = fork();

    //switch (pid)
    //{
        //case 0: //son
        ////File size
        //struct stat st;
        //stat(argv[1], &st);

        //char *p;
        //p = (char *) malloc(st.st_size);
        //int fd;
        //fd = open(argv[1], O_RDONLY);
        //read(fd, p, st.st_size);
        //close(fd);
        //printf("%s\n", p);
        //printf("%i soy hijo", pid);
        //break;
    
    //default:
        //wait(0);
    //}

    return 0;
}